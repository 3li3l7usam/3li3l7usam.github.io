# -*- coding: utf-8 -*-
# Content for alialhusam site: every project of the long portfolio + the AI / behind-the-scenes updates.

CATS = [('campaigns', 'Campaigns & events'), ('presentations', 'Presentations'),
        ('social', 'Social media'), ('earlier', 'Earlier work')]

BRIEFS = {
 'AC': ('The city changes. The promise stays.',
        'Launch a premium chauffeur service in five international cities with a clear luxury position.',
        'The car and the message stay fixed while the skyline changes, so every post is news and part of one series.',
        'Golden-hour skylines, a dark sedan and the copper mark: luxury, kept simple.'),
 'ND': ('Pride, told through the people of industry.',
        'Celebrate National Day as a story about Saudi industry and the people behind it.',
        '‘Our pride is in our industry’: every scene puts a Saudi figure at the heart of production.',
        'Directed AI scenes in deep industrial blues and warm golden light, with heritage patterns inside modern factories.'),
 'SF': ('One theme, from the roadside to the VIP lounge.',
        'Present MODON as the home for food manufacturers and draw investors to its pavilion.',
        'One theme split into four value messages, each on its own touchpoint along the visitor’s path.',
        'MODON greens and angular facets framing factory scenes of Saudi women at work.'),
 'RM': ('One season, one light, every audience.',
        'One Ramadan identity for every greeting, from the minister to staff and investors.',
        'Light as the symbol of the month, around a hand-lettered ‘Ramadan Kareem’ wordmark.',
        'A blue-to-green glow taken from MODON’s own palette, so the season feels part of the brand.'),
 'RQ': ('A campaign employees can see themselves in.',
        'Raise employee participation at every stage, from nominations to workshops and voting.',
        '‘Ideas start with you’: employees shown as the authors of change. Nominate, participate, make an impact.',
        'Real colleagues, deep navy and light-blue type for an authentic tone rather than a promotional one.'),
 'DD': ('Change starts with your turn.',
        'Invite employees to shape their workplace through surveys, ideas and voting.',
        '‘It’s your turn’: from teaser to winners, people see their input change something.',
        'Calm MODON blues with a lime highlight on every call to action, friendly and practical.'),
 'EF': ('Hospitality, made festive.',
        'A joyful Eid theme that feels new yet belongs to the same family as Ramadan.',
        'The Saudi coffee pot, a symbol of welcome, inside a hand-lettered ‘Eid Mubarak’ wordmark.',
        'Glossy 3D festive objects on a soft blue-to-white wash: modern, playful and warm.'),
 'EA': ('Calm, white and sky blue for the Hajj season.',
        'Greet every audience with a calm, respectful tone and carry practical Eid messages in one theme.',
        'Peace and pilgrimage: calligraphy with doves over photography of pilgrims.',
        'White and sky blue for purity and calm, applied the same way to cards, email and ads.'),
 'GN': ('Two flags, one gesture.',
        'Congratulate the Gulf states on their national days and express Saudi brotherhood.',
        'The neighbour’s flag beside the Saudi flag, above that country’s iconic skyline.',
        'Hand-painted watercolour for a warm, human feel, with one composition for all five cards.'),
 'SE': ('From bystander to hero.',
        'Get people to report electrical hazards: keep a safe distance, then report through the app.',
        'Every report is an act of heroism: a cape of light turns ordinary Saudis into quiet heroes.',
        'Blue-hour scenes in electric blues, with orange kept only for the safety message.'),
 'MF': ('Following the pilgrim, step by step.',
        'A dignified, spiritual presence for the Fund during the Hajj season.',
        'Four posts follow the pilgrim’s journey: supplication, Labbaik, Arafah and Tawaf.',
        'Large calligraphic headlines over light pilgrim photography, with generous white space.'),
 'YF': ('One big idea per post.',
        'Help young people build better habits in entrepreneurship and saving.',
        'One number or one word per post, understood in the second it takes to scroll.',
        'Deep indigo and golden yellow, cut-out portraits and oversized numerals.'),
}

BTS = {
 'ND': dict(img='20_AI_Process/ND_Spaces_Canvas.jpg', window='Magnific Spaces — National Day 96', title='Directed in Magnific Spaces',
            steps=[('Reference board', 'Locations, light, Sadu patterns and the MODON mark grouped as one input.'),
                   ('Generate and branch', 'Each scene explored in variations and compared side by side on one canvas.'),
                   ('Select and finish', 'Chosen frames upscaled, then composed with the campaign wordmark.')]),
 'SE': dict(img='20_AI_Process/EF_Spaces_Canvas.jpg', window='Magnific Spaces — Electricity Friend', title='From brief to hero',
            steps=[('Brief', 'One idea: a cape of light turns everyday people into quiet heroes.'),
                   ('Generate', 'Blue-hour scenes generated with Nano Banana Pro, one for each everyday moment.'),
                   ('Design', 'Selected scenes upscaled, then the type, the safe-distance line and the app call-to-action set in Photoshop.')]),
 'SF': dict(img='20_AI_Process/SF_Spaces_Canvas.jpg', window='Magnific Spaces — Saudifood Show 2026', title='From canvas to venue',
            steps=[('Reference', 'Factory floors, robotic lines and MODON buildings collected as one board.'),
                   ('Generate', 'Image Generator nodes branch every scene into options before one is chosen.'),
                   ('Apply', 'The chosen scenes framed in the theme’s green facets on flags, fences, gates and the VIP wall.')]),
}

ND, AC, SE, SFH, SFM, SF0 = ('02_National_Day_96/', '01_Altanfeethi_Chauffeur/', '19_Saudi_Energy/',
                             '03_Saudifood_2026/mockups_hd/', '03_Saudifood_2026/mockups/', '03_Saudifood_2026/')
PR, SM = '12_Presentations/', '13_Social_Media/'

def jpg(folder, *names): return [folder + n + ('' if n.endswith(('.jpg', '.png')) else '.jpg') for n in names]

