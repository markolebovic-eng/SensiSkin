<?php
/**
 * Plugin Name: SensiSkin - Forma za usluge (WooCommerce)
 * Description: Dodaje obaveznu formu (lični podaci + 3 slike) na stranicu odabranih proizvoda/usluga, pre dugmeta "Dodaj u korpu". Podaci putuju kroz korpu, checkout i porudžbinu, a slike se šalju kao prilog uz email "Nova porudžbina".
 * Version: 1.0.0
 * Author: SensiSkin
 * Text Domain: sensiskin-service-form
 * Requires Plugins: woocommerce
 */

// Sprečava direktan pristup fajlu (bezbednosna mera).
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Glavna klasa plugina.
 * Sve je smešteno u jednu klasu radi preglednosti i da se izbegne
 * sudaranje imena funkcija sa drugim pluginovima/temom.
 */
final class SensiSkin_Service_Form {

	/** Meta ključ koji čuva da li proizvod zahteva formu (yes/no). */
	const META_ZAHTEVA_FORMU = '_sensiskin_zahteva_formu';

	/** Naziv nonce polja za zaštitu forme. */
	const NONCE_ACTION = 'sensiskin_service_form_action';
	const NONCE_NAME   = 'sensiskin_service_form_nonce';

	/** Broj obaveznih upload polja za slike. */
	const BROJ_SLIKA = 3;

	public function __construct() {
		// Proveravamo da li je WooCommerce aktivan pre nego što kačimo bilo šta.
		add_action( 'plugins_loaded', array( $this, 'proveri_woocommerce' ) );
	}

	/**
	 * Ako WooCommerce nije aktivan, samo prikazujemo admin obaveštenje i ne kačimo ništa dalje.
	 */
	public function proveri_woocommerce() {
		if ( ! class_exists( 'WooCommerce' ) ) {
			add_action( 'admin_notices', function () {
				echo '<div class="notice notice-error"><p>';
				echo esc_html__( 'Plugin "SensiSkin - Forma za usluge" zahteva da WooCommerce bude instaliran i aktivan.', 'sensiskin-service-form' );
				echo '</p></div>';
			} );
			return;
		}

		$this->registruj_hookove();
	}

	/**
	 * Registracija svih WooCommerce/WordPress kuka (hooks) koje plugin koristi.
	 */
	private function registruj_hookove() {

		// 1) Admin panel: checkbox u Product Data > General tabu.
		add_action( 'woocommerce_product_options_general_product_data', array( $this, 'prikazi_admin_checkbox' ) );
		add_action( 'woocommerce_process_product_meta', array( $this, 'sacuvaj_admin_checkbox' ) );

		// 2) Prikaz forme na stranici proizvoda, pre dugmeta "Dodaj u korpu".
		add_action( 'woocommerce_before_add_to_cart_button', array( $this, 'prikazi_formu' ) );

		// 3) Prisiljavanje forme na multipart/form-data (potrebno za upload fajlova).
		add_action( 'wp_footer', array( $this, 'forsiraj_multipart_enctype' ) );

		// 4) Validacija pre dodavanja u korpu - blokira dodavanje ako forma nije popunjena ispravno.
		add_filter( 'woocommerce_add_to_cart_validation', array( $this, 'validiraj_formu' ), 10, 3 );

		// 5) Čuvanje podataka iz forme (i upload slika) kao deo stavke korpe.
		add_filter( 'woocommerce_add_cart_item_data', array( $this, 'sacuvaj_podatke_u_korpu' ), 10, 3 );

		// 6) Prikaz unetih podataka u korpi i na checkout stranici.
		add_filter( 'woocommerce_get_item_data', array( $this, 'prikazi_podatke_u_korpi' ), 10, 2 );

		// 7) Prebacivanje podataka iz stavke korpe u samu porudžbinu (order item meta).
		add_action( 'woocommerce_checkout_create_order_line_item', array( $this, 'sacuvaj_podatke_u_porudzbinu' ), 10, 4 );

		// 8) Prilaganje uploadovanih slika kao pravi email attachment uz "Nova porudžbina" email.
		add_filter( 'woocommerce_email_attachments', array( $this, 'dodaj_slike_u_email' ), 10, 3 );
	}

