"""Tek sayfalık föyleri veriden üretir; --lab N yalnız seçili haftayı üretir."""
import argparse
import json
import os
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
FONTS = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
pdfmetrics.registerFont(TTFont('Arial', str(FONTS / 'arial.ttf')))
pdfmetrics.registerFont(TTFont('Arial-Bold', str(FONTS / 'arialbd.ttf')))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold')
NAVY, TEAL = colors.HexColor('#18314b'), colors.HexColor('#008d88')
INK, LIGHT, LINE = colors.HexColor('#24364b'), colors.HexColor('#eef5f8'), colors.HexColor('#cbdbe5')
W, H, M = 595.276, 841.89, 35
CW = W - 2*M
BASE = ParagraphStyle('body', fontName='Arial', fontSize=9.0, leading=12.2, textColor=INK)
SMALL = ParagraphStyle('small', parent=BASE, fontSize=7.0, leading=9.6)
CELL = ParagraphStyle('cell', parent=BASE, fontSize=8.2, leading=11.1)
SOURCES = {
    'K1': ('Karmetal ürün sayfası', 'https://www.karmetal.com.tr/urun/30/osa-350x450-plc.html'),
    'K3': ('ISA/IEC 62443-3-2 önizlemesi', 'https://www.isa.org/getmedia/661c718f-8e64-446d-acf9-2c6286db1b33/isa-62443-3-2-preview.pdf'),
    'K4': ('ISO 13849-1:2023 özeti', 'https://www.iso.org/standard/73481.html'),
    'K5': ('NIST SP 800-82 Rev.3', 'https://csrc.nist.gov/pubs/sp/800/82/r3/final'),
    'K8': ('SBOM 2026 rehberi', 'https://www.cyber.gov.au/publication/2026-minimum-elements-for-a-software-bill-of-materials-sbom'),
    'K9': ('FIRST CVSS rehberi', 'https://www.first.org/cvss/user-guide.html'),
    'F1': ('Dersin Lab Föyleri PDF dosyası, s. 2-5 (yerel)', None),
}

def p(text, style=BASE):
    return Paragraph(escape(text), style)

def para(c, text, top, width=CW, x=M, style=BASE):
    obj = p(text, style)
    _, height = obj.wrap(width, 1000)
    obj.drawOn(c, x, H-top-height)
    return top + height

def heading(c, text, top):
    c.setFont('Arial-Bold', 10.4)
    c.setFillColor(NAVY)
    c.drawString(M, H-top-11, text)
    return top + 20

def box(c, x, top, width, height, title, subtitle='', fill=LIGHT):
    c.setFillColor(fill)
    c.roundRect(x, H-top-height, width, height, 5, fill=1, stroke=0)
    st = ParagraphStyle('box', parent=BASE, fontName='Arial-Bold', fontSize=7.5, leading=9, alignment=TA_CENTER,
                        textColor=colors.white if fill in (NAVY, TEAL) else INK)
    text = title + ('<br/>' + subtitle if subtitle else '')
    obj = Paragraph(text, st)
    _, h = obj.wrap(width-8, height)
    assert h <= height-5, (title, h, height)
    obj.drawOn(c, x+4, H-top-(height+h)/2)

def arrow(c, x1, y1, x2, y2, label=None):
    c.setStrokeColor(TEAL)
    c.setLineWidth(1)
    c.line(x1, H-y1, x2, H-y2)
    if x2 != x1:
        d = 1 if x2 > x1 else -1
        c.line(x2, H-y2, x2-4*d, H-y2+2.5)
        c.line(x2, H-y2, x2-4*d, H-y2-2.5)
    if label:
        c.setFont('Arial-Bold', 6)
        c.setFillColor(TEAL)
        c.drawCentredString((x1+x2)/2, H-y1+5, label)