PROJECTS = [
 dict(slug='national-day-96', cat='campaigns', title='National Day 96', sub='Our pride is our industry.', client='MODON', brief='ND', bts='ND', ai=True, feat=True,
      summary='A national day campaign built on one visual idea: Saudi industry, seen through the people who drive it. Every scene was directed and generated with AI, then unified into one visual language for posters, greetings, stickers and city screens.',
      facts=[('Client', 'MODON'), ('Role', 'Concept, visual direction and design'), ('Scope', 'Posters, greetings, stickers, screens'), ('AI tools', 'Magnific Spaces, Nano Banana Pro, Photoshop')],
      hero=ND + 'ND_Screen_Wide_Triple.jpg', cover=ND + 'ND_Izzuna_01.jpg',
      images=jpg(ND, 'ND_Izzuna_01', 'ND_Izzuna_02', 'ND_Izzuna_03', 'ND_Izzuna_04', 'ND_Izzuna_05', 'ND_Izzuna_06',
                 'ND_Screen_Main_Building', 'ND_Screen_Landmark', 'ND_Screen_Road', 'ND_Greeting_Investors', 'ND_Greeting_Employees') + [ND + 'ND_Sticker_01_White.png']),
 dict(slug='altanfeethi-chauffeur', cat='campaigns', title='Altanfeethi Chauffeur', sub='One journey, five cities.', client='Altanfeethi', brief='AC', ai=True, feat=True,
      summary='A social media campaign announcing a chauffeur service’s arrival in five international cities. One adaptable layout lets every city feel distinct while the series reads as a single brand.',
      facts=[('Client', 'Altanfeethi'), ('Role', 'Planning, structure and design'), ('Scope', 'Social media series, 5 cities'), ('AI tools', 'Magnific, Photoshop')],
      hero=None, cover=AC + 'AC_Rome.jpg',
      images=jpg(AC, 'AC_New-York_02', 'AC_Rome', 'AC_Vienna', 'AC_Abu-Dhabi', 'AC_Amman', 'AC_New-York_01')),
 dict(slug='electricity-friend', cat='campaigns', title='Electricity Friend', sub='From bystander to hero.', client='Saudi Energy', brief='SE', bts='SE', ai=True, feat=True,
      summary='A national public-safety campaign that turns people into the grid’s first line of safety: spot exposed electrical equipment, keep a safe distance and report it in seconds through the app.',
      facts=[('Client', 'Saudi Energy'), ('Role', 'Concept, visual direction and design'), ('Scope', 'Key visuals, poster series, digital'), ('AI tools', 'Magnific, Nano Banana Pro, Photoshop')],
      hero=SE + 'SE_Safe_Distance_Landscape.jpg', cover=SE + 'SE_Poster_Be_The_Hero.jpg',
      images=jpg(SE, 'SE_Poster_Be_The_Hero', 'SE_Poster_Dont_Ignore', 'SE_Poster_True_Eye', 'SE_Poster_How_To', 'SE_Poster_Never_Ignores', 'SE_Safe_Distance_Portrait')),
 dict(slug='saudifood-show-2026', cat='campaigns', title='Saudifood Show 2026', sub='One theme, every touchpoint.', client='MODON', brief='SF', bts='SF', ai=True, feat=True,
      summary='A dedicated theme and the full design suite for MODON’s participation in The Saudifood Show, from outdoor and VIP branding to invitations and digital banners.',
      facts=[('Client', 'MODON'), ('Role', 'Event theme and design'), ('Scope', 'Outdoor, VIP, print, digital'), ('AI tools', 'Magnific Spaces, Photoshop, Illustrator')],
      hero=SFH + 'SF_Final_Flags.jpg', cover=SFH + 'SF_Final_VIP_Wall.jpg',
      images=[SFH + 'SF_Final_VIP_Wall.jpg', SFH + 'SF_Final_Fence.jpg', SFH + 'SF_V13_Exit_Gates.jpg', SFH + 'SF_V13_VIP_Glass.jpg',
              SFM + 'SF_Mock_Digital.jpg', SFM + 'SF_Mock_Invitations.jpg', SF0 + 'SF_Invitation_Investors.jpg', SF0 + 'SF_Invitation_Internal.jpg']),
 dict(slug='campaign-key-visuals', cat='campaigns', title='Campaign key visuals', sub='Cinematic scenes for print and social.', client='MODON', ai=True, feat=True,
      summary='Two campaign visuals for MODON’s industry story. A young industrial professional blended with an aerial view of an industrial city, and a backlit lightbox that opens the story with a Saudi craftsman in bilingual copy.',
      facts=[('Client', 'MODON'), ('Role', 'Design'), ('Formats', 'Social campaign visual, lightbox print'), ('AI tools', 'Magnific, Photoshop')],
      hero=None, cover=SM + 'SM_Watan_Story.jpg',
      images=[SM + 'SM_Watan_Story.jpg', SM + 'SM_Harf_Lightbox_Mockup.jpg', SM + 'SM_Harf_Lightbox.jpg']),
 dict(slug='ramadan-1447', cat='campaigns', title='Ramadan 1447', sub='A theme for the season.', client='MODON, Ministry of Industry', brief='RM', feat=True,
      summary='A seasonal theme for MODON: a hand-lettered wordmark, a blue-to-green light gradient and one layout system, applied to every greeting from the minister’s message to staff and investor cards.',
      facts=[('Client', 'MODON, Ministry of Industry'), ('Role', 'Theme and design'), ('Scope', 'Wordmark, greeting posters, cards')],
      hero=None, cover='04_Ramadan_1447/RM_Greeting_Minister.jpg',
      images=jpg('04_Ramadan_1447/', 'RM_Greeting_Minister', 'RM_Greeting_Employees_01', 'RM_Greeting_Employees_02', 'RM_Greeting_Investors', 'RM_Greeting_Link_Ad') + ['04_Ramadan_1447/RM_Wordmark_Calligraphy.png']),
 dict(slug='eid-al-fitr-1447', cat='campaigns', title='Eid al-Fitr 1447', sub='Soft blue, glossy gold.', client='MODON, Ministry of Industry', brief='EF',
      summary='A seasonal theme for MODON: a hand-lettered Eid wordmark, glossy 3D festive objects and a soft blue-to-green wash, applied to the minister’s greeting in three treatments.',
      facts=[('Client', 'MODON, Ministry of Industry'), ('Role', 'Theme and design'), ('Scope', 'Greeting posters, identity')],
      hero='10_Eid_Al-Fitr_1447/EF_Identity_01.jpg', cover='10_Eid_Al-Fitr_1447/EF_Minister_Greeting.jpg',
      images=jpg('10_Eid_Al-Fitr_1447/', 'EF_Minister_Greeting', 'EF_Minister_Alt_01', 'EF_Minister_Alt_02', 'EF_Identity_02', 'EF_Identity_03')),
 dict(slug='eid-al-adha-1447', cat='campaigns', title='Eid al-Adha 1447', sub='Sky blue, white and prayer.', client='MODON', brief='EA',
      summary='A calm seasonal theme for the Hajj season: hand-drawn calligraphy with doves, photography of pilgrims and a white-to-sky-blue palette, applied to e-cards, email and digital ads.',
      facts=[('Client', 'MODON'), ('Role', 'Theme and design'), ('Scope', 'E-cards, email, digital ads')],
      hero='11_Eid_Al-Adha_1447/EA_Identity_01.jpg', cover='11_Eid_Al-Adha_1447/EA_Cards_Download_Ad.jpg',
      images=jpg('11_Eid_Al-Adha_1447/', 'EA_Identity_02', 'EA_Identity_03', 'EA_Identity_07', 'EA_Cards_Download_Ad', 'EA_Email_Work_Hours',
                 'EA_Greeting_Minister', 'EA_Greeting_Investors', 'EA_Greeting_CEO_Employees', 'EA_Card_01', 'EA_Card_02', 'EA_Card_03', 'EA_Card_04', 'EA_Card_05', 'EA_Card_06', 'EA_Card_07')),
 dict(slug='ruqi', cat='campaigns', title='Ruqi', sub='Every voice, one campaign.', client='MODON', brief='RQ',
      summary='An internal campaign inviting MODON employees to take part in the Participation Enhancement initiative, from nominations and workshop invitations to voting. One unified campaign, conceived, directed and designed end to end.',
      facts=[('Client', 'MODON'), ('Role', 'Concept, direction and design'), ('Scope', 'Posters, invitations, voting')],
      hero=None, cover='05_Ruqi/RQ_Poster_Main.jpg',
      images=['05_Ruqi/RQ_Logo.png'] + jpg('05_Ruqi/', 'RQ_Poster_Main', 'RQ_Poster_Ideas', 'RQ_Poster_Nominate', 'RQ_Poster_Time_To_Join', 'RQ_Poster_Objectives',
                                           'RQ_Poster_Applications_Open', 'RQ_Poster_Conditions', 'RQ_Poster_Workshop_Jeddah', 'RQ_Poster_Workshop_Dammam', 'RQ_Poster_Vote', 'RQ_Poster_Thanks')),
 dict(slug='dour-dourak', cat='campaigns', title='Dour Dourak', sub='Your turn to shape the workplace.', client='MODON', brief='DD',
      summary='An internal MODON initiative inviting employees to help shape their work environment. One calm visual system guides colleagues from the first teaser through nominations and voting to the winners’ announcement.',
      facts=[('Client', 'MODON'), ('Role', 'Identity and campaign design'), ('Scope', 'Teasers, voting, surveys, results')],
      hero='07_Dour_Dourak/DD_Screen_Teaser.jpg', cover='07_Dour_Dourak/DD_Close_to_You.jpg',
      images=jpg('07_Dour_Dourak/', 'DD_Logo', 'DD_Close_to_You', 'DD_Your_Space', 'DD_Change_01', 'DD_Change_02', 'DD_Change_03', 'DD_Screen_Goals', 'DD_Screen_Mechanism',
                 'DD_Screen_Conditions', 'DD_Survey', 'DD_Phase2_A', 'DD_Phase2_B', 'DD_Vote_Central', 'DD_Vote_East', 'DD_Vote_West', 'DD_Vote_BuildingA', 'DD_Vote_BuildingB', 'DD_Winners')),
 dict(slug='gulf-national-days', cat='campaigns', title='Gulf National Days', sub='A card for every neighbour.', client='Altanfeethi', brief='GN',
      summary='A social campaign congratulating the Gulf states on their national days. Each watercolour card sets the neighbour’s flag beside the Saudi flag above an iconic skyline, so five countries read as one gesture.',
      facts=[('Client', 'Altanfeethi'), ('Role', 'Campaign design'), ('Scope', '5 national day cards')],
      hero=None, cover='14_Gulf_National_Days/GN_UAE.jpg',
      images=jpg('14_Gulf_National_Days/', 'GN_UAE', 'GN_Bahrain', 'GN_Kuwait', 'GN_Oman', 'GN_Qatar')),
 dict(slug='martyrs-fund-eid-al-adha', cat='campaigns', title='Eid al-Adha for the Martyrs’ Fund', sub='Four posts for the Hajj season.', client='Martyrs’ Fund', brief='MF',
      summary='A social series for the Hajj season, built around four moments: supplication, Labbaik, the Day of Arafah and Tawaf. Calm calligraphy over pilgrim photography keeps the set quiet and consistent.',
      facts=[('Client', 'Martyrs’ Fund'), ('Role', 'Campaign design'), ('Scope', '4 social posts')],
      hero=None, cover='16_Martyrs_Fund_Eid_Al-Adha/MF_02_Labbaik.png',
      images=['16_Martyrs_Fund_Eid_Al-Adha/MF_01_Supplication.png', '16_Martyrs_Fund_Eid_Al-Adha/MF_02_Labbaik.png', '16_Martyrs_Fund_Eid_Al-Adha/MF_03_Arafah.png', '16_Martyrs_Fund_Eid_Al-Adha/MF_04_Tawaf.png']),
 dict(slug='y-foundation', cat='campaigns', title='Y Foundation', sub='Bold type, one idea per post.', client='Y Foundation', brief='YF',
      summary='A social series for Y Foundation on entrepreneurship and saving: quotes, tips and founder stories in a deep indigo and gold palette, with one big headline per post.',
      facts=[('Client', 'Y Foundation'), ('Role', 'Campaign design'), ('Scope', '4 social posts')],
      hero=None, cover='17_Y_Foundation/YFN_01.png',
      images=['17_Y_Foundation/YFN_0%d.png' % i for i in range(1, 5)]),
 # ---- presentations
 dict(slug='new-horizons', cat='presentations', title='New Horizons', sub='MODON company profile.', client='MODON', feat=True,
      summary='An investor-facing profile of MODON’s industrial cities, enabling services and investment opportunities, structured as a clean 23-slide deck. One grid and one icon set keep dense content easy to read.',
      facts=[('Client', 'MODON'), ('Role', 'Presentation design'), ('Format', '23 slides, English')],
      hero=PR + 'PR_Mockup_Horizons.jpg', cover=PR + 'PR_Mockup_Horizons.jpg',
      images=jpg(PR, 'PR_HZ_01', 'PR_HZ_02', 'PR_HZ_03', 'PR_HZ_04', 'PR_HZ_05', 'PR_HZ_06', 'PR_HZ_12', 'PR_HZ_14', 'PR_HZ_22')),
 dict(slug='hirafiyoon', cat='presentations', title='Hirafiyoon', sub='Year of Handicrafts 2025.', client='MODON',
      summary='A short briefing deck on Hirafiyoon, MODON’s offer for craft enterprises in its industrial cities: objectives, key facts and programme impact, prepared for the Minister of Industry in Arabic.',
      facts=[('Client', 'MODON'), ('Role', 'Presentation design'), ('Format', '8 slides, Arabic')],
      hero=PR + 'PR_Mockup_Hirafiyoon.jpg', cover=PR + 'PR_Mockup_Hirafiyoon.jpg',
      images=jpg(PR, 'PR_HR_01', 'PR_HR_02', 'PR_HR_03', 'PR_HR_04', 'PR_HR_05', 'PR_HR_06', 'PR_HR_07')),
 dict(slug='expo-2030-riyadh', cat='presentations', title='Expo 2030 Riyadh', sub='Industry Pavilion concept.', client='MODON',
      summary='A concept deck for MODON’s participation in Expo 2030 Riyadh: strategic positioning, timeline, pavilion zones and immersive visual renders, in Arabic.',
      facts=[('Client', 'MODON'), ('Role', 'Presentation design'), ('Format', '18 slides, Arabic')],
      hero=PR + 'PR_Mockup_Journey.jpg', cover=PR + 'PR_Mockup_Journey.jpg',
      images=jpg(PR, 'PR_PJ_01', 'PR_PJ_02', 'PR_PJ_03', 'PR_PJ_04', 'PR_PJ_06', 'PR_PJ_10', 'PR_PJ_11', 'PR_PJ_12', 'PR_PJ_14', 'PR_PJ_16', 'PR_PJ_17')),
 dict(slug='impact-maker', cat='presentations', title='Impact Maker', sub='MODON Industrial Excellence Award.', client='MODON',
      summary='A concept and programme deck for an honorary track recognising individuals who shaped Saudi industry, in Arabic, from rationale to ceremony programme.',
      facts=[('Client', 'MODON'), ('Role', 'Presentation design'), ('Format', '12 slides, Arabic')],
      hero=PR + 'PR_Mockup_Impact.jpg', cover=PR + 'PR_Mockup_Impact.jpg',
      images=jpg(PR, 'PR_IM_01', 'PR_IM_02', 'PR_IM_03', 'PR_IM_05', 'PR_IM_06', 'PR_IM_07', 'PR_IM_09', 'PR_IM_10', 'PR_IM_11')),
 dict(slug='bonded-zone', cat='presentations', title='Bonded Zone', sub='Jeddah 3rd Industrial City.', client='MODON',
      summary='An investment proposal for a bonded-zone logistics opportunity: market demand, site masterplan and land use, told in 14 slides.',
      facts=[('Client', 'MODON'), ('Role', 'Presentation design'), ('Format', '14 slides, English')],
      hero=PR + 'PR_Mockup_Jeddah.jpg', cover=PR + 'PR_JD_11.jpg',
      images=jpg(PR, 'PR_JD_01', 'PR_JD_03', 'PR_JD_05', 'PR_JD_06', 'PR_JD_07', 'PR_JD_10', 'PR_JD_11', 'PR_JD_13')),
 # ---- social
 dict(slug='modon-announcements', cat='social', title='MODON announcements', sub='Milestones, made shareable.', client='MODON',
      summary='A website launch, two executive recognitions and a speech summary, each in the format its channel needs and with one clear message per frame.',
      facts=[('Client', 'MODON'), ('Role', 'Design'), ('Formats', 'Stories, posts, infographic')],
      hero=SM + 'SM_BRF_Speech_Photo.jpg', cover=SM + 'SM_Website_Launch.jpg',
      images=jpg(SM, 'SM_Website_Launch', 'SM_Top100_CEO_00', 'SM_Top100_CEO_01', 'SM_Top100_CEO_02', 'SM_Top30_CEO', 'SM_BRF_Speech_Infographic')),
 dict(slug='industry-carousels', cat='social', title='Industry carousels', sub='Growth figures, slide by slide.', client='MODON',
      summary='Two swipeable carousels: food and pharma industries growth figures told slide by slide, and a new multi-story factory model explained in six swipes.',
      facts=[('Client', 'MODON'), ('Role', 'Design'), ('Formats', '5-slide and 6-slide carousels')],
      hero=None, cover=SM + 'SM_FoodIndustries_01.jpg',
      images=jpg(SM, 'SM_FoodIndustries_01', 'SM_FoodIndustries_02', 'SM_FoodIndustries_03', 'SM_FoodIndustries_04', 'SM_FoodIndustries_05',
                 'SM_MultiStory_01', 'SM_MultiStory_02', 'SM_MultiStory_03', 'SM_MultiStory_04', 'SM_MultiStory_05', 'SM_MultiStory_06')),
 dict(slug='altanfeethi-social', cat='social', title='Altanfeethi social', sub='Always-on social content.', client='Altanfeethi',
      summary='Occasion posts and brand-message posts for Altanfeethi, from national celebrations and Mother’s Day to Ramadan, all in one warm, dark palette with the copper mark.',
      facts=[('Client', 'Altanfeethi'), ('Role', 'Design'), ('Scope', 'Occasion posts, brand messages')],
      hero=None, cover='15_Altanfeethi_Social/AS_King_Anniversary.jpg',
      images=jpg('15_Altanfeethi_Social/', 'AS_Mothers_Day', 'AS_King_Anniversary', 'AS_AlUla_Congrats', 'AS_Ramadan', 'AS_Earth_Hour',
                 'AS_Msg_Premium', 'AS_Msg_Empowerment', 'AS_Msg_Hospitality', 'AS_Msg_Communication')),
 dict(slug='yafoooh', cat='social', title='Yafoooh', sub='Fragrance posts for the feed.', client='Yafoooh',
      summary='Social posts for Yafoooh, from product hero shots and seasonal offers to a brand-voice poster for the nation, each built around one bottle, one message and a single offer.',
      facts=[('Client', 'Yafoooh'), ('Role', 'Design'), ('Scope', 'Product and offer posts')],
      hero=None, cover='18_Yafoooh_Social/YS_Best_Seller_55C.jpg',
      images=['18_Yafoooh_Social/YS_Best_Seller_55C.jpg', '18_Yafoooh_Social/YS_Black_Winter.png', '18_Yafoooh_Social/YS_Prayer_For_The_Nation.jpg',
              '18_Yafoooh_Social/YS_Founding_Day_Offer.jpg', '18_Yafoooh_Social/YS_National_Day_95.jpg', '18_Yafoooh_Social/YS_Gift_Offer_Musk.jpg', '18_Yafoooh_Social/YS_Opening_Offer.png']),
 # ---- earlier
 dict(slug='logo-design', cat='earlier', title='Logo design', sub='Selected marks.', client='Various clients', plate=True,
      summary='Marks for brands across media, software, retail and fragrance, each reduced to one clear idea that holds up from an app icon to a storefront.',
      facts=[('Clients', 'Skyme, Jadeer, Twix Media, Hadiyati, Viviano, Wahida, Yafoooh, Eques and others'), ('Role', 'Logo design')],
      hero=None, cover='06_Earlier_Work/Logos/11_eques.png',
      images=['06_Earlier_Work/Logos/%s.png' % n for n in ('01_skyme', '02_jadeer', '03_twix_media', '04_hadiyati', '05_lamset_musamem', '06_viviano',
                                                           '07_wahida', '08_dragon_software', '09_jas', '10_yafoooh', '11_eques')]),
 dict(slug='annual-report-and-profile', cat='earlier', title='Annual report and company profile', sub='Long documents, made easy to read.', client='University Vice Presidency for Development, Health Eye Medical',
      summary='An annual report for the University Vice Presidency for Development (2018) and a company profile for Health Eye Medical, laid out on clear grids with data and photography.',
      facts=[('Clients', 'University Vice Presidency for Development, Health Eye Medical'), ('Role', 'Editorial design')],
      hero=None, cover='06_Earlier_Work/Company_Profiles/p33_01.png',
      images=['06_Earlier_Work/Company_Profiles/p3%d_0%d.png' % (a, b) for a in (3, 4) for b in range(1, 5)]),
 dict(slug='packaging', cat='earlier', title='Fragrance packaging', sub='Boxes, shown as finished products.', client='Fragrance brands',
      summary='Box designs for fragrance brands, shown as finished product shots.',
      facts=[('Clients', 'Fragrance brands'), ('Role', 'Packaging design')],
      hero=None, cover='06_Earlier_Work/Packaging/p36_01.png',
      images=['06_Earlier_Work/Packaging/p36_0%d.png' % i for i in range(1, 5)]),
]

