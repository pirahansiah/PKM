import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def check_links(base_url):
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        
        print(f"Scanning {base_url}... Found {len(links)} links.")
        
        for link in links:
            url = link['href']
            # Resolve relative paths
            full_url = urljoin(base_url, url)
            
            # Only check internal links or specific domains to save time
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                try:
                    res = requests.head(full_url, allow_redirects=True, timeout=5)
                    if res.status_code >= 400:
                        print(f"[BROKEN] {res.status_code}: {full_url}")
                    else:
                        print(f"[OK] {res.status_code}: {full_url}")
                except Exception as e:
                    print(f"[ERROR] Could not connect to {full_url}: {e}")
    except Exception as e:
        print(f"Failed to crawl homepage: {e}")

# Run the check
check_links("https://www.pirahansiah.com/")




'''
	
	
	To see the location of the link in your HTML source click srcbelow
#	Broken link (you can scroll this field left-right)	Link Text	Page where found	Server response
1	https://github.com/pirahansiah/eot-training-multi-object-tracking
https://github.com/pirahansiah/eot-training-multi-object-tracking	eot-training-multi-object-tracking	url src	404
2	https://www.pirahansiah.com/contents/public/public/projects/Solutions/
https://www.pirahansiah.com/contents/public/public/projects/Solutions/	Impact Portfolio	url src	404
3	https://github.com/pirahansiah/obsidian
https://github.com/pirahansiah/obsidian	obsidian	url src	404
4	https://www.pirahansiah.com/contents/public/public/ai-llm/orchestrating-agents/
https://www.pirahansiah.com/contents/public/public/ai-llm/orchestrating-agents/	Orchestrating AI Agents	url src	404
5	https://www.pirahansiah.com/contents/public/public/ai-llm/advanced-llm-concepts/
https://www.pirahansiah.com/contents/public/public/ai-llm/advanced-llm-concepts/	Advanced LLM Concepts	url src	404
6	https://www.pirahansiah.com/contents/public/public/ai-llm/blog/
https://www.pirahansiah.com/contents/public/public/ai-llm/blog/	Blog: AI &amp; LLMs	url src	404
7	https://www.pirahansiah.com/contents/public/public/cuda-gpu/numba-jit/
https://www.pirahansiah.com/contents/public/public/cuda-gpu/numba-jit/	Numba JIT Tutorial	url src	404
8	https://github.com/pirahansiah/aws
https://github.com/pirahansiah/aws	aws	url src	404
9	https://www.pirahansiah.com/contents/public/public/cuda-gpu/pycuda-kernels/
https://www.pirahansiah.com/contents/public/public/cuda-gpu/pycuda-kernels/	PyCUDA Kernel Explanation	url src	404
10	https://www.pirahansiah.com/contents/public/public/cuda-gpu/vscode-cuda-windows/
https://www.pirahansiah.com/contents/public/public/cuda-gpu/vscode-cuda-windows/	CUDA in VS Code on Windows	url src	404
11	https://www.pirahansiah.com/contents/public/public/cuda-gpu/mlx-coreml-metal/
https://www.pirahansiah.com/contents/public/public/cuda-gpu/mlx-coreml-metal/	MLX<COMMA> CoreML &amp; Metal	url src	404
12	https://www.pirahansiah.com/contents/public/public/cv/3d/
https://www.pirahansiah.com/contents/public/public/cv/3d/	3D Vision &amp; Multi-Camera	url src	404
13	https://www.pirahansiah.com/contents/public/public/cv/optical-flow/
https://www.pirahansiah.com/contents/public/public/cv/optical-flow/	Optical Flow	url src	404
14	https://www.pirahansiah.com/contents/public/public/cv/multi-camera-systems/
https://www.pirahansiah.com/contents/public/public/cv/multi-camera-systems/	Real-Time Multi-Camera	url src	404
15	https://www.pirahansiah.com/contents/public/public/optimization/
https://www.pirahansiah.com/contents/public/public/optimization/	CV/DL/ML Optimization	url src	404
16	https://www.pirahansiah.com/contents/public/public/CPP/
https://www.pirahansiah.com/contents/public/public/CPP/	C++ Quick Reference	url src	404
17	https://www.pirahansiah.com/contents/public/public/Python/
https://www.pirahansiah.com/contents/public/public/Python/	Python Config &amp; Tips	url src	404
18	https://www.pirahansiah.com/contents/public/public/setup/
https://www.pirahansiah.com/contents/public/public/setup/	Developer Tools	url src	404
19	https://www.pirahansiah.com/contents/public/public/shell-vim-quickref/
https://www.pirahansiah.com/contents/public/public/shell-vim-quickref/	Shell &amp; Vim	url src	404
20	https://www.pirahansiah.com/contents/public/public/StartUp/
https://www.pirahansiah.com/contents/public/public/StartUp/	Startup Guide	url src	404
21	https://www.pirahansiah.com/contents/public/public/coaching/
https://www.pirahansiah.com/contents/public/public/coaching/	Coaching	url src	404
22	https://www.pirahansiah.com/contents/public/public/SEO/
https://www.pirahansiah.com/contents/public/public/SEO/	SEO for LLMs	url src	404
23	https://www.pirahansiah.com/contents/public/public/linkedin-top-posts/
https://www.pirahansiah.com/contents/public/public/linkedin-top-posts/	Top LinkedIn Posts	url src	404
24	https://github.com/pirahansiah/opencv-cpp
https://github.com/pirahansiah/opencv-cpp	opencv-cpp	url src	404
25	https://www.pirahansiah.com/contents/public/public/links/
https://www.pirahansiah.com/contents/public/public/links/	Curated Links	url src	404
26	https://www.pirahansiah.com/contents/public/seo/
https://www.pirahansiah.com/contents/public/seo/	Structured data<COMMA> Q&amp;A formats<COMMA> and authoritative c	url src	404
27	https://www.pirahansiah.com/contents/public/python
https://www.pirahansiah.com/contents/public/python	Python	url src	404
28	https://www.pirahansiah.com/farshid/portfolio/publications/CV
https://www.pirahansiah.com/farshid/portfolio/publications/CV	Dr. Farshid Pirahansiah CV	url src	404
29	https://www.pirahansiah.com/farshid/portfolio/publications/Patents/A_METHOD_FOR_AUGMENTING_A_PLURALITY_OF_FACE_IMAGES_WO2021060971A1
https://www.pirahansiah.com/farshid/portfolio/publications/Patents/A_METHOD_FOR_AUGMENTING_A_PLURALITY_OF_FACE_IMAGES_WO2021060971A1	My Patents: A METHOD FOR AUGMENTING A PLURALITY OF FACE	url src	404
30	https://www.pirahansiah.com/farshid/portfolio/publications/Patents/SYSTEM_AND_METHOD_FOR_PROVIDING_ADVERTISEMENT_CONTENTS_BASED_ON_FACIAL_ANALYSIS_WO2020141969A2
https://www.pirahansiah.com/farshid/portfolio/publications/Patents/SYSTEM_AND_METHOD_FOR_PROVIDING_ADVERTISEMENT_CONTENTS_BASED_ON_FACIAL_ANALYSIS_WO2020141969A2	My Patents: SYSTEM AND METHOD FOR PROVIDING ADVERTISEME	url src	404
31	https://www.pirahansiah.com/farshid/portfolio/publications/Patents/A_METHOD_FOR_DETECTING_A_MOVING_VEHICLE_WO2021107761A1
https://www.pirahansiah.com/farshid/portfolio/publications/Patents/A_METHOD_FOR_DETECTING_A_MOVING_VEHICLE_WO2021107761A1	My Patents: A METHOD FOR DETECTING A MOVING VEHICLE WO2	url src	404
32	https://www.pirahansiah.com/farshid/portfolio/publications/Books/My_Book_chapter_Camera_Calibration_and_Video_Stabilization_Framework_for_Robot_Localization
https://www.pirahansiah.com/farshid/portfolio/publications/Books/My_Book_chapter_Camera_Calibration_and_Video_Stabilization_Framework_for_Robot_Localization	My Book: My_Book_chapter_Camera_Calibration_and_Video_S	url src	404
33	https://www.pirahansiah.com/farshid/portfolio/publications/Books/Book_Computational_Intelligence_From_Theory_to_Application_explores_augmented_optical_flow_methods_for_video_stabilization
https://www.pirahansiah.com/farshid/portfolio/publications/Books/Book_Computational_Intelligence_From_Theory_to_Application_explores_augmented_optical_flow_methods_for_video_stabilization	My Book: Computational Intelligence: From Theory to App	url src	404
34	https://www.pirahansiah.com/farshid/portfolio/publications/Journals/Adaptive_Image_Thresholding_Based_on_the_Peak_Signal-to-noise_Ratio
https://www.pirahansiah.com/farshid/portfolio/publications/Journals/Adaptive_Image_Thresholding_Based_on_the_Peak_Signal-to-noise_Ratio	My Journal Publications: Adaptive Image Thresholding Ba	url src	404
35	https://www.pirahansiah.com/farshid/portfolio/publications/Journals/CHARACTER_AND_OBJECT_RECOGNITION_BASED_ON_GLOBAL_FEATURE_EXTRACTION
https://www.pirahansiah.com/farshid/portfolio/publications/Journals/CHARACTER_AND_OBJECT_RECOGNITION_BASED_ON_GLOBAL_FEATURE_EXTRACTION	My Journal Publications: CHARACTER AND OBJECT RECOGNITI	url src	404
36	https://www.pirahansiah.com/farshid/portfolio/publications/Journals/GSFT-PSNR_Global_Single_Fuzzy_Threshold
https://www.pirahansiah.com/farshid/portfolio/publications/Journals/GSFT-PSNR_Global_Single_Fuzzy_Threshold	My Journal Publications: GSFT-PSNR Global Single Fuzzy	url src	404
37	https://www.pirahansiah.com/farshid/portfolio/publications/Journals/PEAK_SIGNAL-TO-NOISE_RATIO_BASED_ON_THRESHOLD_METHOD_FOR_IMAGE_SEGMENTATION
https://www.pirahansiah.com/farshid/portfolio/publications/Journals/PEAK_SIGNAL-TO-NOISE_RATIO_BASED_ON_THRESHOLD_METHOD_FOR_IMAGE_SEGMENTATION	My Journal Publications: PEAK SIGNAL-TO-NOISE RATIO BAS	url src	404
38	https://www.pirahansiah.com/farshid/portfolio/publications/Journals/3D_SLAM_Simultaneous_Localization_And_Mapping_Trends_And_Humanoid_Robot_Linkages
https://www.pirahansiah.com/farshid/portfolio/publications/Journals/3D_SLAM_Simultaneous_Localization_And_Mapping_Trends_And_Humanoid_Robot_Linkages	My Journal Publications: 3D SLAM Simultaneous Localizat	url src	404
39	https://www.pirahansiah.com/farshid/portfolio/publications/Journals/USING_AN_ANT_COLONY_OPTIMIZATION_ALGORITHM
https://www.pirahansiah.com/farshid/portfolio/publications/Journals/USING_AN_ANT_COLONY_OPTIMIZATION_ALGORITHM	My Journal Publications: USING AN ANT COLONY OPTIMIZATI	url src	404
40	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/My_Conference_Paper_2D_versus_3D_Map_for_Environment_Movement_Objects
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/My_Conference_Paper_2D_versus_3D_Map_for_Environment_Movement_Objects	My Conference Papers: 2D versus 3D Map for Environment	url src	404
41	https://r.jina.ai/YOUR_URL
https://r.jina.ai/YOUR_URL	get markdown from url	url src	400
42	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Adaptive_Image_Segmentation_Based_on_PSNR_for_License_Plate_Recognition
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Adaptive_Image_Segmentation_Based_on_PSNR_for_License_Plate_Recognition	My Conference Papers: Adaptive Image Segmentation Based	url src	404
43	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/An_evaluation_of_classification_techniques_using_enhanced_Geometrical_Topological_Feature_Analysis
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/An_evaluation_of_classification_techniques_using_enhanced_Geometrical_Topological_Feature_Analysis	My Conference Papers: An evaluation of classification t	url src	404
44	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Camera_Calibration_for_Multi-Modal_Robot_Vision
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Camera_Calibration_for_Multi-Modal_Robot_Vision	My Conference Papers: Camera Calibration for Multi-Moda	url src	404
45	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/	My Conference Papers: Character Recognition Based on Gl	url src	404
46	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Comparison_single_thresholding_method_for_handwritten_images_segmentation
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Comparison_single_thresholding_method_for_handwritten_images_segmentation	My Conference Papers: Comparison single thresholding me	url src	404
47	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/License_Plate_Recognition_with_Multi-Threshold_Based_on_Entropy
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/License_Plate_Recognition_with_Multi-Threshold_Based_on_Entropy	My Conference Papers: License Plate Recognition with Mu	url src	404
48	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Multi-threshold_Approach_for_License_Plate_Recognition_System
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Multi-threshold_Approach_for_License_Plate_Recognition_System	My Conference Papers: Multi-threshold Approach for Lice	url src	404
49	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Pattern_Image_Significance_for_Camera_Calibration
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/Pattern_Image_Significance_for_Camera_Calibration	My Conference Papers: Pattern Image Significance for Ca	url src	404
50	https://www.pyspur.dev/blog/introduction_cuda_programming
https://www.pyspur.dev/blog/introduction_cuda_programming	CUDA python	url src	404
51	https://www.pirahansiah.com/farshid/portfolio/publications/Papers/TafreshGrid_Grid_computing_in_Tafresh_university
https://www.pirahansiah.com/farshid/portfolio/publications/Papers/TafreshGrid_Grid_computing_in_Tafresh_university	My Conference Papers: TafreshGrid Grid computing in Taf	url src	404
52	https://www.pirahansiah.com/farshid/portfolio/projects/AI_Model_Cost_Calculator.html
https://www.pirahansiah.com/farshid/portfolio/projects/AI_Model_Cost_Calculator.html	AI Model Cost Calculator: Optimizing Costs for Computer	url src	404
53	https://www.youtube.com/playlist?list=PL1ysOEBe5977vlocXuRt6KBCYu_sdu1Ru
https://www.youtube.com/playlist?list=PL1ysOEBe5977vlocXuRt6KBCYu_sdu1Ru	CUDA youtube playlist	url src	~404
54	https://www.youtube.com/@0mean1sigma/playlists
https://www.youtube.com/@0mean1sigma/playlists	mini project how to program a gpu cuda c++	url src	404
55	https://www.youtube.com/playlist?list=PL5B692fm6--vWLhYPqLcEu6RF3hXjEyJr
https://www.youtube.com/playlist?list=PL5B692fm6--vWLhYPqLcEu6RF3hXjEyJr	CUDA	url src	~404
56	https://www.youtube.com/@leadermarketer/playlists
https://www.youtube.com/@leadermarketer/playlists	farsi start up	url src	~404
57	https://www.youtube.com/@Finanzfluss/videos
https://www.youtube.com/@Finanzfluss/videos	Finanzfluss	url src	~404
58	https://github.com/e2b-dev/awesome-agents
https://github.com/e2b-dev/awesome-agents	Awesome AI Agents	url src	404
59	https://dev.intelrealsense.com/docs/high-dynamic-range-with-stereoscopic-depth-cameras
https://dev.intelrealsense.com/docs/high-dynamic-range-with-stereoscopic-depth-cameras	Intel RealSense HDR	url src	bad host
60	https://startupverband.de/ressourcen/
https://startupverband.de/ressourcen/	Ressourcen für Gründer	url src	404
61	https://www.gruenderszene.de/lexikon/begriffe/problem-solution-fit
https://www.gruenderszene.de/lexikon/begriffe/problem-solution-fit	Artikel über Problem-Solution-Fit	url src	404
62	https://www.hwr-berlin.de/forschung/forschungsprofil/entrepreneurship/
https://www.hwr-berlin.de/forschung/forschungsprofil/entrepreneurship/	Entrepreneurship-Center	url src	404
63	https://www.deutsche-startups.de/schwerpunkte/marktforschung-fuer-startups/
https://www.deutsche-startups.de/schwerpunkte/marktforschung-fuer-startups/	Marktforschung für Startups	url src	404
64	https://www.kfw.de/KfW-Konzern/KfW-Research/KfW-Gr%C3%BCndungsmonitor.html
https://www.kfw.de/KfW-Konzern/KfW-Research/KfW-Gr%C3%BCndungsmonitor.html	Studien zum deutschen Startup-Ökosystem	url src	404
65	https://www.dihk.de/de/themen-und-positionen/internationales/aussenwirtschaft/zoelle-und-handelshemmnisse
https://www.dihk.de/de/themen-und-positionen/internationales/aussenwirtschaft/zoelle-und-handelshemmnisse	Auswirkungen von Zöllen auf den Mittelstand	url src	404
66	https://startupverband.de/wissen/krisenmanagement/
https://startupverband.de/wissen/krisenmanagement/	Krisenmanagement für Startups	url src	404
67	https://www.ifw-kiel.de/de/themendossier/handelskonflikte/
https://www.ifw-kiel.de/de/themendossier/handelskonflikte/	Forschungsberichte zu Handelskonflikten	url src	404
68	https://www.kfw.de/inlandsfoerderung/Unternehmen/Gr%C3%BCnden-Nachfolgen/index.html
https://www.kfw.de/inlandsfoerderung/Unternehmen/Gr%C3%BCnden-Nachfolgen/index.html	Finanzierungslösungen in Krisenzeiten	url src	404
69	https://www.kfw-capital.de/KfW-Capital/Newsroom/
https://www.kfw-capital.de/KfW-Capital/Newsroom/	Venture Capital und KI-Finanzierung	url src	404
70	https://deutschestartups.org/themen/ki/
https://deutschestartups.org/themen/ki/	AI-Ökosystem in Deutschland	url src	404
71	https://bifold.berlin/
https://bifold.berlin/	KI-Forschung und Anwendung	url src	404
72	https://www.handelsblatt.com/unternehmen/mittelstand/gruenderszene/
https://www.handelsblatt.com/unternehmen/mittelstand/gruenderszene/	Das Gründerdilemma: Reich oder König?	url src	404
73	https://www.whu.edu/de/fakultaet-forschung/entrepreneurship/
https://www.whu.edu/de/fakultaet-forschung/entrepreneurship/	Entrepreneurship-Forschung	url src	404
74	https://www.kfw.de/KfW-Konzern/KfW-Research/KfW-Gr%C3%BCndungsmonitor.html
https://www.kfw.de/KfW-Konzern/KfW-Research/KfW-Gr%C3%BCndungsmonitor.html	Gründungsentscheidungen in Deutschland	url src	404
75	https://www.deutsche-startups.de/schwerpunkte/fuehrungswechsel-in-startups/
https://www.deutsche-startups.de/schwerpunkte/fuehrungswechsel-in-startups/	Führungswechsel in Startups	url src	404
76	https://www.eri.tum.de/eri/forschung/
https://www.eri.tum.de/eri/forschung/	Entrepreneurship Research Institute	url src	bad host
77	https://www.iao.fraunhofer.de/de/forschung/unternehmensentwicklung-und-arbeitsgestaltung.html
https://www.iao.fraunhofer.de/de/forschung/unternehmensentwicklung-und-arbeitsgestaltung.html	Studien zur Unternehmensführung	url src	404
78	https://www.kfw.de/inlandsfoerderung/Unternehmen/Gr%C3%BCnden-Nachfolgen/Finanzierungswissen/
https://www.kfw.de/inlandsfoerderung/Unternehmen/Gr%C3%BCnden-Nachfolgen/Finanzierungswissen/	Finanzierungsoptionen für Startups	url src	404
79	https://www.business-angels.de/startup-investition/
https://www.business-angels.de/startup-investition/	Angel Investing in Deutschland	url src	404
80	https://berlinvalley.com/category/funding/
https://berlinvalley.com/category/funding/	Investor-Relations für Startups	url src	bad host
81	https://www.ihk.de/themenfelder/innovation-und-umwelt/innovation/ihk-startup-initiative
https://www.ihk.de/themenfelder/innovation-und-umwelt/innovation/ihk-startup-initiative	Finanzierungsberatung	url src	404
82	https://www.bvkap.de/publikationen
https://www.bvkap.de/publikationen	Leitfäden für Investoren	url src	404
83	https://deutschestartups.org/themen/kapitalbeschaffung/
https://deutschestartups.org/themen/kapitalbeschaffung/	Deal Flow Management	url src	404
84	https://www.deutsche-boerse-venture-network.com/
https://www.deutsche-boerse-venture-network.com/	Matching-Plattform für Startups und Investoren	url src	404
85	https://berlinvalley.com/
https://berlinvalley.com/	Trends im deutschen VC-Markt	url src	bad host
86	https://www.bitkom-research.de/de/studien/ki-studie-deutschland
https://www.bitkom-research.de/de/studien/ki-studie-deutschland	KI-Studie Deutschland	url src	404
87	https://www.kfw-capital.de/KfW-Capital/Newsroom/
https://www.kfw-capital.de/KfW-Capital/Newsroom/	Venture Capital für KI-Startups	url src	404
88	https://deutschestartups.org/themen/ki/
https://deutschestartups.org/themen/ki/	KI-Ökosystem in Deutschland	url src	404
89	https://appliedai.de/resources/
https://appliedai.de/resources/	KI-Forschung und Anwendung	url src	404
90	https://bifold.berlin/news/
https://bifold.berlin/news/	KI-Forschungstrends	url src	404
91	https://www.familienunternehmen.de/de/wissen/studien
https://www.familienunternehmen.de/de/wissen/studien	Herausforderungen in Familienunternehmen	url src	404
92	https://www.hk24.de/produktmarken/beratung-service/unternehmensgruendung
https://www.hk24.de/produktmarken/beratung-service/unternehmensgruendung	Ratgeber für Familiengründer	url src	404
93	https://www.bvmw.de/themen/familienunternehmen/
https://www.bvmw.de/themen/familienunternehmen/	Konfliktmanagement in Familienunternehmen	url src	404
94	https://www.gruenderszene.de/perspektiven/gruenderpaare
https://www.gruenderszene.de/perspektiven/gruenderpaare	Erfahrungsberichte von Gründerpaaren	url src	404
95	https://www.whu.edu/fakultaet-forschung/entrepreneurship/institut-fuer-familienunternehmen/
https://www.whu.edu/fakultaet-forschung/entrepreneurship/institut-fuer-familienunternehmen/	Best Practices für Familiengründer	url src	404
96	https://www.bitkom-research.de/de/studien/ki-studie-deutschland
https://www.bitkom-research.de/de/studien/ki-studie-deutschland	KI-Anwendungen in Deutschland	url src	404
97	https://appliedai.de/resources/
https://appliedai.de/resources/	KI-Strategien für Unternehmen	url src	404
98	https://bifold.berlin/research/
https://bifold.berlin/research/	Grundlagenforschung und Anwendung	url src	404
99	https://ki-campus.org/courses
https://ki-campus.org/courses	Lernplattform für künstliche Intelligenz	url src	404
100	https://www.konsumentenpsychologie.uni-mannheim.de/forschung/
https://www.konsumentenpsychologie.uni-mannheim.de/forschung/	Forschung zur Kaufentscheidung	url src	bad host
101	https://www.bvdw.org/publikationen/
https://www.bvdw.org/publikationen/	Leitfaden für psychologisches Marketing	url src	404
102	https://www.hwr-berlin.de/studium/studiengaenge/detail/marketingmanagement/
https://www.hwr-berlin.de/studium/studiengaenge/detail/marketingmanagement/	Marketing-Psychologie Kurse	url src	404
103	https://www.nmsba.com/de
https://www.nmsba.com/de	Neuromarketing-Forschung	url src	timeout
104	https://www.kfw.de/KfW-Konzern/KfW-Research/
https://www.kfw.de/KfW-Konzern/KfW-Research/	Kennzahlen für Wachstumsunternehmen	url src	404
105	https://www.gruenderszene.de/lexikon/begriffe/saas-metriken
https://www.gruenderszene.de/lexikon/begriffe/saas-metriken	SaaS-Metriken einfach erklärt	url src	404
106	https://www.business-angels.de/startups/
https://www.business-angels.de/startups/	Investoren-Perspektive zu Startup-KPIs	url src	404
107	https://www.whu.edu/fakultaet-forschung/entrepreneurship/
https://www.whu.edu/fakultaet-forschung/entrepreneurship/	Entrepreneurship Research	url src	404
108	https://www.pwc.de/de/startups.html
https://www.pwc.de/de/startups.html	Startup-Bewertung und Kennzahlen	url src	404
109	https://berlinvalley.com/
https://berlinvalley.com/	SaaS-Metrik-Benchmarks	url src	bad host
110	https://www.kfw-capital.de/KfW-Capital/Newsroom/
https://www.kfw-capital.de/KfW-Capital/Newsroom/	Finanzierungsratgeber für Gründer	url src	404
111	https://www.business-angels.de/startup-investition/
https://www.business-angels.de/startup-investition/	Kapitalaufnahme für Startups	url src	404
112	https://deutschestartups.org/themen/kapitalbeschaffung/
https://deutschestartups.org/themen/kapitalbeschaffung/	Finanzierungsrunden planen	url src	404
113	https://www.ihk.de/themenfelder/innovation-und-umwelt/innovation/ihk-startup-initiative
https://www.ihk.de/themenfelder/innovation-und-umwelt/innovation/ihk-startup-initiative	Finanzierungsberatung für Gründer	url src	404
114	https://berlinvalley.com/category/funding/
https://berlinvalley.com/category/funding/	Bewertungstrends in der deutschen Startup-Szene	url src	bad host
115	https://www.business-angels.de/startups/
https://www.business-angels.de/startups/	Effiziente Due-Diligence-Prozesse	url src	404
116	https://berlinvalley.com/category/funding/
https://berlinvalley.com/category/funding/	Angel-Investment-Trends in Deutschland	url src	bad host
117	https://deutschestartups.org/themen/kapitalbeschaffung/
https://deutschestartups.org/themen/kapitalbeschaffung/	Investorenleitfaden	url src	404
118	https://www.whu.edu/fakultaet-forschung/entrepreneurship/
https://www.whu.edu/fakultaet-forschung/entrepreneurship/	Entrepreneurship-Forschung	url src	404
119	https://www.tum-venture-labs.de/resources/
https://www.tum-venture-labs.de/resources/	Investorenperspektiven	url src	404
120	https://www.angelinvestmentnetzwerk.de/ressourcen/
https://www.angelinvestmentnetzwerk.de/ressourcen/	Moderne Due-Diligence-Methoden	url src	bad host
121	https://www.kfw.de/KfW-Konzern/KfW-Research/
https://www.kfw.de/KfW-Konzern/KfW-Research/	Erfolgsfaktoren für Startups in Wettbewerbsmärkten	url src	404
122	https://www.gruenderszene.de/lexikon/begriffe/wettbewerbsstrategie
https://www.gruenderszene.de/lexikon/begriffe/wettbewerbsstrategie	Wettbewerbsstrategie für deutsche Startups	url src	404
123	https://deutschestartups.org/ressourcen/
https://deutschestartups.org/ressourcen/	Operational Excellence in wettbewerbsintensiven Märkten	url src	404
124	https://www.whu.edu/fakultaet-forschung/entrepreneurship/
https://www.whu.edu/fakultaet-forschung/entrepreneurship/	Forschung zu Wettbewerbsstrategien	url src	404
125	https://www.tum.de/wirtschaft/entrepreneurship/
https://www.tum.de/wirtschaft/entrepreneurship/	Wettbewerbsanalyse und Skalierung	url src	404
126	https://www.bitkom.org/Themen/Digitale-Transformation/Startups.html
https://www.bitkom.org/Themen/Digitale-Transformation/Startups.html	Digitale Tools für wettbewerbsfähige Startups	url src	404
127	https://www.kfw-capital.de/KfW-Capital/Newsroom/
https://www.kfw-capital.de/KfW-Capital/Newsroom/	Pitch Deck-Vorlagen und Tipps	url src	404
128	https://deutschestartups.org/themen/kapitalbeschaffung/
https://deutschestartups.org/themen/kapitalbeschaffung/	Pitch Deck-Bewertungskriterien	url src	404
129	https://www.unternehmertum.de/ressourcen
https://www.unternehmertum.de/ressourcen	Wissenschaftlich fundierte Präsentationstechniken	url src	404
130	https://startupverband.de/ressourcen/
https://startupverband.de/ressourcen/	Ressourcen für Gründer	url src	404
131	https://www.kfw.de/KfW-Konzern/KfW-Research/
https://www.kfw.de/KfW-Konzern/KfW-Research/	Kennzahlen für Wachstumsunternehmen	url src	404
132	https://www.ihk.de/themenfelder/innovation-und-umwelt/innovation/ihk-startup-initiative
https://www.ihk.de/themenfelder/innovation-und-umwelt/innovation/ihk-startup-initiative	Finanzierungsberatung für Gründer	url src	404
133	https://www.deutsche-boerse-venture-network.com/
https://www.deutsche-boerse-venture-network.com/	Matching-Plattform für Startups und Investoren	url src	404
134	http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8305440&isnumber=8305342
http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8305440&isnumber=8305342	PDF Download My Conference Paper	url src	418
135	http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6014009&isnumber=6013532
http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6014009&isnumber=6013532	PDF Download My Conference Paper	url src	418



'''