def followMessage(name):
    message = "Halo, " + name + \
            ", terima kasih sudah menambahkan saya sebagai teman."

    return message + helpMessage()

def helpMessage():
    message = "Beberapa perintah yang dapat kamu berikan: \n\n"

    message += "1. !isi_<NRP FORMAT BARU>_<PASSWORD>\n\nUntuk mengisi IPD-mu.\n\n"
    message += "2. !help\n\nUntuk melihat perintah yang tersedia.\n\n"
    message += "3. !about\n\nUntuk mengetahui lebih banyak tentang bot ini\n\n"
    message += "Hubungi developer untuk tambahan fitur"

    return message

def aboutMessage():
    message = "Auto IPD Line Bot v 0.1\n\n"
    message += "Line bot ini berfungsi untuk membantu anda untuk membantu anda mengisi kuisioner IPD dan mata kuliah\n"
    message += "yang dibuat karena MURNI keingintahuan dan eksperimen.\n\n"
    message += "Dengan menggunakan Line Bot ini anda mengetahui dan setuju untuk: \n"

    message += "1. USE IT WITH YOUR OWN RISK\nPengembang tidak bertanggung jawab bila terjadi sesuatu\n"+\
            "kepada akun Integra ini akibat dari penggunaan script ini untuk mengisi kuisioner IPD dan mata kuliah.\n\n"

    message += "2. Line Bot ini TIDAK melakukan logging ataupun menyimpan password Integra anda. Logging HANYA\n" + \
            "dilakukan untuk keperluan DEBUGGING jika terjadi error.\n\n"

    message += "3. Line Bot ini MASIH dalam tahap pengembangan, HARAP memeriksa lagi kuisioner IPD dan matkul anda\n" + \
            "setelah menggunakan Line Bot ini."

    message += "4. Jika terjadi pesan error atau menemukan BUG, saya dengan senang hati akan mendengarnya\n" + \
            "jika anda melaporkannya."

    message += "5. Saya (developer) tidak melayani pertanyaan tentang aspek legalitas dari penggunaan Line Bot ini."

    return message

def doneMessage():
    return "Pengisian selesai, mohon periksa lagi di akun Integra anda."

def formatNRPSalahMessage():
    return "Format NRP yang kamu masukkan salah, silahkan diperiksa lagi"

def errorMessage():
    return "Maaf, terjadi kesalahan, silahkan coba lagi"