FEATURED = ['national-day-96', 'altanfeethi-chauffeur', 'electricity-friend', 'saudifood-show-2026', 'campaign-key-visuals', 'ramadan-1447', 'new-horizons']

TOOLKIT = [('Ideas and concept', 'Claude, ChatGPT', 'Analysing the brief and building the idea, the copy direction and the prompts.'),
           ('Image', 'Magnific, Photoshop', 'Scenes generated in Magnific Spaces with Nano Banana Pro, upscaled with Magnific, then retouched and composited in Photoshop.'),
           ('Video', 'Higgsfield, Flow', 'Key frames turned into motion: image-to-video shots and short sequences.'),
           ('Design and delivery', 'Adobe Creative Cloud', 'Illustrator, InDesign, Photoshop, After Effects and Premiere Pro for identity, layout, motion and final files.')]

PROCESS = [('Idea', 'Claude and ChatGPT', 'The brief analysed and the idea built, down to the copy direction and the prompts.'),
           ('Reference', 'Magnific Spaces', 'Location, light, people and cultural detail gathered as one board.'),
           ('Generate', 'Magnific with Nano Banana Pro', 'Scenes directed and iterated side by side on one canvas.'),
           ('Refine and animate', 'Photoshop, Higgsfield, Flow', 'Upscaling, retouching and compositing, then key frames turned into motion.'),
           ('Design', 'Adobe Creative Cloud', 'Typography, layout and roll-out to every format and screen.')]