def diagram(c, lab, top):
    if lab['id'] == 1:
        top = heading(c, 'İşlevsel harita - gerçek bağlantı şeması değildir', top)
        cols = [(M, 147), (M+163, 155), (M+334, CW-334)]
        for (x, w), title, sub, fill in zip(cols,
                ['Sensör / encoder [D]', 'Normal PLC paneli [D]', 'Şerit / besleme [D]'],
                ['', 'üretim kumandası', 'tehlikeli hareket'], [LIGHT, TEAL, LIGHT]):
            box(c, x, top, w, 29, title, sub, fill)
        arrow(c, M+147, top+15, M+163, top+15)
        arrow(c, M+318, top+15, M+334, top+15)
        top += 37
        for (x, w), title, sub, fill in zip(cols,
                ['Kapak / şerit algısı [D]', 'Emniyet mantığı [B]', 'Duruş + güvenli tutma [Ö]'],
                ['koruma isteği', 'röle / Safety PLC: bilinmiyor', 'son eleman / STO: bilinmiyor'], [LIGHT, NAVY, LIGHT]):
            box(c, x, top, w, 31, title, sub, fill)
        arrow(c, M+147, top+16, M+163, top+16)
        arrow(c, M+318, top+16, M+334, top+16)
        return top+39
    if lab['id'] in (2, 4):
        top = heading(c, 'Önerilen erişim sınırları [Ö] - tüm ağ bağlantıları koşulludur', top)
        widths = [85, 101, 94, 100]
        positions = [M, M+118, M+252, M+379]
        for x, width, title, sub in zip(positions, widths,
                ['Z0 Dış servis', 'Z2 OT DMZ', 'Z3 Bakım', 'Z4 Makine'],
                ['kişisel kimlik', 'VPN / ara nokta', 'mühendislik cihazı', 'PLC / panel']):
            box(c, x, top, width, 31, title, sub, TEAL if 'Z2' in title else LIGHT)
        for i, lbl in enumerate(['C1', 'C2', 'C3']):
            arrow(c, positions[i]+widths[i], top+16, positions[i+1], top+16, lbl)
        top += 42
        box(c, M, top, 175, 30, 'Z1 Ofis [Ö]', 'Z1 -> Z4 doğrudan erişim yasak')
        box(c, M+240, top, 239, 30, 'Z5 Emniyet işlevi [Ö]', 'uzaktan emniyet yazma / reset yasak', NAVY)
        c.setStrokeColor(TEAL)
        c.line(M+165, H-(top-11), M+165, H-top)
        c.setFillColor(TEAL)
        c.setFont('Arial', 6)
        c.drawString(M+169, H-top+2, 'C5')
        # C4 is explicitly limited to status/permission signals.
        c.setStrokeColor(TEAL)
        c.line(M+429, H-(top-11), M+429, H-top)
        c.setFillColor(TEAL)
        c.setFont('Arial', 6)
        c.drawString(M+433, H-top+2, 'C4')
        return top+39
    return top

def table(c, data, top):
    hdr = ParagraphStyle('hdr', parent=CELL, fontName='Arial-Bold', textColor=colors.white)
    rows = [[p(t, hdr) for t in data['headers']]]
    rows += [[p(t, CELL) for t in row] for row in data['rows']]
    obj = Table(rows, colWidths=[CW*v for v in data['widths']])
    obj.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),NAVY), ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('GRID',(0,0),(-1,-1),0.35,LINE),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),
        ('LEFTPADDING',(0,0),(-1,-1),6), ('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),5), ('BOTTOMPADDING',(0,0),(-1,-1),5),
    ]))
    _, h = obj.wrap(CW, 1000)
    obj.drawOn(c, M, H-top-h)
    return top+h+9

