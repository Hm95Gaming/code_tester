# code_tester

Changelog Update 1.3 Ruby Update:
- Menambahkan function execute_ruby untuk testing code ruby
- Mendukung code ruby dari tingkatan rendah sampe medium (Untuk yang lebih kompleks masih belum di tes)
- Mengupdate Detect_language untuk bisa mendeteksi kode ruby
- Mengupdate language_executors untuk memanggil function execute_ruby
- Mengupdate code_presets untuk memberi contoh kodingan maupun mengetes kode ruby

Changelog Update 1.2 Frontend Full Pack Patch (Big Update):
- Ditambahkan atribut untuk menyimpan kode PHP, HTML, CSS, dan JavaScript yang akan digunakan saat memanggil metode html_set.
- Ditambahkan metode html_set(self, *args) untuk mengatur kode PHP, HTML, CSS, dan JavaScript, serta memanggil metode build_html_set untuk menghasilkan file HTML dan membukanya di browser.
- Ditambahkan metode extract_html_head_and_body(self, html_code) untuk mengekstrak kode bagian head dan body dari kode HTML yang diberikan.
- Ditambahkan metode build_html_set(self, php_code, html_code, css_code, js_code) untuk membangun file HTML dari kode PHP, HTML, CSS, dan JavaScript yang diberikan.
- Dalam metode html_set, kode telah diperbaiki untuk memeriksa dan menangani kondisi jika kode PHP, HTML, CSS, atau JavaScript tidak diberikan atau tidak valid.
- Penanganan untuk mengatasi kasus ketika kode CSS atau JavaScript tidak diberikan telah diperbaiki dengan menambahkan kondisi yang tepat.
- Dalam metode html_set, kesalahan tipe telah diperbaiki untuk mengecek kode bahasa pemrograman yang sesuai.
- Ditambahkan pengecekan untuk kode bahasa pemrograman "Javascript" sebagai alternatif untuk "JS" saat memeriksa kode CSS atau JavaScript.
- Kesalahan penamaan fungsi telah diperbaiki dengan mengganti "Javascript" menjadi "JavaScript".
- Ditambahkan penanganan kesalahan untuk mengangani situasi ketika kode bahasa pemrograman tidak sesuai urutan yang diharapkan.
- Dalam metode html_set, kode telah diperbaiki untuk mengembalikan hasil dari metode build_html_set.
- Penanganan kesalahan telah diperbaiki untuk mengatasi situasi ketika fungsi extract_html_head_and_body mengembalikan None.

Note: Dengan pembaruan ini, Anda dapat dengan mudah menggunakan fungsi html_set untuk menghasilkan halaman web dari kode PHP, HTML, CSS, dan JavaScript yang Anda berikan. Pastikan untuk menjalankan XAMPP dan akses output.php melalui localhost agar fungsi ini berfungsi dengan baik.
 
Changelog Update 1.1 CSS & JS support:

CSS Support:
- Sekarang mendukung semua properti CSS standar seperti font, color, background, margin, padding, dsb.
- Mendukung pemilihan elemen berdasarkan nama, class, atau id.
- Mendukung pemilihan elemen berdasarkan hierarki (contoh: .parent .child).
- Mendukung pseudo-class (contoh: :hover, :active, :before, :after, dsb.).
- Mendukung media queries (contoh: @media screen and (max-width: 768px)).
- Mendukung keyframes untuk animasi (contoh: @keyframes animationName { from { opacity: 0; } to { opacity: 1; } }).
- Mendukung transformasi (contoh: transform: translateX(50px);).
- Mendukung flexbox dan grid layout.
- Mendukung media query (CSS di dalamnya akan dieksekusi berdasarkan ukuran layar).
- Mendukung CSS custom properties (variabel CSS).
- Mendukung @import untuk memuat file CSS eksternal.

JavaScript Support:
- Sekarang mendukung eksekusi pernyataan JavaScript dasar seperti variabel, operasi matematika, dan fungsi.
- Mendukung manipulasi DOM (Document Object Model).
- Mendukung pembuatan fungsi dan pemanggilan fungsi.
- Mendukung kondisional seperti if-else statement.
- Mendukung penggunaan objek dan properti objek.
- Mendukung looping seperti for dan while loop.
- Mendukung penggunaan event listener.
- Mendukung penggunaan Promise (async/await).
- Mendukung penggunaan AJAX untuk berkomunikasi dengan server.
- Mendukung manipulasi elemen HTML dan konten dengan innerHTML.
- Mendukung manipulasi CSS (ubah gaya elemen HTML melalui JavaScript).
- Mendukung penggunaan alert, prompt, dan confirm untuk interaksi pengguna.

Catatan: Code Tester adalah alat sederhana dan fokus pada eksekusi kode dari berbagai bahasa pemrograman serta CSS dan JavaScript yang sederhana. Jika Anda memerlukan lingkungan pengujian yang lebih lengkap untuk proyek web yang lebih kompleks, disarankan untuk menggunakan lingkungan pengembangan web seperti XAMPP atau browser dan console developer untuk pengujian yang lebih mendalam.


Changelog Update 1.0 First Build:
- Code tester bisa mengetes 5 Bahasa total yaitu:(Python,Java,C++,PHP,dan HTML)
- Code tester mempunyai function*2 yaitu: (run_code,validate_html,run_code_preset,run_code_auto,dan show_html_output_browser)
- Code tester memiliki contoh penggunaannya dengan tanda kurung
- Code tester bisa mendeteksi kode apa yang digunakan

yang di update setelah versi awal:
- Menambahkan preset kode HTML dalam metode __init__
- Memperbarui metode run_code_auto untuk secara otomatis mendeteksi kode berdasarkan kata kunci.
- Memperbarui metode run_code_preset untuk menghandle kode HTML dan memanggil metode show_html_output_in_browser jika kode HTML valid.