CLIENT_LOGOS = ['ministry_white', 'modon_white', 'saudi_energy_white', 'industrial_center_white', 'altanfeethi_white', 'martyrs_fund_white', 'yafoooh_white']

FEEDBACK = [  # fill these in; the section stays hidden on the live site while any quote is a placeholder
    dict(quote='', name='', role='', project='National Day 96'),
    dict(quote='', name='', role='', project='Altanfeethi Chauffeur'),
    dict(quote='', name='', role='', project='Electricity Friend'),
]

CONTACT = dict(email='3li.3l7osam@gmail.com', phone='+966 53 607 0382', behance='https://www.behance.net/3li3l7usam', linkedin='')

# ======================================================================== v4: booths, step-by-step boards, sketch-first process
CATS = [('campaigns', 'Campaigns & events'), ('booths', 'Exhibition booths'), ('presentations', 'Presentations'),
        ('social', 'Social media'), ('earlier', 'Earlier work')]

BRIEFS['QR'] = ('A stand you can smell from the aisle.',
                'Give a heritage food brand a stand that draws visitors in and keeps them seated.',
                'A live grill counter at the front, a red lounge behind it and a castle-edge wall that reads from across the hall.',
                'Brand red and warm white, a hanging header sign, and the logo repeated at every eye level.')
