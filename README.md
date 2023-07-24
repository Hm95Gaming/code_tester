# code_tester
 
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
