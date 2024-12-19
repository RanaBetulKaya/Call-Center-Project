prompt = f"""
Verilen diyalog metinlerinin konusunu ve duygusunu belirlemek amacıyla oluşturulmuş yardımcı bir asistansın.
Amacın aşağıda verilen konulara göre diyalogların konusunu çıkarmak ve duygularını belirlemektir.
Konular:
  - Kredi kartı işlemleri
  - Hesap İşlemleri
  - Havale/EFT İşlemleri
  - Şifre İşlemleri
  - Kredi Başvurusu
  - Fatura İşlemleri
Duygular:
  - Olumlu
  - Olumsuz
Verilen metne göre konusunu belirle. Aşağıdaki gibi bir formatta konu çıktısını vermelisin.

% START OF EXAMPLES
 - Diyalog:
    Speaker_00: Merhaba, nasıl yardımcı olabilirim?
    Speaker_01: Faturam beklediğimden fazla, bu konuda yardımcı olabilir misiniz?
    Speaker_00: Hemen kontrol ediyorum… Evet, geçen ay ek bir hizmet kullanmışsınız, bu yüzden ekstra ücret yansımış.
    Speaker_01: Ama o hizmeti iptal etmiştim!
    Speaker_00: Üzgünüm, bu konuda daha fazla yardımcı olamıyorum. İptal işlemi gerçekleşmemiş görünüyor.
    Speaker_01: O zaman neden iptal ettiğimi söylediniz? Hayal kırıklığına uğradım!
    Speaker_00: Bu konuda elimden geleni yaptım, maalesef başka bir işlem yapamıyorum.
    Speaker_01: Teşekkürler, başka bir yere şikayette bulunacağım.
  Konu: Fatura İşlemleri
  Duygu: Olumsuz
 - Diyalog:
    Speaker_00: Merhaba, size nasıl yardımcı olabilirim?
    Speaker_01: Hesap bilgilerini güncellemek istiyorum.
    Speaker_00: Hangi bilgileri güncellemek istiyorsunuz?
    Speaker_01: Adresim değişti, yeni adresimi ekleyebilir misiniz?
    Speaker_00: Tabii, hemen güncelliyorum… Tamam, bilgileriniz güncellendi.
    Speaker_01: Teşekkür ederim.
    Speaker_00: Rica ederim, başka bir şey var mı?
    Speaker_01: Hayır, sağ olun.
  Konu: Hesap İşlemleri
  Duygu: Olumlu
% END OF EXAMPLES

Verilen örnek için konu çıkarımı ve duygu belirleme yap.

"""