BRIEFS['AJ'] = ('Gateway of the Guests of God.',
                'Present a pilgrim transport company at the Hajj exhibition on a tight 51 m² corner plot.',
                'A 4 m corner tower as the landmark, pointed arches for the Hajj journey, and three glowing Tawaf rings over the majlis.',
                'Beige travertine, walnut slats, brass and warm 3000K light: calm, hospitable and premium.')

BT = '22_Booths/'
PROJECTS[4:4] = [
 dict(slug='alojour-booth', cat='booths', title='Alojour booth', sub='Gateway of the Guests of God.', client='Alojour for transporting pilgrims', brief='AJ', feat=True,
      summary='An exhibition booth for a pilgrim transport company at the Hajj exhibition: a 51 m² L-shaped corner stand with a walnut tower, pointed arches, a majlis under three hanging Tawaf rings, a reception counter and a hospitality bar.',
      facts=[('Client', 'Alojour for transporting pilgrims'), ('Role', 'Concept, 3D design and rendering'), ('Scope', 'Booth design, renders, plan with dimensions'), ('Tools', 'Blender, Cycles, ChatGPT')],
      hero=BT + 'renders/AJ_CAM_01_Hero_Front.jpg', cover=BT + 'renders/AJ_CAM_02_Frontal_Diagonal.jpg',
      images=[BT + 'renders/AJ_%s.jpg' % n for n in ('CAM_02_Frontal_Diagonal', 'CAM_16_Low_Angle_Hero', 'CAM_03_Left_Wing_Reception', 'CAM_04_Right_Wing_Cafe',
              'CAM_07_Majlis_Interior', 'CAM_14_Tawaf_Rings', 'CAM_12_Tower_Logo_Halo', 'CAM_08_Bar_Cafe', 'CAM_17_Bar_Shelves', 'CAM_06_Reception_Close',
              'CAM_05_Aerial', 'CAM_10_TopPlan_Dimensions')]),
 dict(slug='alqaryah-booth', cat='booths', title='Al-Qaryah booth', sub='A stand built around a live grill.', client='Al-Qaryah', brief='QR', feat=True,
      summary='An exhibition booth for a heritage food brand: a red-and-white stand with a castle-edge back wall, a hanging header sign, a live grill counter, a lounge and a bar.',
      facts=[('Client', 'Al-Qaryah'), ('Role', 'Concept, 3D design and rendering'), ('Scope', 'Booth design, renders, plan'), ('Tools', 'Blender, Cycles, ChatGPT')],
      hero=BT + 'renders/QR_01_hero_left.jpg', cover=BT + 'renders/QR_02_front.jpg',
      images=[BT + 'renders/QR_%s.jpg' % n for n in ('02_front', '03_hero_right', '04_interior', '05_grill', '06_left_side', '07_plan')]),
]

ST, MI = '21_Process/', '03_Saudifood_2026/mockups/_magnific_in/'
def _booth(k, plan, plan_lab, caps, second=('_front_1_outline.jpg', 'Front')):
    return [('Sketch and plan', 'Pen and paper', [(BT + k + '_0_sketch.jpg', 'Concept sketch'), (BT + k + plan, plan_lab)], caps[0]),
            ('Outline', 'Blender', [(BT + k + '_1_outline.jpg', 'Outline'), (BT + k + second[0], second[1])], caps[1]),
            ('Place the models', 'Blender', [(BT + k + '_2_models.jpg', 'Models placed'), (BT + k + '_int_2_models.jpg', 'Interior')], caps[2]),
            ('Render', 'Blender, Cycles', [(BT + k + '_3_render.jpg', 'Final render'), (BT + k + '_int_3_render.jpg', 'Interior')], caps[3])]

# step-by-step boards shown on each project page: (step, tools, [(image, label)], caption)
STEPS = {
 'national-day-96': [
    ('Sketch and references', 'Pen and paper, Magnific Spaces', [(ST + 'ND_Sketch.jpg', 'Concept sketch'), (ST + 'ND_Ref_Board.jpg', 'Reference board'), (ST + 'ND_Ref_Pattern.jpg', 'Sadu and wordmark')],
     'The idea drawn first: one figure, one long street, the sun at its end. Locations, light and Sadu patterns gathered as one board.'),
    ('Generate and branch', 'Magnific Spaces, Nano Banana Pro', [(ST + 'ND_Gen_Craft.jpg', 'Handicraft'), (ST + 'ND_Gen_Robotics.jpg', 'Robotics')],
     'Each scene generated in variations and compared side by side until the light and palette matched across the series.'),
    ('Compose and roll out', 'Photoshop, Illustrator', [(ND + 'ND_Izzuna_01.jpg', 'Final poster'), (ND + 'ND_Screen_Road.jpg', 'City screen'), (ND + 'ND_Screen_Landmark.jpg', 'Landmark screen')],
     'Chosen frames upscaled and retouched, then set with the campaign wordmark and rolled out to screens and greetings.')],
 'altanfeethi-chauffeur': [
    ('Sketch the layout', 'Pen and paper', [(ST + 'AC_Sketch.jpg', 'Concept sketch')],
     'Car and road at the base, the message panel above them, the city filling the sky: the grid every post follows.'),
    ('Generate the cities', 'Magnific, Nano Banana Pro', [(ST + 'AC_Gen_Rome.jpg', 'Rome'), (ST + 'AC_Gen_Vienna.jpg', 'Vienna'), (ST + 'AC_Gen_Amman.jpg', 'Amman'), (ST + 'AC_Gen_New-York.jpg', 'New York')],
     'Each skyline generated at the same golden hour and eye level, so it drops into the frame without retouching.'),
    ('Place and finish', 'Photoshop', [(AC + 'AC_Abu-Dhabi.jpg', 'Final post')],
     'The car, road and Arabic headline composited over the city, with the brand mark kept in one fixed position.')],
 'electricity-friend': [
    ('Sketch and brief', 'Pen and paper, Claude, ChatGPT', [(ST + 'EF_Sketch.jpg', 'Concept sketch'), (ST + 'EF_Ref_Brief.jpg', 'Brief to prompts')],
     'One idea sketched first: a cape of light and a safe distance from the cabinet. The brief then written as prompts.'),
    ('Generate the scenes', 'Magnific Spaces, Nano Banana Pro', [(ST + 'EF_Gen_Night.jpg', 'Night street'), (ST + 'EF_Gen_Cape.jpg', 'Cape of light')],
     'Blue-hour scenes generated one per everyday moment, keeping the same light, wardrobe and glowing cape.'),
    ('Type and call to action', 'Photoshop', [(SE + 'SE_Poster_Dont_Ignore.jpg', 'Poster'), (SE + 'SE_Poster_True_Eye.jpg', 'Poster')],
     'Selected scenes upscaled, then the headline, the orange safe-distance line and the app call to action set in Photoshop.')],
 'saudifood-show-2026': [
    ('Sketch the site', 'Pen and paper, site photos', [(ST + 'SF_Sketch.jpg', 'Concept sketch'), (MI + 'bg_flags.png', 'Empty site')],
     'A row of flags in front of the pavilion sketched over the real entrance, with the empty site as the base plate.'),
    ('Design flat', 'Illustrator, Photoshop', [(MI + 'design_flag_%d.jpg' % i, '') for i in range(1, 5)] + [(MI + 'design_fence.jpg', 'Flags and fence')],
     'Flags, fences and gates designed flat in one green family, with the Arabic and English messages paired on every piece.'),
    ('Place and render', 'Photoshop, Magnific Spaces', [(SFH + 'SF_HD_Flags.jpg', 'Placement'), (SFH + 'SF_Final_Flags.jpg', 'Final render')],
     'The artwork placed on the site photo, then re-lit in Magnific so light, shadow and fabric read as one photograph.')],
 'alqaryah-booth': _booth('QR', '_0_hallplan.jpg', 'Hall plan',
    ['The layout drawn first on paper, then checked against the hall plan and the stand size.',
     'Platform, walls and the hanging header blocked out in Blender to true size.',
     'Lounge chairs, grill counter, bar, kiosk and plants placed to test seating and flow.',
     'Brand red, graphics and lighting added, then rendered in Cycles for approval.']),
 'alojour-booth': _booth('AJ', '_0_siteplan.jpg', 'Site plan',
    ['An L-shaped stand sketched over the two plots, with the corner kept for a landmark tower.',
     'Walls, arches and the 4 m tower blocked out in Blender to the real plot dimensions.',
     'Reception, majlis, hospitality bar, cafe tables and the hanging rings placed.',
     'Travertine, walnut, brass and warm 3000K light, rendered in Cycles for approval.'],
    second=('_int_1_outline.jpg', 'Interior')),
}

