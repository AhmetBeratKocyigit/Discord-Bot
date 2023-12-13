# Discord Botu

![MasterHead](https://cdn.webrazzi.com/uploads/2020/11/discord-thumb-848.jpeg)

Bu proje bir Discord botu için temel bir şablondur. İlgili komutları içerir ve özel komutlar eklemek için genişletilebilir.

## Kurulum


1. **Gerekli Kütüphaneleri Yükleme:**
   - Komut istemcisine (`cmd` veya `terminal`) gidin.
   - Proje dizinine gidin.
   - Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyin:
     ```bash
     pip install discord.py
     ```

2. **Bot Token'ını Ekleyin:**
   - `bot.py` dosyasını açın.
   - `bot.run('Token')` satırındaki `'Token'` kısmını, Discord Developer Portal'dan aldığınız bot token'ıyla değiştirin.

3. **Botu Başlatma:**
   - Komut istemcisine gidin ve projenin olduğu dizine gidin.
   - Aşağıdaki komutu kullanarak botu başlatın:
     ```bash
     python bot.py
     ```

4. **Discord Sunucunuza Ekleyin:**
   - Discord Developer Portal'da bulunan uygulama sayfanıza geri dönün.
   - Sol taraftaki menüden "OAuth2" sekmesine gidin.
   - "OAuth2 URL Generator" kısmında, "OAuth2 URL" başlığı altındaki URL'yi kopyalayın.
   - Bu URL'yi bir tarayıcıda açarak, botunuzu eklemek istediğiniz sunucuyu seçerek ekleyin.

## Komutlar

- `!cal <url>`: Belirtilen URL'den ses çalar.
- `!ayril`: Sesli kanaldan ayrılır.
- `!merhaba`: Merhaba mesajı atar.
- `!at <kullanıcı> [sebep]`: Kullanıcıyı sunucudan atar.
- `!sustur <kullanıcı> [süre] [sebep]`: Kullanıcıyı belirtilen süreyle susturur.
- `!yasakla <kullanıcı> [sebep]`: Kullanıcıyı sunucudan yasaklar.
- `!temizle <mesaj sayısı>`: Belirtilen miktarda mesajı temizler.
- `!bilgi [kullanıcı]`: Belirtilen kullanıcının bilgilerini gösterir.
- `!yardim`: Yardım komutlarına erişim sağlar.
- `!ping`: Botun gecikmesini ms cinsinden gösterir.
- `!avatar [kullanıcı]`: Belirtilen kullanıcının avatarını gösterir.
- `!yaz [metin]`: Girilen metini Botun yazmasını sağlar.
- `!kullanıcılar`: Sunucudaki tüm kullanıcıların adını gösterir.
- `!sesli [metin]`: Girilen metini Botun sesli olarak okumasını sağlar.


---
**Not:** Bu bir şablondur ve projenizi geliştirmek için özelleştirebilirsiniz.
