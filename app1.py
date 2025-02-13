import pandas as pd

# Dosyayı okuyalım
df = pd.read_csv('C:\ML/ad_campaign_performance/ad_campaign_performance.csv')

# İlk birkaç satırı ve genel bilgileri inceleyelim
df.head(), df.info(), df.describe()


# En iyi performans gösteren kampanyaları belirleyelim

# Engagement Rate yerine CTR (Click-Through Rate) kullanabiliriz.
# En yüksek CTR ve Conversion Rate'e sahip ilk 10 kampanyayı belirleyelim.
top_campaigns = df.nlargest(10, ['CTR', 'Conversion_Rate'])

# Ortalama metrikleri hesaplayalım
avg_metrics = df[['CTR', 'Conversion_Rate', 'CPC', 'Budget']].mean()

# Sonuçları gösterelim
top_campaigns[['Campaign_ID', 'Platform', 'CTR', 'Conversion_Rate', 'CPC', 'Budget']], avg_metrics



# 🔍 En İyi Performans Gösteren Kampanyalar:
#İlk 10 kampanyayı incelediğimizde YouTube, Instagram ve Facebook en yüksek CTR (Click-Through Rate) sağlayan platformlar olarak öne çıkıyor.

# Öne Çıkan Kampanyalar:
#En yüksek CTR: CAMP-7G2RE6 (YouTube, 31,711% CTR, düşük bütçe: 155$)

#En yüksek Conversion Rate: CAMP-BSI9NB (LinkedIn, 13.46% dönüşüm oranı)

#En düşük CPC (Cost Per Click): CAMP-7G2RE6 (0.003$)

# 📊 Genel Ortalama Değerler:
#CTR: 388.99%
#Conversion Rate: 26.86%
#CPC: 2.97$
#Ortalama Bütçe: 24,592$

#  Öneriler:
#YouTube ve Instagram düşük bütçeyle yüksek etkileşim sağlıyor gibi görünüyor.
#LinkedIn dönüşüm açısından güçlü ancak maliyetli olabilir.
#Reklam harcamalarını optimize etmek için CPC ve dönüşüm oranı arasında bir denge kurmak gerekiyor.

import seaborn as sns
import matplotlib.pyplot as plt

# Platform bazında ortalama Conversion Rate ve CPC'yi karşılaştıralım
platform_analysis = df.groupby("Platform")[["Conversion_Rate", "CPC", "Budget"]].mean().reset_index()

# Grafikleri çizelim
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Conversion Rate grafiği
sns.barplot(data=platform_analysis, x="Platform", y="Conversion_Rate", ax=axes[0], palette="viridis")
axes[0].set_title("Platform Bazında Ortalama Conversion Rate")
axes[0].set_ylabel("Conversion Rate (%)")

# CPC grafiği
sns.barplot(data=platform_analysis, x="Platform", y="CPC", ax=axes[1], palette="magma")
axes[1].set_title("Platform Bazında Ortalama CPC (Cost Per Click)")
axes[1].set_ylabel("CPC ($)")

plt.tight_layout()
plt.show()

# Platform bazında detaylı ortalamaları gösterelim
platform_analysis