	/* =========================================================================
	 * 1) ADMIN: checkbox "Zahtevaj formu za uslugu" u Product Data tabu
	 * ========================================================================= */

	public function prikazi_admin_checkbox() {
		echo '<div class="options_group">';

		woocommerce_wp_checkbox( array(
			'id'          => self::META_ZAHTEVA_FORMU,
			'label'       => __( 'Zahtevaj formu za uslugu', 'sensiskin-service-form' ),
			'description' => __( 'Ako je uključeno, kupac mora popuniti formu (lični podaci + 3 slike) pre nego što može da doda ovaj proizvod u korpu.', 'sensiskin-service-form' ),
		) );

		echo '</div>';
	}

	public function sacuvaj_admin_checkbox( $post_id ) {
		$vrednost = isset( $_POST[ self::META_ZAHTEVA_FORMU ] ) ? 'yes' : 'no';
		update_post_meta( $post_id, self::META_ZAHTEVA_FORMU, $vrednost );
	}

	/**
	 * Pomoćna funkcija - proverava da li dati proizvod zahteva formu.
	 */
	private function proizvod_zahteva_formu( $product_id ) {
		return 'yes' === get_post_meta( $product_id, self::META_ZAHTEVA_FORMU, true );
	}

	/* =========================================================================
	 * 2) PRIKAZ FORME na stranici proizvoda
	 * ========================================================================= */

	public function prikazi_formu() {
		global $product;

		if ( ! $product instanceof WC_Product ) {
			return;
		}

		if ( ! $this->proizvod_zahteva_formu( $product->get_id() ) ) {
			return;
		}

		wp_nonce_field( self::NONCE_ACTION, self::NONCE_NAME );
		?>
		<div class="sensiskin-forma-usluge" style="margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 6px;">
			<h3 style="margin-top:0;"><?php esc_html_e( 'Podaci potrebni za ovu uslugu', 'sensiskin-service-form' ); ?></h3>

			<p>
				<label>
					<?php esc_html_e( 'Ime *', 'sensiskin-service-form' ); ?><br>
					<input type="text" name="sensiskin_ime" required style="width:100%;">
				</label>
			</p>

			<p>
				<label>
					<?php esc_html_e( 'Prezime *', 'sensiskin-service-form' ); ?><br>
					<input type="text" name="sensiskin_prezime" required style="width:100%;">
				</label>
			</p>

			<p>
				<label>
					<?php esc_html_e( 'Broj telefona *', 'sensiskin-service-form' ); ?><br>
					<input type="text" name="sensiskin_telefon" required style="width:100%;">
				</label>
			</p>

			<p>
				<label>
					<?php esc_html_e( 'Email *', 'sensiskin-service-form' ); ?><br>
					<input type="email" name="sensiskin_email" required style="width:100%;">
				</label>
			</p>

			<p>
				<label>
					<?php esc_html_e( 'Opis *', 'sensiskin-service-form' ); ?><br>
					<textarea name="sensiskin_opis" rows="4" required style="width:100%;"></textarea>
				</label>
			</p>

			<?php for ( $i = 1; $i <= self::BROJ_SLIKA; $i++ ) : ?>
				<p>
					<label>
						<?php
						/* translators: %d je redni broj slike (1, 2 ili 3) */
						printf( esc_html__( 'Slika %d *', 'sensiskin-service-form' ), $i );
						?><br>
						<input type="file" name="sensiskin_slika_<?php echo (int) $i; ?>" accept="image/*" required>
					</label>
				</p>
			<?php endfor; ?>

			<p>
				<label>
					<input type="checkbox" name="sensiskin_saglasnost" value="1" required>
					<?php
					printf(
						/* translators: %s je link ka stranici uslova korišćenja */
						esc_html__( 'Slažem se sa %s *', 'sensiskin-service-form' ),
						'<a href="/uslovi-koriscenja/" target="_blank" rel="noopener">' . esc_html__( 'uslovima kupovine', 'sensiskin-service-form' ) . '</a>'
					);
					?>
				</label>
			</p>
		</div>
		<?php
	}