TOOLKIT = [('Ideas and concept', 'Pen and paper, Claude, ChatGPT', 'A rough sketch first, then the brief analysed and the idea, copy direction and prompts built.'),
           ('Image', 'Magnific, Photoshop', 'Scenes generated in Magnific Spaces with Nano Banana Pro, upscaled, then retouched and composited in Photoshop.'),
           ('3D and video', 'Blender, Higgsfield, Flow', 'Exhibition booths modelled and rendered in Blender; key frames turned into motion.'),
           ('Design and delivery', 'Adobe Creative Cloud', 'Illustrator, InDesign, Photoshop, After Effects and Premiere Pro for identity, layout, motion and final files.')]

PROCESS = [('Sketch', 'Pen and paper', 'Every project starts as a rough sketch: the composition and the message before any tool.'),
           ('Reference', 'Magnific Spaces', 'Location, light, people and cultural detail gathered as one board.'),
           ('Generate or model', 'Magnific, Nano Banana Pro, Blender', 'Scenes directed side by side on one canvas; booths built in Blender from outline to placed models.'),
           ('Refine', 'Photoshop, Higgsfield, Flow', 'Upscaling, retouching and compositing, then key frames turned into motion.'),
           ('Design and render', 'Adobe Creative Cloud, Blender', 'Typography, layout and final renders for every format and screen.')]

# the method strip on the home page: one booth, sketch to render
FLOW = ('alojour-booth', [(BT + 'AJ_0_sketch.jpg', 'Sketch'), (BT + 'AJ_1_outline.jpg', 'Outline'), (BT + 'AJ_2_models.jpg', 'Models'), (BT + 'AJ_3_render.jpg', 'Render')])

# ======================================================================== v5: more MODON events, Saudi Energy storyboards, extra social
for p in PROJECTS:  # the multi-story factory carousel now lives in its own campaign below
    if p['slug'] == 'industry-carousels':
        p.update(title='Food industries carousel', sub='Growth figures, slide by slide.',
                 summary='A swipeable carousel on the growth of Saudi food and pharma industries, told one figure per slide.',
                 facts=[('Client', 'MODON'), ('Role', 'Design'), ('Format', '5-slide carousel')],
                 images=[r for r in p['images'] if 'MultiStory' not in r])

MS, IC, RS, AG, S5, S4, SH, LN, SX = ('28_Multistory_Factories/', '25_Industry_Champions/', '26_Riyadh_Season/', '27_Annual_Gathering_2025/',
                                      '29_Saudifood_2025/', '30_Saudifood_2024/', '23_SE_Hajj_1447/', '24_SE_Lenel/', '31_Social_Extra/')
