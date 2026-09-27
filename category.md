# Labeling Guide
## Thai Social Media — NLP Classifier Reference

**Version:** 1.0  
**Audience:** Labelers & Developers  
**Scope:** Thai-language / Thailand-based content only (unless stated otherwise)

---

## Table of Contents

1. [Gambling (พนัน)](#1-gambling)
2. [Pornography (ลามก)](#2-pornography)
3. [Fraud / Scam (หลอกลวง)](#3-fraud--scam)
4. [E-Cigarettes (บุหรี่ไฟฟ้า)](#4-e-cigarettes)
5. [Prostitution (ค้าประเวณี)](#5-prostitution)
6. [Kratom Drink (กระท่อม)](#6-kratom-drink)
7. [Cannabis (กัญชา)](#7-cannabis)
8. [Hate Speech](#8-hate-speech)
9. [Royal Institution & Royal Family (สถาบัน / พระบรมวงศานุวงศ์)](#9-royal-institution--royal-family)
10. [Illegal Labor Recruitment (จัดหาแรงงานเถื่อน)](#10-illegal-labor-recruitment)
11. [Illegal Firearms (อาวุธปืน)](#11-illegal-firearms)
12. [Alcohol Advertising (โฆษณาแอลกอฮอล์)](#12-alcohol-advertising)
13. [Copyright Infringement (ลิขสิทธิ์)](#13-copyright-infringement)
14. [Religion (ศาสนา)](#14-religion)
15. [Surrogacy (การรับตั้งครรภ์แทน)](#15-surrogacy)
16. [Illegal Loans (เงินกู้)](#16-illegal-loans)
17. [Forged Documents (รับทำเอกสารปลอม)](#17-forged-documents)
18. [Child Sexual Content (เด็กและเยาวชน)](#18-child-sexual-content)

---

## 1. Gambling

**Definition:** Any social media post that advertises, promotes, or facilitates gambling activities targeting a Thai audience. All gambling formats are labeled as "Gambling Advertisement" (โฆษณาพนัน).

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Any gambling format advertised on social media (online casino, sports betting, lottery, card games, slot games, etc.)
- Gambling-related keywords appear in the post

### Does Not Qualify

- Foreign-language content
- General news or opinion about gambling
- Educational content about gambling risks

### Examples

| # | Sample Text (Thai) | Label | Reason |
|---|---|---|---|
| Pass 1 | `"สมัครวันนี้รับโบนัส 100% บาคาร่าออนไลน์ จ่ายจริง ถอนได้จริง"` | Qualifies | Clear gambling advertisement with bonus offer |
| Pass 2 | `"แทงบอลออนไลน์ ได้เงินจริง สมัครฟรี ลิงก์ในไบโอ"` | Qualifies | Sports betting ad with sign-up CTA |
| Fail 1 | `"รัฐบาลควรเปิดคาสิโนถูกกฎหมายไหม? แสดงความคิดเห็น"` | Does Not Qualify | General opinion poll, no gambling service offered |
| Fail 2 | `"Online casino bonus 200% sign up now"` | Does Not Qualify | Foreign language |
| Edge 1 | `"เพจชื่อ: BetKing99TH" โพสต์รูปทีมบอลพร้อมตัวเลขราคาต่อรอง` | Qualifies | Gambling keyword in publisher name + odds image = gambling ad |
| Edge 2 | `"หวยดังแม่นมาก เลขเด็ดงวดนี้ ส่งฟรีไม่มีค่าใช้จ่าย"` | Qualifies | Lottery tip promotion is still gambling content; "ฟรี" does not exempt it |

---

## 2. Pornography

**Definition:** Explicit sexual content showing nudity or sexual acts without blur/censorship.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Post contains keywords strongly indicating pornographic content

### Does Not Qualify

- Foreign-language content
- Suggestive content without clear sexual acts
- Artistic nudity in a clearly educational or fine-art context

### Examples

| #      | Sample Text / Description                                                   | Label            | Reason                                                           |
| ------ | --------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------- |
| Pass 1 | Thumbnail showing exposed genitalia, unblurred, caption: `"คลิปใหม่มาแล้ว"` | Qualifies        | Unblurred genitalia visible in thumbnail                         |
| Pass 2 | Post with unblurred image of sexual intercourse, no caption                 | Qualifies        | Explicit visual evidence is sufficient                           |
| Fail 1 | Thumbnail where genitalia is blurred with emoji/mosaic                      | Does Not Qualify | Content is censored                                              |
| Fail 2 | Lingerie model photo with suggestive caption                                | Does Not Qualify | No nudity or sexual act visible                                  |
| Edge 1 | Thumbnail shows bare chest (female) + caption: `"หนังโป๊ใหม่ อัพเดทล่าสุด"` | Qualifies        | Nipple visible + explicit keyword confirming pornographic intent |
| Edge 2 | Artistic painting of a nude figure shared in a museum context               | Does Not Qualify | Fine-art context; no sexual act; no explicit keyword             |

---

## 3. Fraud / Scam

**Definition:** Content in Thai that involves impersonation of official agencies or documented victim reports of fraud.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- An official source (government agency, organization) or a verified victim is cited
- Clear evidence of impersonation, false claims, or financial deception

### Does Not Qualify

- Foreign-language content
- General opinions or complaints without official backing
- Satirical content clearly labeled as such

### Examples

| # | Sample Text (Thai) | Label | Reason |
|---|---|---|---|
| Pass 1 | `"DSI แจ้งเตือน! มิจฉาชีพแอบอ้างเป็นธนาคารกสิกร หลอกโอนเงิน ผู้เสียหายกว่า 200 คน"` | Qualifies | Official agency (DSI) cited, victims reported |
| Pass 2 | `"ผู้เสียหายแจ้งความ บริษัทลงทุน X หลอกหลวง สูญเงิน 3 ล้าน"` | Qualifies | Victim filed official complaint |
| Fail 1 | `"ระวังแอปนี้ มันหลอกทุกคน อย่าโหลด"` | Does Not Qualify | Personal opinion, no official source |
| Fail 2 | `"Scam alert: this investment platform is fake"` | Does Not Qualify | Foreign language |
| Edge 1 | Screenshot of a LINE message impersonating SCB Bank, shared by a private user with no official report | Does Not Qualify | No official source or victim complaint — treated as general warning opinion |
| Edge 2 | Post by an NGO documenting a scam with victim interviews but no police report | Qualifies (borderline) | NGO with documented victims qualifies as an official source with victim data; escalate for review if uncertain |

---

## 4. E-Cigarettes

**Definition:** Posts advertising the sale of e-cigarettes or e-liquid in Thailand.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Clear intent to sell e-cigarettes or e-liquid (not just a review)
- Price is visible or language indicates a purchase transaction (สั่งซื้อ, inbox, ทักมา, สั่งได้เลย)

### Does Not Qualify

- Foreign-language content
- Reviews or opinions about e-cigarettes
- General discussion or news about e-cigarette policy
- Posts without any price or purchase signal

### Examples

| # | Sample Text (Thai) | Label | Reason |
|---|---|---|---|
| Pass 1 | `"พอตราคาถูก ส่งทั่วไทย ตัวละ 250 บาท ทักมาเลย"` | Qualifies | Selling keyword + price + purchase CTA |
| Pass 2 | `"น้ำยาบุหรี่ครบทุกกลิ่น สั่งขั้นต่ำ 3 ขวด ราคาส่ง"` | Qualifies | E-liquid sale with order minimum |
| Fail 1 | `"รีวิว พอต XX รุ่นใหม่ ดีไหม? คุ้มมั้ย?"` | Does Not Qualify | Product review, no price or sale intent |
| Fail 2 | `"รัฐบาลควรถูกกฎหมายบุหรี่ไฟฟ้าไหม?"` | Does Not Qualify | General opinion/policy discussion |
| Edge 1 | Post showing e-cigarette image with caption `"ของมีพร้อม ทักสอบถามได้"` but no price | Qualifies | "ทักสอบถาม" + product image = purchase signal even without an explicit price |
| Edge 2 | Account named `"VapeShopBangkok"` posts a lifestyle photo with no product or price visible | Does Not Qualify | Keyword in account name alone without sale evidence in this specific post is insufficient |

---

## 5. Prostitution

**Definition:** Posts offering paid sexual services in Thailand. All three components below are required for a post to qualify.

### Qualifies

| Component                       | Examples                                            |
| ------------------------------- | --------------------------------------------------- |
| 2.1 Price / Compensation        | ราคา, ค่าตัว, โอนมัดจำ, ราคาคุยได้                  |
| 2.2 Sexual relationship implied | ฟีลแฟน, ค้างคืน, ไม่บวกเพิ่ม, ขาวตรงปก, ถุงเท่านั้น |
| 2.3 Self-offer / Invitation     | รับงาน, พร้อมดูแล, พร้อม, ได้ค่ะ, inbox มาเลย       |

### Does Not Qualify

- Foreign-language content
- General opinions or dating posts
- Seeking a partner without a price (FWB, หาคนเลี้ยงดู, หาแฟน)
- Seeking a sugar daddy/mommy without an explicit sexual offer and price

### Examples

| #      | Sample Text (Thai)                                       | Label            | Reason                                                              |
| ------ | -------------------------------------------------------- | ---------------- | ------------------------------------------------------------------- |
| Pass 1 | `"รับงาน ค้างคืนได้ ถุงเท่านั้น ราคา 2,500 ทักมาเลยค่ะ"` | Qualifies        | All 3 components                                                    |
| Pass 2 | `"พร้อมดูแล ฟีลแฟน ค่าตัว inbox คุย"`                    | Qualifies        | All 3 components                                                    |
| Fail 1 | `"หาแฟน อยากมีคนดูแล ไม่ได้หาเงิน"`                      | Does Not Qualify | No price, no sexual offer                                           |
| Fail 2 | `"หา FWB อายุ 25+ ไม่เอาจริงจัง"`                        | Does Not Qualify | FWB explicitly excluded                                             |
| Fail 3 | `"หาสปอนเซอร์ดูแลค่าใช้จ่ายประจำเดือน"`                  | Does Not Qualify | Seeking financial support only, no sexual offer                     |
| Edge 1 | `"พร้อมนะคะ ค้างคืนได้ ทักมา"`                           | Does Not Qualify | Component 2.1 (price) is missing; all 3 must be present             |
| Edge 2 | `"รับงานกทม. ราคาตามตกลง ฟีลแฟน inbox ได้เลย"`           | Qualifies        | "ราคาตามตกลง" counts as a price signal + sexual signal + self-offer |

---

## 6. Kratom Drink

**Definition:** Posts advertising the sale of processed kratom drink (น้ำกระท่อม) in Thailand. Raw leaves do not qualify.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Product is processed into liquid form (น้ำกระท่อม)
- Keywords explicitly indicate kratom drink in the post
- Price is visible or a purchase signal is present

### Does Not Qualify

- Foreign-language content
- Keywords referring only to raw kratom leaves (ใบกระท่อม)
- No keyword indicating liquid kratom
- No price or purchase signal
- General opinions or news

### Keyword Signals

> น้ำกระท่อม, กระท่อมพร้อมดื่ม, กระท่อมขวด, ส่งน้ำกระท่อม, 4×100

### Examples

| # | Sample Text (Thai) | Label | Reason |
|---|---|---|---|
| Pass 1 | `"น้ำกระท่อมสด ขวดละ 30 ส่งทั่วประเทศ ทักได้เลย"` | Qualifies | Liquid kratom + price + purchase CTA |
| Pass 2 | `"มีน้ำกระท่อมพร้อมส่ง สั่งขั้นต่ำ 10 ขวด"` | Qualifies | Liquid kratom + purchase signal |
| Fail 1 | `"ขายใบกระท่อมสด กิโลละ 50 บาท"` | Does Not Qualify | Raw leaves only, not processed drink |
| Fail 2 | `"กระท่อมดีต่อสุขภาพจริงไหม?"` | Does Not Qualify | General opinion, no sale signal |
| Edge 1 | Post with photo of a dark liquid bottle, no text other than `"ของมี inbox"` | Does Not Qualify | Cannot confirm it is kratom drink without a keyword |
| Edge 2 | `"กระท่อม 4×100 ราคาส่ง"` | Qualifies | "4×100" is a recognized kratom drink formula keyword + price reference |

---

## 7. Cannabis

**Definition:** Posts advertising the sale of cannabis flower/buds in Thailand. Covers flower/bud formats only.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- If the only keyword is "ดอก" (without "กัญชา"), a recognized strain name combined with a cannabis image together qualify
- Price is visible or a purchase signal is present

### Does Not Qualify

- Foreign-language content
- General opinions or news

### Examples

| #      | Sample Text (Thai)                                   | Label            | Reason                                                                           |
| ------ | ---------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------- |
| Pass 1 | `"กัญชาพรีเมียม สายพันธุ์ OG Kush กรัมละ 300 ทักมา"` | Qualifies        | Keyword + strain name + price                                                    |
| Pass 2 | `"Bud สด ราคาส่ง ส่งทั่วไทย inbox ได้เลย"`           | Qualifies        | Keyword + purchase signal                                                        |
| Fail 1 | `"ภาพสวยงามของดอกกัญชา #nature"`                     | Does Not Qualify | No sale keyword or price                                                         |
| Fail 2 | `"กัญชาทางการแพทย์ดีอย่างไร?"`                       | Does Not Qualify | No sale intent                                                                   |
| Edge 1 | `"สายพันธุ์ Gorilla Glue มีของพร้อมส่ง ราคา inbox"`  | Qualifies        | Recognized strain name + purchase signal; no image is required in buy-sell posts |

---

## 8. Hate Speech

**Definition:** Content that attacks, incites hatred, or provokes conflict against individuals or groups based on race, religion, nationality, or other group identity.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Contains insults, hate speech, incitement, or provocative language targeting a race, religion, group of people, country, temple, religious objects, or rituals

### Does Not Qualify

- Foreign-language content
- No insults, hateful language, or incitement present
- Critical academic or journalistic discussion of sensitive topics without incitement

### Examples

| #      | Sample Text (Thai)                                                        | Label            | Reason                                       |
| ------ | ------------------------------------------------------------------------- | ---------------- | -------------------------------------------- |
| Pass 1 | `"[กลุ่มชาติพันธุ์] พวกนี้ไม่มีคุณค่า ควรไล่ออกจากประเทศ"`                | Qualifies        | Direct ethnic hate speech                    |
| Fail 1 | `"ฉันไม่เห็นด้วยกับนโยบายของรัฐบาล X"`                                    | Does Not Qualify | Policy criticism, not hate speech            |
| Fail 2 | `"Immigrants are ruining the country"`                                    | Does Not Qualify | Foreign language                             |
| Edge 1 | Post sharing a news article about ethnic conflict with a neutral caption  | Does Not Qualify | Informational share without incitement       |
| Edge 2 | `"ไอ้พวก [ศาสนา] บ้า ทำลายสังคม"`                                         | Qualifies        | Clear incitement targeting a religious group |

---

## 9. Royal Institution & Royal Family

**Definition:** Two sub-categories covering content that defames the monarchy or disrespects any member of the Royal Family.

### 9.1 Royal Institution (Lèse-majesté)

#### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Defamatory, mocking, or inciting content (text or image) targeting any of these four individuals:
  1. พระมหากษัตริย์ (the King)
  2. พระราชินี (the Queen)
  3. ผู้สำเร็จราชการแทน (the Regent)
  4. ผู้สืบสันตติวงศ์ / รัชทายาท (the Crown Prince — สมเด็จพระเจ้าลูกยาเธอ เจ้าฟ้าทีปังกรรัศมีโชติฯ)

#### Does Not Qualify

- Foreign-language content
- No defamatory or inciting content
- The word "กษัตริย์" appearing alone (exception: กษัตริย์ + โอ qualifies)
- Criticism of law 112 itself, not the institution
- The phrase "ตระกูลปรสิต" alone without other clearly identifying context

---

### 9.2 Royal Family Members (พระบรมวงศานุวงศ์)

Applies to all members of the Royal Family.

#### Qualifies

- Posts containing insults or defamatory language directed at any royal family member
- Inappropriate text accompanying royal images
- Non-Thai language posts qualify if they contain clearly identifiable royal images combined with inappropriate content

#### Does Not Qualify

- Respectful posts featuring royal images
- The word "กษัตริย์" appearing alone

### Examples

| #      | Sample Text / Description                                                          | Label            | Reason                                                     |
| ------ | ---------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------- |
| Pass 1 | Thai post: `"[ชื่อพระองค์] เป็นพวกโกงชาติ"`                                        | Qualifies (9.1)  | Direct defamation of a monarch                             |
| Fail 1 | "สถาบันกษัตริย์" mentioned neutrally in a history article                          | Does Not Qualify | Neutral academic reference                                 |
| Fail 2 | `"กฎหมาย 112 ไม่ยุติธรรม ควรยกเลิก"`                                               | Does Not Qualify | Criticism of the law, not the institution                  |
| Edge 1 | `"ตระกูลปรสิต"` alone, no other context                                            | Does Not Qualify | Phrase alone without identifying context is excluded       |
| Edge 2 | English post: `"Thai royals are [insult]"` with a clearly identifiable royal photo | Qualifies (9.2)  | Language exemption applies; royal image + insult qualifies |
| Edge 3 | `"กษัตริย์โอ"` in post                                                             | Qualifies        | "กษัตริย์ + โอ" is an exception that qualifies             |

---

## 10. Illegal Labor Recruitment

**Definition:** Posts recruiting workers for illegal or grey-area jobs in Thailand.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Job is clearly illegal or grey-area: แก๊งคอลเซ็นเตอร์, แรงงานต่างด้าวผิดกฎหมาย, ผีน้อย, งานสายเทา, งานสายดำ
- Post is a job listing, recruitment ad, or a request for identity scanning (รับสแกนหน้า)

### Does Not Qualify

- Foreign-language content
- Legitimate legal job postings
- General news about illegal labor

### Examples

| # | Sample Text (Thai) | Label | Reason |
|---|---|---|---|
| Pass 1 | `"รับสมัครงานสายเทา รายได้ดี ไม่ต้องมีประสบการณ์ ทักมา"` | Qualifies | Explicit grey-area job recruitment |
| Pass 2 | `"รับสแกนหน้า บัตรประชาชน จ่ายวันละ 500"` | Qualifies | Identity scanning request = illegal activity recruitment |
| Fail 1 | `"รับสมัครพนักงานบริษัท สวัสดิการดี มีประกันสังคม"` | Does Not Qualify | Legitimate employment |
| Fail 2 | `"ข่าว: ตำรวจบุกจับแก๊งคอลเซ็นเตอร์"` | Does Not Qualify | News report, not recruitment |
| Edge 1 | `"งานออนไลน์ รายได้วันละ 3,000 ไม่ต้องออกจากบ้าน ทักด่วน"` | Borderline — escalate | High pay + urgency may indicate illegal work; check further context before labeling |
| Edge 2 | `"รับงานต่างประเทศ เงินเดือนสูง ไม่ต้องมีวีซ่า"` | Qualifies | "ไม่ต้องมีวีซ่า" signals an undocumented illegal work arrangement |

---

## 11. Illegal Firearms

**Definition:** Posts advertising the sale of unregistered firearms in Thailand.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Contains the keyword "ปืนเถื่อน" or "ปืนไม่มีทะเบียน" in the post body
- Price is visible or a purchase signal is present

### Does Not Qualify

- Foreign-language content
- Legal / registered firearms (ปืนถูกกฎหมาย, ปืนมีทะเบียน)
- Modified or improvised firearms (ปืนแปลง, ปืนประดิษฐ์)
- Posts with no keyword for unregistered firearms
- General news

### Examples

| #      | Sample Text (Thai)                           | Label            | Reason                                  |
| ------ | -------------------------------------------- | ---------------- | --------------------------------------- |
| Pass 1 | `"ปืนเถื่อน ราคาถูก ส่งทั่วไทย ทักได้เลย"`   | Qualifies        | Mandatory keyword + price               |
| Pass 2 | `"มีปืนไม่มีทะเบียน พร้อมส่ง inbox ราคาคุย"` | Qualifies        | Mandatory keyword + purchase signal     |
| Fail 1 | `"ขายปืน Glock 17 มีทะเบียนครบ ราคา 25,000"` | Does Not Qualify | Registered firearm                      |
| Fail 2 | `"รีวิวปืนรุ่นใหม่ ดีไหม?"`                  | Does Not Qualify | No sale intent, no unregistered keyword |
| Edge 1 | `"ขายปืนแปลง ราคาถูก"`                       | Does Not Qualify | Modified firearm — explicitly excluded  |

---

## 12. Alcohol Advertising

**Definition:** Posts advertising the sale of alcoholic beverages in Thailand.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Price is visible or language indicates a purchase transaction
- Alcohol-related keywords are present

### Does Not Qualify

- Foreign-language content
- No alcohol keyword
- General news or reviews about alcohol

### Examples

| #      | Sample Text (Thai)                           | Label            | Reason                                           |
| ------ | -------------------------------------------- | ---------------- | ------------------------------------------------ |
| Pass 1 | `"เหล้านำเข้า ราคาส่ง ขวดละ 350 ส่งถึงบ้าน"` | Qualifies        | Alcohol keyword + price + delivery offer         |
| Pass 2 | `"ไวน์ราคาดี สั่งได้ทาง inbox ส่งทั่วกทม."`  | Qualifies        | Alcohol + purchase signal                        |
| Fail 1 | `"รีวิวบาร์แห่งใหม่ย่านทองหล่อ บรรยากาศดี"`  | Does Not Qualify | Review/editorial, no sale                        |
| Fail 2 | `"Best whisky deals this week"`              | Does Not Qualify | Foreign language                                 |
| Edge 1 | `"ปาร์ตี้คืนนี้ มีเบียร์ฟรี! มาเลย"`         | Does Not Qualify | Free giveaway at an event, not a commercial sale |
| Edge 2 | `"เบียร์โฮมเมดขาย ลิตรละ 120"`               | Qualifies        | Alcohol + explicit price = sale                  |

---

## 13. Copyright Infringement

**Definition:** Posts illegally distributing copyrighted films or streaming unauthorized sports content online.

### Qualifies

- Post distributes a copyrighted film (หนังออนไลน์) or streams live sports (เว็บบอลออนไลน์) without authorization

### Does Not Qualify

- Legal streaming platforms promoting their own licensed content
- Film reviews or trailer sharing without an unauthorized access link

### Examples

| #      | Sample Text / Description                                          | Label            | Reason                                                      |
| ------ | ------------------------------------------------------------------ | ---------------- | ----------------------------------------------------------- |
| Pass 1 | Post: `"[ชื่อหนัง] HD พากย์ไทย"` + thumbnail + link to pirate site | Qualifies        | keyword                                                     |
| Pass 2 | `"ดูบอลสด [ลีก] คืนนี้ฟรี"                                         | Qualifies        | keyword                                                     |
| Fail 1 | `"[ชื่อหนัง] ดีมากเลย ใครดูบ้าง?"`                                 | Does Not Qualify | No access link                                              |
| Fail 2 | `"ดูหนังออนไลน์ที่ Netflix"`                                       | Does Not Qualify | Licensed platform                                           |
| Edge 1 | Link goes to a Google Drive folder containing a film file          | Qualifies        | Google Drive link with a film file counts as an access link |

---

## 14. Religion

**Definition:** Content that mocks, distorts, or attacks sacred religious figures or objects.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Content mocks, distorts, or attacks sacred figures (พระพุทธเจ้า / religious founders) or religious icons (พระพุทธรูป)

### Does Not Qualify

- Foreign-language content
- No mockery or defamation of sacred figures or objects
- General news or journalism about religious topics
- General opinions about religious news or monks
- Mocking of temples, religious instruments, or rituals
- Insulting religious leaders or scholars

> Note: Coverage is narrowed to focus primarily on mockery of the Buddha and core sacred figures. Temples, rituals, and religious scholars are out of scope.

### Examples

| #      | Sample Text / Description                                | Label            | Reason                                                                                 |
| ------ | -------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------- |
| Pass 1 | `"พระพุทธเจ้าเป็นตัวตลก ล้าสมัย"`                        | Qualifies        | Direct defamation of the Buddha                                                        |
| Fail 1 | `"วัดนี้สวยมาก แนะนำให้มาเที่ยว"`                        | Does Not Qualify | Positive content                                                                       |
| Fail 2 | `"พระสงฆ์ทุจริต เป็นข่าวใหญ่"`                           | Does Not Qualify | News about monks, not mockery of sacred figures                                        |
| Edge 1 | Meme mocking a Buddhist temple ceremony                  | Does Not Qualify | Temples and rituals are out of scope                                                   |
| Edge 2 | Post insulting a famous monk by name with crude language | Does Not Qualify | Insulting religious scholars is out of scope; re-evaluate as Hate Speech if applicable |

---

## 15. Surrogacy

**Definition:** Posts offering commercial surrogacy services in Thailand.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Explicitly offers to carry a pregnancy for compensation (รับจ้างตั้งครรภ์แทน, รับอุ้มบุญ)

### Does Not Qualify

- Foreign-language content
- Unrelated to surrogacy
- General opinions or news about surrogacy
- Blog articles or educational content

### Examples

| #      | Sample Text (Thai)                                                                    | Label            | Reason                                                                                  |
| ------ | ------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------- |
| Pass 1 | `"รับอุ้มบุญ มีประสบการณ์ ติดต่อ inbox"`                                              | Qualifies        | Direct surrogacy offer                                                                  |
| Pass 2 | `"รับตั้งครรภ์แทน ค่าตอบแทนตกลงได้ สนใจทักมา"`                                        | Qualifies        | Surrogacy offer with compensation                                                       |
| Fail 1 | `"อุ้มบุญควรถูกกฎหมายในไทยไหม?"`                                                      | Does Not Qualify | General opinion                                                                         |
| Fail 2 | `"คลินิกช่วยมีบุตร IVF ราคาเริ่มต้น"`                                                 | Does Not Qualify | IVF clinic, not a surrogacy offer                                                       |
| Edge 1 | `"หาคุณแม่อุ้มบุญ ให้ค่าตอบแทนสูง"` (posted by a would-be parent seeking a surrogate) | Qualifies        | Solicitation of surrogacy falls in the same category; both offering and seeking qualify |

---

## 16. Illegal Loans

**Definition:** Posts advertising loans with interest rates exceeding the legal limit of 15% per year, or loans with floating/unregulated interest.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Interest rate explicitly exceeds 15% per year, or uses floating interest (ดอกลอย)
- Tiered/escalating loan schemes where the rate exceeds 15%

### Does Not Qualify

- Foreign-language content
- General opinions or news

### Examples

| # | Sample Text (Thai) | Label | Reason |
|---|---|---|---|
| Pass 1 | `"ปล่อยกู้ ดอก 20% ต่อเดือน อนุมัติไว"` | Qualifies | 20% per month far exceeds the 15% annual legal limit |
| Pass 2 | `"กู้เงินด่วน ดอกลอย จ่ายตามยอดที่เหลือ"` | Qualifies | Floating interest = illegal |
| Fail 1 | `"สินเชื่อส่วนบุคคล ดอก 12% ต่อปี ผ่อนสบาย"` | Does Not Qualify | Below the 15% annual limit |
| Fail 2 | `"ธนาคารแห่งใหม่เปิดบริการสินเชื่อ"` | Does Not Qualify | News, no rate information |
| Edge 1 | Loan ad showing "ดอก 3% ต่อเดือน" | Qualifies | 3%/month = 36%/year — clearly exceeds 15% even though the monthly figure looks small |
| Edge 2 | Tiered rate table showing ranges with no statement of exceeding 15% | Does Not Qualify | Ambiguous table without confirmation of excess; cannot assume |

---

## 17. Forged Documents

**Definition:** Posts offering to create, sell, or falsify official documents.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Text, image, or clip shows activity of making, selling, or forging documents such as: เอกสารราชการ, วุฒิการศึกษา, บัตรประชาชน, ใบขับขี่, ใบรับรองแพทย์, พาสปอร์ต

### Does Not Qualify

- Foreign-language content
- No evidence of document forgery activity
- General opinions or news articles

### Examples

| # | Sample Text (Thai) | Label | Reason |
|---|---|---|---|
| Pass 1 | `"รับทำใบรับรองแพทย์ ใบลาป่วย ราคา 200 บาท"` | Qualifies | Explicit forgery offer for an official document |
| Pass 2 | `"ทำวุฒิปลอม ป.ตรี-โท ราคา 1,500 ส่งภายใน 3 วัน"` | Qualifies | Degree forgery |
| Fail 1 | `"ทำไมเอกสารราชการถึงช้าจัง ไม่พอใจ"` | Does Not Qualify | Complaint, not forgery |
| Fail 2 | `"ข่าว: จับแก๊งปลอมบัตรประชาชน"` | Does Not Qualify | News report |
| Edge 1 | `"ช่วยแก้ไขเอกสาร PDF ให้หน่อยได้ไหม?"` | Does Not Qualify | Ambiguous; document editing alone does not imply forgery without official document context |
| Edge 2 | `"รับทำ portfolio สวยๆ ดูน่าเชื่อถือ"` | Does Not Qualify | Portfolio design, not official document forgery |

---

## 18. Child Sexual Content

**Definition:** Sexual content involving minors (under 18 years old) in Thailand. This is the highest-priority category.

### Qualifies

- Content is in Thai or clearly targets a Thai audience
- Image, clip, or text involves a person clearly under 18 in a sexual or indecent context
- Sexualized content explicitly referencing minors qualifies

### Does Not Qualify

- Foreign-language content
- No sexual or indecent content involving minors
- Age is unclear
- Keywords referencing "เด็ก" in a non-youth context (e.g., เด็กเอ็น, เด็กเสี่ย) do not qualify

> Critical note: If a post appears to involve sexual content but the person's age is unclear, do not leave it uncategorized — move it to Category 2 (Pornography).

### Examples

| # | Sample Text / Description | Label | Reason |
|---|---|---|---|
| Pass 1 | Image of a clearly young child in a sexual pose | Qualifies (Cat. 18) | Minor + sexual content |
| Pass 2 | `"คลิปนักเรียนมัธยม [sexual content]"` | Qualifies (Cat. 18) | "นักเรียนมัธยม" implies a minor; sexual context confirmed |
| Fail 1 | `"เด็กเอ็น น่ารักมาก"` (celebrity nickname, not a minor) | Does Not Qualify | "เด็ก" used as a nickname, not referring to a youth |
| Fail 2 | `"เด็กเสี่ย ชอบ"` | Does Not Qualify | Slang for a specific adult persona, not a minor |
| Edge 1 | Explicit image, age of person unclear | Escalate to Category 2 | Unclear age defaults to Pornography category, not Child category |
| Edge 2 | Anime/drawn sexual content depicting what appears to be a young character | Qualifies (Cat. 18) | Illustrated minors in a sexual context still qualify |