	/**
	 * Prisiljava standardnu WooCommerce "cart" formu da koristi multipart/form-data,
	 * jer je to neophodno da bi upload fajlova (slika) uopšte stigao u $_FILES.
	 * WooCommerce po defaultu ne dodaje enctype atribut, a AJAX add-to-cart
	 * ne podržava upload fajlova - zato koristimo standardan (non-AJAX) submit
	 * i malim inline JS-om dodajemo enctype na formu.
	 */
	public function forsiraj_multipart_enctype() {
		if ( ! function_exists( 'is_product' ) || ! is_product() ) {
			return;
		}

		global $product;

		if ( ! $product instanceof WC_Product || ! $this->proizvod_zahteva_formu( $product->get_id() ) ) {
			return;
		}
		?>
		<script>
			document.addEventListener( 'DOMContentLoaded', function () {
				var forma = document.querySelector( 'form.cart' );
				if ( forma ) {
					forma.setAttribute( 'enctype', 'multipart/form-data' );
					forma.setAttribute( 'encoding', 'multipart/form-data' );
				}
			} );
		</script>
		<?php
	}

	/* =========================================================================
	 * 3) VALIDACIJA - blokira dodavanje u korpu ako forma nije ispravno popunjena
	 * ========================================================================= */

	public function validiraj_formu( $prosao, $product_id, $kolicina ) {

		if ( ! $this->proizvod_zahteva_formu( $product_id ) ) {
			return $prosao;
		}

		// Provera nonce-a (zaštita od CSRF-a).
		if ( ! isset( $_POST[ self::NONCE_NAME ] ) || ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST[ self::NONCE_NAME ] ) ), self::NONCE_ACTION ) ) {
			wc_add_notice( __( 'Došlo je do greške pri proveri forme. Molimo osvežite stranicu i pokušajte ponovo.', 'sensiskin-service-form' ), 'error' );
			return false;
		}

		$obavezna_tekstualna_polja = array(
			'sensiskin_ime'     => __( 'Ime', 'sensiskin-service-form' ),
			'sensiskin_prezime' => __( 'Prezime', 'sensiskin-service-form' ),
			'sensiskin_telefon' => __( 'Broj telefona', 'sensiskin-service-form' ),
			'sensiskin_email'   => __( 'Email', 'sensiskin-service-form' ),
			'sensiskin_opis'    => __( 'Opis', 'sensiskin-service-form' ),
		);

		foreach ( $obavezna_tekstualna_polja as $polje => $naziv ) {
			if ( empty( $_POST[ $polje ] ) ) {
				/* translators: %s je naziv polja koje nedostaje */
				wc_add_notice( sprintf( __( 'Polje "%s" je obavezno.', 'sensiskin-service-form' ), $naziv ), 'error' );
				$prosao = false;
			}
		}

		// Validacija formata email adrese.
		if ( ! empty( $_POST['sensiskin_email'] ) && ! is_email( wp_unslash( $_POST['sensiskin_email'] ) ) ) {
			wc_add_notice( __( 'Uneta email adresa nije ispravnog formata.', 'sensiskin-service-form' ), 'error' );
			$prosao = false;
		}

		// Provera checkbox-a za saglasnost sa uslovima kupovine.
		if ( empty( $_POST['sensiskin_saglasnost'] ) ) {
			wc_add_notice( __( 'Morate se saglasiti sa uslovima kupovine da biste nastavili.', 'sensiskin-service-form' ), 'error' );
			$prosao = false;
		}

		// Provera da su sve 3 slike priložene i da su zaista slike.
		for ( $i = 1; $i <= self::BROJ_SLIKA; $i++ ) {
			$polje = 'sensiskin_slika_' . $i;

			if ( empty( $_FILES[ $polje ]['name'] ) || UPLOAD_ERR_OK !== $_FILES[ $polje ]['error'] ) {
				/* translators: %d je redni broj slike */
				wc_add_notice( sprintf( __( 'Slika %d je obavezna.', 'sensiskin-service-form' ), $i ), 'error' );
				$prosao = false;
				continue;
			}

			$provera_tipa = wp_check_filetype( $_FILES[ $polje ]['name'] );
			$mime_tip     = $_FILES[ $polje ]['type'];

			if ( empty( $provera_tipa['type'] ) || strpos( $mime_tip, 'image/' ) !== 0 ) {
				/* translators: %d je redni broj slike */
				wc_add_notice( sprintf( __( 'Slika %d mora biti fajl tipa slike (jpg, png, webp...).', 'sensiskin-service-form' ), $i ), 'error' );
				$prosao = false;
			}
		}

		return $prosao;
	}

	/* =========================================================================
	 * 4) ČUVANJE PODATAKA U KORPI (upload slika + tekstualna polja)
	 * ========================================================================= */

	public function sacuvaj_podatke_u_korpu( $cart_item_data, $product_id, $variation_id ) {

		if ( ! $this->proizvod_zahteva_formu( $product_id ) ) {
			return $cart_item_data;
		}

		// Učitavamo WP admin funkcije neophodne za media_handle_upload,
		// jer front-end (shop) po defaultu nema te fajlove učitane.
		if ( ! function_exists( 'media_handle_upload' ) ) {
			require_once ABSPATH . 'wp-admin/includes/image.php';
			require_once ABSPATH . 'wp-admin/includes/file.php';
			require_once ABSPATH . 'wp-admin/includes/media.php';
		}

		$id_priloga = array();

		for ( $i = 1; $i <= self::BROJ_SLIKA; $i++ ) {
			$polje = 'sensiskin_slika_' . $i;

			if ( empty( $_FILES[ $polje ]['name'] ) ) {
				continue;
			}

			// media_handle_upload sam radi validaciju, premeštanje fajla i
			// kreiranje zapisa u Media Library-ju (attachment post).
			$attachment_id = media_handle_upload( $polje, $product_id );

			if ( ! is_wp_error( $attachment_id ) ) {
				$id_priloga[ $i ] = $attachment_id;
			}
		}

		$cart_item_data['sensiskin_podaci'] = array(
			'ime'     => sanitize_text_field( wp_unslash( $_POST['sensiskin_ime'] ?? '' ) ),
			'prezime' => sanitize_text_field( wp_unslash( $_POST['sensiskin_prezime'] ?? '' ) ),
			'telefon' => sanitize_text_field( wp_unslash( $_POST['sensiskin_telefon'] ?? '' ) ),
			'email'   => sanitize_email( wp_unslash( $_POST['sensiskin_email'] ?? '' ) ),
			'opis'    => sanitize_textarea_field( wp_unslash( $_POST['sensiskin_opis'] ?? '' ) ),
			'slike'   => $id_priloga,
		);

		// Jedinstveni ključ osigurava da se svaka porudžbina ove usluge tretira
		// kao posebna stavka korpe (različiti podaci = različita stavka).
		$cart_item_data['unique_key'] = md5( microtime() . wp_rand() );

		return $cart_item_data;
	}

	/* =========================================================================
	 * 5) PRIKAZ PODATAKA U KORPI / NA CHECKOUT STRANICI
	 * ========================================================================= */

	public function prikazi_podatke_u_korpi( $item_data, $cart_item ) {

		if ( empty( $cart_item['sensiskin_podaci'] ) ) {
			return $item_data;
		}

		$podaci = $cart_item['sensiskin_podaci'];

		$item_data[] = array(
			'key'   => __( 'Ime i prezime', 'sensiskin-service-form' ),
			'value' => esc_html( trim( $podaci['ime'] . ' ' . $podaci['prezime'] ) ),
		);
		$item_data[] = array(
			'key'   => __( 'Telefon', 'sensiskin-service-form' ),
			'value' => esc_html( $podaci['telefon'] ),
		);
		$item_data[] = array(
			'key'   => __( 'Email', 'sensiskin-service-form' ),
			'value' => esc_html( $podaci['email'] ),
		);
		$item_data[] = array(
			'key'   => __( 'Opis', 'sensiskin-service-form' ),
			'value' => esc_html( $podaci['opis'] ),
		);

		if ( ! empty( $podaci['slike'] ) ) {
			$linkovi = array();
			foreach ( $podaci['slike'] as $attachment_id ) {
				$url = wp_get_attachment_thumb_url( $attachment_id );
				if ( $url ) {
					$linkovi[] = $url;
				}
			}
			if ( $linkovi ) {
				$item_data[] = array(
					'key'   => __( 'Priložene slike', 'sensiskin-service-form' ),
					'value' => wp_kses_post( implode( '<br>', array_map( 'esc_url', $linkovi ) ) ),
				);
			}
		}

		return $item_data;
	}

	/* =========================================================================
	 * 6) PREBACIVANJE PODATAKA U PORUDŽBINU (order item meta)
	 * ========================================================================= */

	public function sacuvaj_podatke_u_porudzbinu( $item, $cart_item_key, $values, $order ) {

		if ( empty( $values['sensiskin_podaci'] ) ) {
			return;
		}

		$podaci = $values['sensiskin_podaci'];

		$item->add_meta_data( __( 'Ime i prezime', 'sensiskin-service-form' ), trim( $podaci['ime'] . ' ' . $podaci['prezime'] ) );
		$item->add_meta_data( __( 'Telefon', 'sensiskin-service-form' ), $podaci['telefon'] );
		$item->add_meta_data( __( 'Email', 'sensiskin-service-form' ), $podaci['email'] );
		$item->add_meta_data( __( 'Opis', 'sensiskin-service-form' ), $podaci['opis'] );

		if ( ! empty( $podaci['slike'] ) ) {
			$linkovi_za_prikaz = array();

			foreach ( $podaci['slike'] as $redni_broj => $attachment_id ) {
				// Meta ključevi koji počinju sa "_" su "skriveni" (protected) u
				// WooCommerce-u, tj. ne prikazuju se kupcu niti u standardnom
				// email šablonu - koristimo ih samo da kasnije nađemo fajl
				// za slanje kao pravi email attachment (vidi dodaj_slike_u_email).
				$item->add_meta_data( '_sensiskin_slika_' . $redni_broj, $attachment_id );

				$url = wp_get_attachment_url( $attachment_id );
				if ( $url ) {
					$linkovi_za_prikaz[] = $url;
				}
			}

			if ( $linkovi_za_prikaz ) {
				$item->add_meta_data( __( 'Priložene slike (linkovi)', 'sensiskin-service-form' ), implode( "\n", $linkovi_za_prikaz ) );
			}
		}
	}

	/* =========================================================================
	 * 7) PRAVI EMAIL ATTACHMENT UZ "NOVA PORUDŽBINA" EMAIL
	 * ========================================================================= */

	public function dodaj_slike_u_email( $prilozi, $email_id, $objekat ) {

		// Slike prilažemo samo uz email koji administrator dobija o novoj porudžbini.
		if ( 'new_order' !== $email_id ) {
			return $prilozi;
		}

		if ( ! $objekat instanceof WC_Order ) {
			return $prilozi;
		}

		foreach ( $objekat->get_items() as $item ) {
			for ( $i = 1; $i <= self::BROJ_SLIKA; $i++ ) {
				$attachment_id = $item->get_meta( '_sensiskin_slika_' . $i );

				if ( ! $attachment_id ) {
					continue;
				}

				$putanja_do_fajla = get_attached_file( $attachment_id );

				if ( $putanja_do_fajla && file_exists( $putanja_do_fajla ) ) {
					$prilozi[] = $putanja_do_fajla;
				}
			}
		}

		return $prilozi;
	}
}

// Pokrećemo plugin.
new SensiSkin_Service_Form();