NEW_CAMPAIGNS = [
 dict(slug='multi-story-factories', cat='campaigns', title='78 factories, one building', sub='Multi-story factories in Dammam.', client='MODON', feat=True,
      summary='The launch campaign for MODON’s first multi-story factory building in Dammam’s 1st Industrial City: 78 units over 8 floors, told through big numbers, an infographic, screen ads, a press release and the media plan.',
      facts=[('Client', 'MODON'), ('Role', 'Campaign identity and design'), ('Scope', 'Posters, infographic, screens, press release, media plan')],
      hero=MS + 'MS_06.jpg', cover=MS + 'MS_01.jpg',
      images=jpg(MS, 'MS_01', 'MS_03', 'MS_04', 'MS_07', 'MS_08', 'MS_05', 'MS_09', 'MS_10', 'MS_11', 'MS_12')),
 dict(slug='industry-champions', cat='campaigns', title='Industry Champions', sub='A sports tournament for the industry system.', client='MODON, Ministry of Industry',
      summary='The identity and print suite for MODON’s fifth sports tournament, played in Ramadan by teams from across the industry and mining system: tournament badges, the poster, investor invitations, roll-ups, wall banners, a pop-up wall and the tournament deck.',
      facts=[('Client', 'MODON, Ministry of Industry'), ('Role', 'Identity and design'), ('Scope', 'Badges, poster, invitations, roll-ups, banners, deck')],
      hero=IC + 'IC_Deck_Cover.jpg', cover=IC + 'IC_Poster.jpg',
      images=jpg(IC, 'IC_Poster', 'IC_Invitation', 'IC_Rollup_Padel', 'IC_Wall_Banner', 'IC_Popup', 'IC_Deck_Pitch')),
 dict(slug='riyadh-season-2025', cat='campaigns', title='MODON at Riyadh Season', sub='Four spaces in Boulevard World.', client='MODON',
      summary='The campaign for MODON’s participation in Riyadh Season 2025: screens, stories and posts inviting visitors to four interactive spaces in Boulevard World, from a kids’ factory to a VIP ticket.',
      facts=[('Client', 'MODON'), ('Role', 'Campaign design'), ('Scope', 'Screens, stories, social posts')],
      hero=RS + 'RS_Voice_Of_Industry.jpg', cover=RS + 'RS_Explore.jpg',
      images=jpg(RS, 'RS_Explore', 'RS_Spaces_Map', 'RS_VIP_Ticket', 'RS_Join_Us')),
 dict(slug='annual-gathering-2025', cat='campaigns', title='MODON Annual Gathering 2025', sub='One night, one identity.', client='MODON',
      summary='The identity for MODON’s annual staff gathering: a 2025 mark in four colourways, a facet pattern drawn from the MODON skyline, invitations and a boxed invitation, announcements for email and screens, a Diwaniya theme and thank-you cards for employees’ families.',
      facts=[('Client', 'MODON'), ('Role', 'Event identity and design'), ('Scope', 'Logo, pattern, invitations, screens, cards')],
      hero=AG + 'AG_Identity_Cover.jpg', cover=AG + 'AG_Logo_Options.jpg',
      images=jpg(AG, 'AG_Logo_Options', 'AG_Identity_System', 'AG_Invitation_Mockup_Closed', 'AG_Invitation_Mockup_Open', 'AG_Invitation_Minister',
                 'AG_Announcement', 'AG_Diwaniya', 'AG_Family_Card')),
 dict(slug='saudifood-2025', cat='campaigns', title='Saudifood 2025', sub='Two events, two themes.', client='MODON',
      summary='MODON’s presence at two food-industry events in 2025. Saudi Food Manufacturing, in deep navy, under “A new era in food manufacturing”, with invitations, the agenda, hall banners and pillar branding; and The Saudifood Show in green, with the general invitation, the opening agenda and the conference programme proposal.',
      facts=[('Client', 'MODON'), ('Role', 'Event themes and design'), ('Scope', 'Invitations, agendas, hall branding, proposal deck')],
      hero=S5 + 'SFM_Banner_Wide.jpg', cover=S5 + 'SFM_Connected_Communities.jpg',
      images=jpg(S5, 'SFM_Invitation_VIP', 'SFM_Agenda', 'SFM_Connected_Communities', 'SFM_Operational_Efficiency', 'SFM_Hall_Freestanding',
                 'SFS25_Invitation', 'SFS25_Agenda', 'SFS25_Conference_Proposal')),
 dict(slug='saudifood-2024', cat='campaigns', title='Saudifood 2024', sub='Empowering the food industry.', client='MODON',
      summary='The show logo and MODON’s event suite for The Saudifood Show 2024: invitations, the opening-ceremony agenda, an infographic on MODON’s support for food manufacturers, screens, pillar branding and the stage design.',
      facts=[('Client', 'MODON'), ('Role', 'Logo, event theme and design'), ('Scope', 'Logo, invitations, agenda, infographic, screens, stage')],
      hero=S4 + 'SF24_Logo.jpg', cover=S4 + 'SF24_36_Cities.jpg',
      images=jpg(S4, 'SF24_36_Cities', 'SF24_Infographic', 'SF24_Invitation', 'SF24_Agenda', 'SF24_Screen_Tall', 'SF24_Pillar', 'SF24_Stage_Model')),
]
NEW_DECKS = [
 dict(slug='se-hajj-1447', cat='presentations', title='Hajj 1447 storyboard', sub='Every scene generated with AI.', client='Saudi Energy', ai=True, feat=True,
      summary='A film storyboard for Saudi Energy’s Hajj 1447 readiness campaign: one filming day for each stage of Hajj, each with its location, timing, interview and voice-over. Every scene of the engineers among the pilgrims was generated with AI on a Magnific Spaces canvas, so the client could see the film before a camera rolled.',
      facts=[('Client', 'Saudi Energy'), ('Role', 'Storyboard, AI scenes and deck design'), ('Format', '27 slides, Arabic'), ('AI tools', 'Magnific Spaces, Nano Banana Pro')],
      hero=SH + 'SH_26.jpg', cover=SH + 'SH_05.jpg',
      images=jpg(SH, 'SH_01', 'SH_02', 'SH_04', 'SH_05', 'SH_07', 'SH_10', 'SH_14', 'SH_17', 'SH_19')),
 dict(slug='se-access-control-film', cat='presentations', title='Access control film', sub='A storyboard built with AI scenes.', client='Saudi Energy', ai=True,
      summary='A storyboard for an introductory film on Saudi Energy’s Lenel access-control system for industrial security, in three chapters, each scene with its shot and voice-over. The offices, gates, control rooms and staff were all generated with AI on a Magnific Spaces canvas.',
      facts=[('Client', 'Saudi Energy'), ('Role', 'Storyboard, AI scenes and deck design'), ('Format', '29 slides, Arabic'), ('AI tools', 'Magnific Spaces, Nano Banana Pro')],
      hero=LN + 'LN_01.jpg', cover=LN + 'LN_10.jpg',
      images=jpg(LN, 'LN_02', 'LN_04', 'LN_10', 'LN_13', 'LN_16', 'LN_21')),
]
NEW_SOCIAL = [
 dict(slug='altanfeethi-international', cat='social', title='Altanfeethi International', sub='Now at London Heathrow.', client='Altanfeethi',
      summary='Launch posts for Altanfeethi International, the chauffeur service’s meet-and-greet at selected airports abroad, starting with London Heathrow.',
      facts=[('Client', 'Altanfeethi'), ('Role', 'Design'), ('Scope', 'Launch posts')],
      hero=None, cover=SX + 'AT_Intl_Arrival.jpg', images=jpg(SX, 'AT_Intl_Arrival', 'AT_Intl_London')),
 dict(slug='industrial-center-founding-day', cat='social', title='Founding Day', sub='From our ancestors’ heritage to today’s industry.', client='Industrial Center',
      summary='A Founding Day post for the Industrial Center that moves from the heritage of Diriyah to the centre’s modern building in one warm, sandstone palette.',
      facts=[('Client', 'Industrial Center'), ('Role', 'Design'), ('Scope', 'Social post')],
      hero=None, cover=SX + 'IC_Founding_Day.jpg', images=jpg(SX, 'IC_Founding_Day')),
]
def _insert_after(slug, items):
    i = next(k for k, p in enumerate(PROJECTS) if p['slug'] == slug) + 1
    PROJECTS[i:i] = items
_insert_after('campaign-key-visuals', NEW_CAMPAIGNS)
_i = next(k for k, p in enumerate(PROJECTS) if p['cat'] == 'presentations'); PROJECTS[_i:_i] = NEW_DECKS
_insert_after('altanfeethi-social', NEW_SOCIAL)

# one image per repeated design, and no greetings that carry a person's name
def _set(slug, **kw):
    next(p for p in PROJECTS if p['slug'] == slug).update(kw)
_set('ruqi', images=['05_Ruqi/RQ_Logo.png'] + jpg('05_Ruqi/', 'RQ_Poster_Main', 'RQ_Poster_Ideas', 'RQ_Poster_Objectives'))
_set('dour-dourak', images=jpg('07_Dour_Dourak/', 'DD_Logo', 'DD_Close_to_You', 'DD_Your_Space', 'DD_Change_01', 'DD_Phase2_A', 'DD_Screen_Goals'))
_set('ramadan-1447', cover='04_Ramadan_1447/RM_Greeting_Employees_01.jpg',
     summary='A seasonal theme for MODON: a hand-lettered wordmark, a blue-to-green light gradient and one layout system, applied to greetings for staff and investors and a download card.',
     images=jpg('04_Ramadan_1447/', 'RM_Greeting_Employees_01', 'RM_Greeting_Investors', 'RM_Greeting_Link_Ad') + ['04_Ramadan_1447/RM_Wordmark_Calligraphy.png'])
_set('eid-al-fitr-1447', cover='10_Eid_Al-Fitr_1447/EF_Identity_02.jpg',
     summary='A seasonal theme for MODON: a hand-lettered Eid wordmark holding the Saudi coffee pot, glossy 3D festive objects and a soft blue-to-green wash.',
     facts=[('Client', 'MODON, Ministry of Industry'), ('Role', 'Theme and design'), ('Scope', 'Wordmark, identity, 3D objects')],
     images=jpg('10_Eid_Al-Fitr_1447/', 'EF_Identity_02', 'EF_Identity_03'))
_set('eid-al-adha-1447', images=jpg('11_Eid_Al-Adha_1447/', 'EA_Identity_02', 'EA_Identity_03', 'EA_Identity_07', 'EA_Cards_Download_Ad', 'EA_Email_Work_Hours', 'EA_Greeting_Investors'))

BTS['SH'] = dict(img='20_AI_Process/SE_Hajj_Spaces_Canvas.jpg', window='Magnific Spaces — Saudi Energy, Hajj 1447', title='Sixteen scenes, one canvas',
                 steps=[('Brand reference', 'The Saudi Energy logo set as a fixed reference, so every uniform carries the right mark.'),
                        ('Generate by moment', 'One Image Generator node per filming moment: arrival, Arafah, Muzdalifah, Mina, day and night.'),
                        ('Select for the storyboard', 'The strongest frame of each moment placed on its slide with the interview and voice-over.')])
_set('se-hajj-1447', bts='SH')

# ======================================================================== v6: no deck slides, mockups, design-to-reality projects
CATS = [('campaigns', 'Campaigns & events'), ('booths', 'Booths & spaces'), ('presentations', 'Presentations'),
        ('social', 'Social media'), ('earlier', 'Earlier work')]
