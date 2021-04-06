
---
title: '专为物联网而生的TinyML，正在开启音频分析的新蓝海'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210406/v2_9e5c648230084a298635057ae9853e97_img_000'
author: 36kr
comments: false
date: Tue, 06 Apr 2021 03:21:05 GMT
thumbnail: 'https://img.36krcdn.com/20210406/v2_9e5c648230084a298635057ae9853e97_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/cQ-WNy6u4jR7h8Xdq90nCg">“物联网智库”（ID:iot101）</a>，作者：彭昭（物联网智库创始人&云和资本合伙人），36氪经授权发布。</p> 
<p>在3月22到26日，TinyML基金会举办了2021 TinyML峰会，这是有史以来的第三届。</p> 
<p>虽然本届峰会在云端举办，但同样声势浩大，而且无论是影响力还是参会者都可谓上了一个新台阶。诸多国际一线企业、业内独角兽初创公司和知名院校<a class="project-link" data-id="3969140" data-name="云集" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969140" target="_blank">云集</a>线上。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,930" src="https://img.36krcdn.com/20210406/v2_9e5c648230084a298635057ae9853e97_img_000" referrerpolicy="no-referrer"></p> 
<p>其中的代表性公司包括：ARM、高通、脸书、微软、三星、Greenwaves、SensiML、Silicon Labs、Syntiant、Qeexo、普林斯顿大学、密歇根大学、埃里克斯霍尔姆大学、麻省理工学院、斯坦福大学等。 </p> 
<p>在此前的文章中，我曾介绍过微型机器学习TinyML，也就是在终端和边缘侧的微处理器上实现的机器学习过程。更准确的说，TinyML是指工程师们在mW功率范围以下的设备上，实现机器学习的方法、工具和技术。</p> 
<p>TinyML微型机器学习是机器学习和物联网设备的交集，它是一门新兴的工程学科，有可能在许多行业引发革命。</p> 
<p>在这次峰会上，大家分享了TinyML的最新进展以及各种应用实例，值得关注的趋势包括：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>用户对于隐私的关注推动了TinyML的发展</p></li> 
 <li><p>TinyML有可能将开启音频识别的新蓝海</p></li> 
 <li><p>最新发布的TinyML产品和工具</p></li> 