def build(lab, date):
    target = OUT / lab['filename']
    c = canvas.Canvas(str(target), pagesize=(W,H), pageCompression=1)
    c.setTitle(f"Lab {lab['id']} - {lab['title']} - Karmetal OSA 350x450 PLC")
    c.setAuthor('Endüstriyel Siber Güvenlik Ders Projesi')
    c.setFillColor(NAVY)
    c.rect(0,H-86,W,86,stroke=0,fill=1)
    c.setFillColor(TEAL)
    c.rect(W-10,H-86,10,86,stroke=0,fill=1)
    c.setFillColor(colors.white)
    c.setFont('Arial-Bold',9)
    c.drawString(M,H-24,f"LABORATUVAR {lab['id']}  |  KARMETAL OSA 350x450 PLC")
    c.setFont('Arial-Bold',21 if lab['id'] != 3 else 20)
    c.drawString(M,H-53,lab['title'])
    c.setFont('Arial',8)
    c.drawString(M,H-73,'Çıktı: '+lab['output']+'  |  '+lab['ep'])
    c.setFillColor(INK)
    c.setFont('Arial-Bold',8)
    c.drawString(M,H-105,'Ad Soyad:')
    c.drawString(300,H-105,'Grup:')
    c.drawString(436,H-105,'Tarih: '+date)
    # Empty interactive fields preserve unspecified identity without inventing it.
    for name,x,w in [('ad_soyad',M+49,200),('grup',331,78)]:
        c.acroForm.textfield(name=name, tooltip=name, x=x, y=H-111, width=w,
                            height=16, borderWidth=0, fillColor=LIGHT, fontSize=9)
    top=123
    c.setFillColor(LIGHT)
    c.roundRect(M,H-top-49,CW,49,5,stroke=0,fill=1)
    end=para(c, lab['context'],top+7,CW-16,M+8)
    assert end <= top+46
    top=178
    top=para(c,'[D] Kaynakta doğrulanan  |  [B] Bilinmiyor  |  [V] Varsayım  |  [Ö] Öneri  |  [Ç] Analitik çıkarım',top,style=SMALL)+10
    top=diagram(c,lab,top)
    for section in lab['sections']:
        top=heading(c,section['heading'],top)
        if 'paragraph' in section:
            top=para(c,section['paragraph'],top)+10
        for question,answer in section.get('qa',[]):
            top=para(c,question,top,style=ParagraphStyle('q',parent=BASE,fontName='Arial-Bold'))+2
            top=para(c,answer,top)+7
        if 'table' in section:
            top=table(c,section['table'],top)
    top=para(c,lab['note'],top,style=SMALL)+6
    refs=[]
    for key in lab['refs']:
        label,url=SOURCES[key]
        if key == 'F1':
            label = f"Dersin Lab Föyleri PDF dosyası, s. {lab['source_page']} (yerel)"
        refs.append(f'<link href="{url}" color="#008d88">[{key}] {escape(label)}</link>' if url else f'[{key}] {escape(label)}')
    refs.append('Bağlantılar tıklanabilir; kaynak/kanıt kaydı: docs/KAYNAKLAR.md. Erişim: '+date+'.')
    obj=Paragraph(' | '.join(refs),SMALL)
    _,height=obj.wrap(CW,1000)
    obj.drawOn(c,M,H-top-height)
    top+=height
    if top>H-40:
        raise RuntimeError(f"Lab {lab['id']} sayfa taşıyor: {top:.1f} > {H-40:.1f}")
    c.setStrokeColor(LINE)
    c.line(M,29,W-M,29)
    c.setFillColor(INK)
    c.setFont('Arial',6.7)
    c.drawString(M,18,'Eğitim amaçlı pasif analiz; resmî denetim veya uygunluk belgesi değildir.')
    c.drawRightString(W-M,18,f"Hafta {lab['id']} | 1 / 1")
    c.showPage()
    c.save()
    print(f"{target.name}: içerik altı {top:.1f} pt; 1 sayfa")

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lab',type=int,help='Yalnız belirtilen haftayı üret')
    args=parser.parse_args()
    data=json.loads((ROOT/'data/labs.json').read_text(encoding='utf-8'))
    labs=[lab for lab in data['labs'] if args.lab is None or lab['id']==args.lab]
    if not labs:
        parser.error('İstenen hafta veride bulunamadı')
    for lab in labs:
        build(lab,lab.get('date',data['date']))