PROJECTS[:] = [p for p in PROJECTS if p['slug'] not in ('annual-gathering-2025', 'saudifood-2024', 'bonded-zone')]
_set('multi-story-factories', images=jpg(MS, 'MS_01', 'MS_03', 'MS_04', 'MS_07', 'MS_08', 'MS_05', 'MS_09'),
     facts=[('Client', 'MODON'), ('Role', 'Campaign identity and design'), ('Scope', 'Posters, infographic, screens, press release')])
_set('industry-champions', hero=IC + 'IC_Rollups_Mockup.jpg', images=jpg(IC, 'IC_Poster', 'IC_Wall_Banner', 'IC_Popup'),
     summary='The identity and print suite for MODON’s fifth sports tournament, played in Ramadan by teams from across the industry and mining system: tournament badges, the poster, roll-ups, wall banners and a pop-up wall.',
     facts=[('Client', 'MODON, Ministry of Industry'), ('Role', 'Identity and design'), ('Scope', 'Badges, poster, roll-ups, banners, pop-up wall')])
_set('se-hajj-1447', title='Hajj 1447 storyboard', sub='Fourteen scenes, generated in about four hours.', hero=SH + 'SH_Deck_Mockup.jpg', cover=SH + 'AI/SH_AI_02.jpg',
     summary='A film storyboard for Saudi Energy’s Hajj 1447 readiness campaign. Instead of stock photos or a reference shoot, every scene of the engineers among the pilgrims was generated with AI on one Magnific Spaces canvas: fourteen scenes in about four hours, so the client could see the film before a camera rolled. Shown here: the deck and the AI scenes it used.',
     facts=[('Client', 'Saudi Energy'), ('Role', 'Storyboard, AI scenes and deck design'), ('AI scenes', '14, in about 4 hours'), ('AI tools', 'Magnific Spaces, Nano Banana Pro')],
     images=['23_SE_Hajj_1447/AI/SH_AI_%02d.jpg' % i for i in range(1, 13)])
_set('se-access-control-film', sub='Twenty-two scenes, generated in about 75 minutes.', hero=LN + 'LN_Deck_Mockup.jpg', cover=LN + 'AI/LN_AI_01.jpg',
     summary='A storyboard for an introductory film on Saudi Energy’s Lenel access-control system for industrial security. The offices, gates, control rooms and staff were all generated with AI: twenty-two scenes in about 75 minutes. Shown here: the deck and the AI scenes it used.',
     facts=[('Client', 'Saudi Energy'), ('Role', 'Storyboard, AI scenes and deck design'), ('AI scenes', '22, in about 75 minutes'), ('AI tools', 'Magnific Spaces, Nano Banana Pro')],
     images=['24_SE_Lenel/AI/LN_AI_%02d.jpg' % i for i in range(1, 13)])

AG6, EP, MZ, N95 = '27_Annual_Gathering_2026/', '32_Excellence_Paths/', '33_Modon_Zone/', '34_National_Day_95/'
_insert_after('multi-story-factories', [
 dict(slug='annual-gathering', cat='campaigns', title='MODON Annual Gathering', sub='The Ashra identity.', client='MODON',
      summary='The identity for MODON’s annual staff gathering: a stacked year mark, a hand-lettered “Ashra” slogan, a navy-to-lime palette and a pattern drawn from Sadu weaving, carried onto a branded entrance arch for the venue.',
      facts=[('Client', 'MODON'), ('Role', 'Event identity and design'), ('Scope', 'Logo, slogan, palette, pattern, entrance arch')],
      hero=AG6 + 'AG26_Arch_Render_01.jpg', cover=AG6 + 'AG26_Arch_Render_02.jpg',
      images=jpg(AG6, 'AG26_Logo', 'AG26_Slogan', 'AG26_Colors', 'AG26_Pattern', 'AG26_Arch_Render_02')),
])
_insert_after('alqaryah-booth', [
 dict(slug='excellence-paths-wall', cat='booths', title='Industrial Excellence Paths', sub='From design to the venue wall.', client='MODON',
      summary='An exhibition wall for an industrial excellence event: seven paths to the top, from people and the industrial revolution to sustainability and women in industry, set in a backlit hexagon strip. Designed flat, then built and lit on site.',
      facts=[('Client', 'MODON'), ('Role', 'Wall design and content layout'), ('Scope', 'Exhibition wall, backlit strip')],
      hero=EP + 'EP_Wall_Design.jpg', cover=EP + 'EP_Wall_Photo.jpg', images=jpg(EP, 'EP_Wall_Photo')),
 dict(slug='modon-zone', cat='booths', title='MODON Zone', sub='Four booths, one zone.', client='MODON',
      summary='A MODON zone of four 2 × 2 m booths for partner companies: a 5 m frame with MODON branding on top and each company’s booth below. Rendered with real dimensions for approval, then built in the exhibition hall.',
      facts=[('Client', 'MODON'), ('Role', 'Zone design, 3D render, branding'), ('Scope', 'Four booths, frame branding')],
      hero=MZ + 'MZ_Booths_Render.jpg', cover=MZ + 'MZ_Booths_Photo.jpg', images=jpg(MZ, 'MZ_Booths_Photo')),
])
_insert_after('modon-announcements', [
 dict(slug='national-day-95', cat='social', title='National Day 95', sub='Glory, made in Saudi.', client='MODON',
      summary='National Day 95 stories for MODON under the year’s theme: Saudi-made industry, from robotic lines to a drill bit stamped “Saudi made”, set against the national Sadu tree.',
      facts=[('Client', 'MODON'), ('Role', 'Design'), ('Scope', 'Stories')],
      hero=None, cover=N95 + 'ND95_Drill_Bit.jpg', images=jpg(N95, 'ND95_Drill_Bit', 'ND95_Robotics')),
])
STEPS['excellence-paths-wall'] = [('Design', 'Illustrator, Photoshop', [(EP + 'EP_Wall_Design.jpg', 'Design')], 'The wall drawn flat: seven paths, copy and photography on one hexagon strip.'),
                                  ('On site', 'Built and lit', [(EP + 'EP_Wall_Photo.jpg', 'Built')], 'Printed, built and backlit at the venue.')]
STEPS['modon-zone'] = [('Render', 'Blender', [(MZ + 'MZ_Booths_Render.jpg', '3D render')], 'Four booths rendered with real dimensions for approval.'),
                       ('On site', 'Built in the hall', [(MZ + 'MZ_Booths_Photo.jpg', 'Built')], 'The zone built in the exhibition hall, ready for the partners.')]

STEPS_NOTE = {'excellence-paths-wall': 'From the design file to the wall on site.', 'modon-zone': 'From the 3D render to the booths on site.'}
_set('excellence-paths-wall', images=[])
_set('modon-zone', images=[])

# ======================================================================== v7
PROJECTS[:] = [p for p in PROJECTS if p['slug'] not in ('annual-gathering', 'saudifood-2025')]
_set('industry-champions', images=jpg(IC, 'IC_Poster'),
     summary='The identity for MODON’s fifth sports tournament, played in Ramadan by teams from across the industry and mining system: tournament badges, the poster and roll-ups.',
     facts=[('Client', 'MODON, Ministry of Industry'), ('Role', 'Identity and design'), ('Scope', 'Badges, poster, roll-ups')])
# series with many designs: the colour variants and template adaptations were made in Photoshop
for p in PROJECTS:
    if len(p['images']) >= 6 and p['cat'] != 'booths' and not any(k in ('Tools', 'AI tools') and 'Photoshop' in v for k, v in p['facts']):
        p['facts'] = p['facts'] + [('Tools', 'Photoshop for colour variants and template adaptations')]