</ul> 
<h2 label="一级标题"><strong>01 保护隐私成为TinyML发展的推动力</strong></h2> 
<p>消费者对于隐私问题的担忧，成为TinyML发展的推动力，很多公司为了响应消费者需求，正在开发功耗更低、响应速度更快、隐私保护更佳的设备。 </p> 
<p>人工智能与设备的结合，经历了三个发展阶段：</p> 
<h3 label="二级标题"><strong>第1阶段--云端能</strong></h3> 
<p class="image-wrapper"><img data-img-size-val="957,286" src="https://img.36krcdn.com/20210406/v2_231f85178775440aa3e03f921e7a2159_img_000" referrerpolicy="no-referrer"></p> 
<p>在人工智能发展的初期，机器学习模型是在云端训练和托管的。运行AI所需的强大计算能力使云成为理想的选择。</p> 
<p>开发人员和数据科学家利用高端CPU和GPU训练模型，然后托管它们以进行推理。每个消耗AI的应用程序都与云对话。该应用程序将与微控制器通信以管理传感器和执行器。</p> 
<h3 label="二级标题"><strong>第二阶段--边缘智能</strong></h3> 
<p class="image-wrapper"><img data-img-size-val="958,324" src="https://img.36krcdn.com/20210406/v2_8e9cb9ad31094c11b9ac90e31b2cf4c2_img_000" referrerpolicy="no-referrer"></p> 
<p>随着物联网的发展，越来越多的遍布于工业自动化、智能医疗、智能联网汽车中的场景，都要求人工智能模型能在本地运行。边缘侧成为在本地托管人工智能模型的理想选择。边缘智能可以有效避免云中运行相同AI所带来的延迟。</p> 
<p>但是鉴于边缘资源有限，AI模型的训练仍然需要云。这种方法提供了两全其美的优势，既有用于训练的云端强大计算环境，又能兼顾用于推理的低延迟边缘托管环境。但是由于与云端进行协作，边缘智能仍旧无法解决消费者对于隐私性的担忧。</p> 
<h3 label="二级标题"><strong>阶段3--微型人工智能</strong></h3> 
<p class="image-wrapper"><img data-img-size-val="960,825" src="https://img.36krcdn.com/20210406/v2_e7b240b679de443cada16c402d6dd24b_img_000" referrerpolicy="no-referrer"></p> 
<p>分布最广的物联网设备往往体积很小、电量有限。它们被作为终端硬件，通过嵌入式传感器采集各种数据；计算能力有限，对功耗极为敏感。某些情况下，将这类设备连接到边缘侧以便实现智能，在成本上并不划算， </p> 
<p>直接在微处理器中嵌入人工智能，成为消费和工业物联网场景的关键。这种方法并不依赖于外部程序，也不依赖边缘和云端。这种方案能够提供最佳的实时响应，同时对隐私提供极大保护。</p> 
<p>TinyML峰会上提供的微型机器学习的例子包括，智能家居场景中，带有传感器洗衣机和冰箱可以在电机损坏之前主动发送信号。洗衣机可以根据衣服的重量，精准的调节水位。</p> 
<p>具备TinyML的可穿戴设备，可以脱离云端持续监测用户的睡眠水平、心率体征等健康数据。TinyML胰岛素泵可以在不必时刻保持网络连接的情况下，根据血糖水平自动释放胰岛素。这些不必时刻联网的设备，让数据处于私有状态，更加安全并保护隐私。</p> 
<h2 label="一级标题"><strong>02 TinyML开启音频分析的新蓝海</strong></h2> 
<p class="image-wrapper"><img data-img-size-val="1080,551" src="https://img.36krcdn.com/20210406/v2_772a6d8918054324a696774a38372cae_img_000" referrerpolicy="no-referrer"></p> 
<p>过去我们极大的发展了机器视觉，现在我们正在赋予机器听觉。 </p> 
<p>和视觉信息一样，声音无处不在。语音启动的设备，在智能家居的应用中非常常见，最典型的比如智能音箱。 </p> 
<p>还有很多声音，比如机床震动的声音、车辆抛锚的声音、报警器鸣响的声音…这些声音不同于语音，没有语言模型。</p> 
<p>目前越来越多的物联网企业正在将分析的重点从视频转移到音频。比如在家居场景中，亚马逊推出了Guard这项在智能音箱中的功能，用来识别窗户破碎的声音并报警。在工业场景中，预测性维护已经取得了长足的发展，很多企业监测设备的振动和声音，用来主动发现故障，为客户节省数百万元的维护成本。</p> 
<p>在TinyML峰会中，一家名为Audio Analytic的公司分享了关于音频分析的最新进展，并且认为TinyML即将开启音频分析的新蓝海。</p> 
<p>他们已经建立了包含700种不同声音的配置文件，可以检测到从火车进站到婴儿啼哭，常见的和不常见的各种声音。</p> 
<p>借助TinyML，Audio Analytic公司展示了基于ARM Cortex-M0+处理器检测声音的方案。应用场景包括墙壁上安装的小型传感器，可以检测玻璃破碎的声音；降噪耳机通过识别疾驰而来的汽车的声音，主动关闭降噪功能，以便让佩戴者及时作出反应。</p> 
<p>根据峰会中的分析，声音检测可能在4个场景取得大发展：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>第一个是安全场景：比如根据玻璃破碎或者烟雾报警器的声音，通知更多人员。</p></li> 
 <li><p>第二个是个人健康：比如检测婴儿的哭声、打鼾的声音，并且及时提醒。根据烹饪时发出的声音，自动调节房间的空气质量。</p></li> 
 <li><p>第三个是家庭娱乐：比如根据外部环境和回声，根据房间大小，自动调整娱乐系统的音效。</p></li> 
 <li><p>第四个是工业应用：比如根据风力发电机振动的声音，检测叶片的裂纹并给予预警。</p></li> 
</ul> 
<h2 label="一级标题"><strong>03 TinyML产品与工具陆续发布</strong></h2> 
<p>Nordic Semiconductor在其nRF52和nRF53系列低功耗蓝牙芯片中引入了TinyML，并且提供相应的开发套件，成为业界首个支持人工智能技术的蓝牙产品。</p> 
<p class="image-wrapper"><img data-img-size-val="639,313" src="https://img.36krcdn.com/20210406/v2_895e02b6abd24909b9ecf5dd3860ddb9_img_000" referrerpolicy="no-referrer"></p> 
<p>Nordic将这些支持TinyML技术的蓝牙SoC应用于濒临灭绝的动物保护，野生大象佩戴了Nordic提供的蓝牙追踪项圈，帮助护林员防止非法狩猎盗取象牙的事件发生，取得了很好的效果。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,429" src="https://img.36krcdn.com/20210406/v2_e4b5b5675d1b4404a9021dcabdf05b84_img_000" referrerpolicy="no-referrer"></p> 
<p>SensiML联手Silicon Labs，为开发者快<a class="project-link" data-id="31748" data-name="速研" data-logo="https://img.36krcdn.com/20200729/v2_52143d51b986423997aac69f2d53da1e_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/31748" target="_blank">速研</a>发支持TinyML的智能传感应用程序提供便利。</p> 
<p>使用Silicon Labs提供的Thunderboard Sense 2物联网开发入门套件，配合使用SensiML提供的Analytics Toolkit AI/ ML开发软件，开发者能够快速创建运行于物联网终端设备的智能方案。 </p> 
<p>这些方案将特别适用于低功耗和能源敏感型应用，包括能源、<a class="project-link" data-id="464601" data-name="水表" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/464601" target="_blank">水表</a>和燃气表、楼宇自动化、警报及安防，和便携式医疗/健身器材。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,607" src="https://img.36krcdn.com/20210406/v2_54b8978fb4234e02b961d9c77cd89bab_img_000" referrerpolicy="no-referrer"></p> 
<p>在峰会上，Raspberry Pi联合创始人Eben Upton公布了“Pi Silicon”的未来路线，其内部专用集成电路ASIC团队正在进行下一次迭代，并且正专注于研发针对超低功耗机器学习TinyML应用程序的轻量级加速器。</p> 
<p>同期，Eben Upton发布了三款“Pi Silicon”树莓派板，分别为SparkFun MicroMod RP2040、Arduino Nano RP2040 Connect和ArduCam Pico4ML。三款产品会将机器学习、摄像头、麦克风和屏幕集成到Pico软件包中。 </p> 
<p>尤其是售价仅为4美元的Pico4ML，提供对于TinyML的支持。比如在上图展示的样例中，Pico4ML可以同时检测到两张人脸，一个真人以及一个超级马里奥，Pico4ML以百分比值做出判断，在提供实时图像的同时，显示图像是真人的概率。 </p> 
<p><strong>写在最后</strong></p> 
<p>划个重点。</p> 
<p>第一，TinyML将为数以亿计的物联网终端设备带来“生命”，它将引发的变革不容小觑。</p> 
<p>第二，消费者对于隐私问题的担忧，成为TinyML发展的推动力，很多公司为了响应消费者需求，正在开发功耗更低、响应速度更快、隐私保护更佳的设备。</p> 
<p>第三，目前越来越多的物联网企业正在将分析的重点从视频转移到音频，TinyML可能即将开启音频分析的新蓝海。</p>  
</div>
            