
---
title: '网易伏羲GDC分享：伏魔AI游戏外挂防控系统在网易游戏的实践经验'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/27/113209y60q1pbw02wg11cb.jpg'
author: GameRes 游资网
comments: false
date: Tue, 27 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/27/113209y60q1pbw02wg11cb.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2506744">
在游戏开发者大会（GDC2021）上，来自网易伏羲的陶建容（花名风天）分享了伏羲伏魔AI游戏外挂防控系统在网易游戏的实践经验。<br>
<br>
网易伏羲实验室在人工智能领域积极探索，推出了游戏行业人工智能解决方案，横跨AI反外挂、AI竞技机器人、AI 对战匹配以及 AI 剧情动画制作四大AI能力，实现了AI 技术在游戏行业的新突破。本次分享的内容是源于AI反外挂在游戏中的运用经验。<br>
<br>
伏羲AI反外挂技术和传统反外挂技术有什么区别，具体效果如何，来自网易伏羲游戏AI技术负责人的风天老师，为我们带来了非常详细的解读。<br>
<br>
<div align="center">
<img id="aimg_995662" aid="995662" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113209y60q1pbw02wg11cb.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113209y60q1pbw02wg11cb.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113209y60q1pbw02wg11cb.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">全球游戏开发者大会（Game Developers Conference）</font></font></div><br>
记者：风天老师，您好，今年的全球游戏开发者大会（GDC），网易伏羲公开了五场游戏AI技术相关的演讲，请您先简单介绍下您演讲的这部分内容？<br>
<br>
风天：你好，今年是我第二次在GDC发表游戏AI技术相关的演讲，这一次的主题是“FUMO Engine: Applying AI to Defeat Cheating in NetEase Games”，主要分享伏羲伏魔AI游戏外挂防控系统在网易游戏的实践经验。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_995663" aid="995663" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113210c45cm4cua99jk7hc.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113210c45cm4cua99jk7hc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113210c45cm4cua99jk7hc.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">伏羲伏魔AI游戏外挂防控系统</font></font></div><br>
我们从2016年开始研究用人工智能技术应对游戏外挂问题，那时的《倩女幽魂》端游人气火爆，吸引了不少游戏脚本工作室的目光，不少工作室账号通过脚本外挂自动刷号、打金、牟利，对游戏经济系统产生了一定的危害，伏羲伏魔AI反外挂系统上线后，帮助游戏运营识别出了大量外挂脚本账号，成功打击了脚本工作室的气焰，挽回了游戏的损失。经过5年的积累，伏羲现在已经形成了8大核心AI反外挂方案，在网易10多款游戏20多个场景中落地了50多个成功案例，同时也在学术圈和行业内产生了一定的影响力。近期，我们也为全球大热的武侠吃鸡游戏《永劫无间》提供了AI反外挂技术支持，帮助游戏应对透视挂、加速挂、瞬移挂、自瞄挂等难题，支撑游戏运营一起为游戏的公平性和可玩性保驾护航。<br>
<br>
记者：伏羲AI反外挂技术和传统反外挂技术有什么区别？您能举例说明吗？<br>
<br>
风天：我们首创提出了基于玩家游戏内行为数据的AI反外挂方案，直白的讲，就是采集游戏玩家在游戏中的行为数据，让AI去挖掘Bot和Human之间的差别。下面我举了一个简单的案例，我们把《天谕》端游玩家的游戏行为序列进行了可视化，图中不同颜色的色条对应玩家在游戏中的不同行为，如进出地图、释放技能等，从图中我们可以非常直观的看到Bot和Human之间的差别，Bot之间有着非常高的行为相似性，而Human除了和Bot有较大差异之外，不同Human之间的行为也表现出了行为的多样性。<br>
<br>
<div align="center">
<img id="aimg_995664" aid="995664" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113212h9y18k8k1z6q4kg8.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113212h9y18k8k1z6q4kg8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113212h9y18k8k1z6q4kg8.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">游戏玩家行为序列可视化对比图（Bot vs Human）</font></font></div><br>
基于这样的数据观察，我们采用表征学习算法将玩家行为序列表征成定长向量，再采用基于密度的聚类方法，就可以挖掘出在Human群体周边一簇一簇的Bot群体，下面是把玩家表征向量降维到3维空间进行可视化的结果。<br>
<br>
<div align="center">
<img id="aimg_995665" aid="995665" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113214vi0utmi87oic19uc.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113214vi0utmi87oic19uc.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113214vi0utmi87oic19uc.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">游戏玩家3维空间聚类可视化图（Bot vs Human）</font></font></div><br>
Bot和Human除了游戏行为序列表现出差异性之外，在移动轨迹、鼠标轨迹、触控轨迹、键盘序列、关系图谱、聊天文本、渲染图片、录制视频等数据上都可以基于AI挖掘出显著的差别，下面展示了《逆水寒》端游中移动轨迹、《天谕》手游中触控轨迹，Bot和Human均表现出了较为明显的差异。<br>
<br>
<div align="center">
<img id="aimg_995666" aid="995666" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113214eerr6mupdg1u8rm6.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113214eerr6mupdg1u8rm6.jpg" width="422" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113214eerr6mupdg1u8rm6.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_995667" aid="995667" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113215tszc4jslfza93lcr.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113215tszc4jslfza93lcr.jpg" width="436" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113215tszc4jslfza93lcr.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">游戏玩家移动轨迹、触控轨迹可视化对比图（Bot vs Human）</font></font></div><br>
和传统反外挂方案相比，AI反外挂具有以下几项优势：<br>
<br>
1.数据不敏感。一些传统反外挂方案需要采集玩家硬件设备信息、进程信息甚至侵入游戏核心代码，而AI反外挂利用的数据均为游戏内行为数据，均为驱动游戏运行的必要非敏感数据，不会对玩家隐私带来任何风险。<br>
<br>
2.学习能力强。只要有充足的数据和标记，通过监督学习的方法就可以很好的学习出Bot和Human之间的区别，保持较高的准确率和召回率，即使没有标记数据，也可以通过无监督学习的方法找到群体性的Bot。<br>
<br>
3.对抗变异强。外挂可以直接修改硬件设备信息，比如IP、序列号等，也可以直接屏蔽进程相关信息，但是只要使用了外挂，它在游戏中的行为表现往往是无法隐藏的，总会表现出一定的行为一致性、重复性和不可达性。<br>
<br>
记者：您能简单介绍下“伏魔AI反外挂系统”背后是如何运转的吗？<br>
<br>
风天：伏魔AI反外挂系统建构起了多层次、多应用、广覆盖的游戏反外挂产品体系，通过底层伏魔引擎和上层伏魔平台的支撑，实现了不同游戏数据源和AI 能力的全面整合，满足了不同品类游戏在不同场景下的外挂对抗需求。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_995668" aid="995668" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113216zddbbq5fid9yqfia.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113216zddbbq5fid9yqfia.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113216zddbbq5fid9yqfia.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">网易伏羲伏魔AI反外挂系统</font></font></div><br>
伏魔系统在工程实践和算法研究中都始终践行着网易“创新”的核心价值观。伏魔引擎设计并实现了BDSDK，全面兼容游戏多终端多类型数据的采集、加密、压缩、传输与存储，并将核心的反外挂算法集成到BDLib，涵盖画像、序列、图像、图谱、轨迹、视频、聊天、语音等多数据类型各类AI算法，同时推出标准化服务接入框架BDFlow，实现规则、监督、无监督、迭代闭环，助力开发团队降本增效。伏魔平台则搭建起了从算法服务到业务输出的桥梁，通过整合数据可视化、分析工具、证据链、预警等平台化功能，使AI反外挂结果能更好地呈现给用户并满足多样化的反外挂业务需求。<br>
<br>
记者：AI尤其深度学习基本都是黑盒模型，反外挂又是一个非常注重解释性和证据性的场景，您是如何应对这个问题的呢？<br>
<br>
风天：这是一个非常好的问题。用户并不只想知道“谁是外挂”，更重要的是“为什么是”—— 增强处罚信心、“拿出证据”—— 应对玩家投诉。<br>
<br>
我们的AI反外挂模型大多数都是基于深度学习算法开发的，游戏客户也会经常询问“为什么模型判断他是外挂？”，为了解决这个问题，我们成功的把可解释性AI引入到我们的AI反外挂系统中，为每一个AI模型提供解释器，比如解释画像模型每一个维度画像的重要性、解释行为模型关键的行为片段、解释图像模型关键的像素区域、解释图谱模型核心的网络子结构等。这个工作还发表在了2020年IEEE游戏大会（CoG）上，并且获得了大会的最佳论文奖。<br>
<br>
<div align="center">
<img id="aimg_995669" aid="995669" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113216ydlg6db9eerq46lp.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113216ydlg6db9eerq46lp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113216ydlg6db9eerq46lp.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">可解释AI在伏魔AI反外挂系统中的应用</font></font></div><br>
<div align="center">
<img id="aimg_995670" aid="995670" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113216kj7tbftfm211jqp8.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113216kj7tbftfm211jqp8.jpg" width="344" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113216kj7tbftfm211jqp8.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">CoG2020最佳论文奖</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_995671" aid="995671" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113217mpoypepmnzqqbhm8.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113217mpoypepmnzqqbhm8.jpg" width="521" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113217mpoypepmnzqqbhm8.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">伏魔平台</font></font></div><br>
2020年起，围绕“拿出证据”，我们推出了伏魔平台，整合了AI、大数据的相关技术能力，标准化后对外输出了一系列反外挂工具组件。通过个体档案、群体档案、证据链、行为分析工具、轨迹分析工具、图像分析工具、图谱分析工具等，可以直观地验证检出异常玩家，并得出法理性证据，提高游戏、运营对检出结果的信任度，高效应对玩家投诉。<br>
<br>
<div align="center">
<img id="aimg_995672" aid="995672" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113217gftx813o9j3xsgo8.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113217gftx813o9j3xsgo8.jpg" width="416" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113217gftx813o9j3xsgo8.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_995673" aid="995673" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113218e0ccf44oprpcnfu4.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113218e0ccf44oprpcnfu4.jpg" width="433" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113218e0ccf44oprpcnfu4.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_995674" aid="995674" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113218svrrjtxhv6gzhtbf.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113218svrrjtxhv6gzhtbf.jpg" width="419" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113218svrrjtxhv6gzhtbf.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_995675" aid="995675" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113218k6k6l75l6tl7tzp5.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113218k6k6l75l6tl7tzp5.jpg" width="418" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113218k6k6l75l6tl7tzp5.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">伏魔平台部分页面展示</font></font></div><br>
记者：前面介绍了非常多技术干货，那么AI反外挂流程又是怎样的呢？<br>
<br>
风天：我们的AI反外挂流程大致是“接入-预防-检测-干预-反馈-迭代”。通过反外挂SDK和伏魔引擎，最快三天即可完成反外挂服务接入。接入后，伏魔平台对游戏内经济系统、核心指标以及游戏外舆情进行异常监控，提前预警，防止外挂大规模爆发。基于8大检测方案，为游戏提供强大的AI外挂检测服务支持。“精细化治理”是我们倡导的外挂治理方式，结合游戏 DAU、游戏经济系统健康度、外挂群体规模、外挂获利、正常玩家感知度等多角度信息，对检出外挂账号做分级多方案处罚，从而最大程度上保证游戏的健康运营与营收。伏魔平台的个体档案、群体档案、一键处罚、一键标记、证据链、分析工具等功能也为快速应对举报、收集客户反馈提供了基础。最后是迭代环节，除了例行的模型自动迭代之外，我们还会持续监控线上服务效果、收集用户效果反馈，定期开展服务效果优化，提升我们反外挂服务的整体质量。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_995676" aid="995676" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113218pz7eeaqjhutl5e7b.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113218pz7eeaqjhutl5e7b.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113218pz7eeaqjhutl5e7b.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">网易伏羲伏魔AI游戏外挂对抗流程</font></font></div><br>
记者：基于AI技术的游戏反外挂效果又如何呢？<br>
<br>
风天：在网易游戏内部应用上，我们服务了包含《逆水寒》、《新倩女幽 魂》、《倩女幽魂手游》、《天谕》、《天谕手游》、《永劫无间》、《战意》、《超激斗梦境》等在内的近20款游戏，累计检测调用量达23亿次，检出外挂4亿次，平均精度超过90%，大大提升了运营方案外挂召回量级，并成功消灭多款游戏外挂，捣毁多家打金工作室，为游戏挽回千万级别损失。并成功面向游戏市场实现商业化，首年便与国内外知名MMORPG、FPS、SLG等达成反外挂商业合作，吸引了来自众多合作厂商（华为云、阿里云、AWS、Unity等）的目光，并建立起合作伙伴关系，共同面向市场树立AI防治外挂的服务标杆，输出网易特色的创新价值，赋能游戏安全领域的变革与发展。<br>
<br>
<div align="center">
<img id="aimg_995677" aid="995677" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113219eyutto7udyy3td73.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113219eyutto7udyy3td73.jpg" width="419" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113219eyutto7udyy3td73.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">网易伏羲伏魔</font></font></div><font size="2"><font color="#808080"><br>
</font></font><br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_995678" aid="995678" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113219odnvvv7v1i1rcarx.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113219odnvvv7v1i1rcarx.jpg" width="437" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113219odnvvv7v1i1rcarx.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">2021网易反外挂白皮书</font></font></div><br>
记者：网易易盾同样作为国内知名的游戏反外挂服务提供商，和网易伏羲有着哪些相同点和不同点？<br>
<br>
风天：网易伏羲和网易易盾一直保持着非常紧密的合作，都致力于与游戏外挂开展技术对抗，双方在技术维度上相辅相成，先后联合推出了“手游模拟点击检测联合解决方案”以及“FPS游戏外挂对抗联合解决方案”。近期伏羲和易盾还将联合制定并发布“2021网易反外挂白皮书”，敬请期待。<br>
<br>
<div align="center">
<img id="aimg_995679" aid="995679" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113219y64y5424f46yd5fn.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113219y64y5424f46yd5fn.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113219y64y5424f46yd5fn.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">网易易盾、网易伏羲游戏反外挂系统主要应用范围</font></font></div><br>
记者：您能透露一些伏羲AI反外挂产品的后续规划吗？<br>
<br>
风天：我们将持续打磨我们的AI反外挂技术和产品，为更多国内游戏客户提供反外挂服务，并进一步开拓海外游戏市场，拓宽产品的覆盖面，致力于成为游戏反外挂领域的标杆品牌。同时，我们也会不断拓展技术外沿，将异常检测的核心技术，从游戏反外挂推向电商反作弊、金融反欺诈、工业反瑕疵等领域，推动技术创新为更多领域赋能。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img id="aimg_995680" aid="995680" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113220f5g5uv68nc48uxju.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113220f5g5uv68nc48uxju.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113220f5g5uv68nc48uxju.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">伏魔8个核心异常检测技术方案</font></font></div><br>
记者：面向游戏行业，除了前面介绍的AI外挂防控系统，伏羲还对外开放了哪些AI能力呢？<br>
<br>
风天：伏羲正在开展游戏AI和虚拟人的商业化工作，不久前在上海举行的世界人工智能大会，伏羲携AI竞技机器人、AI剧情动画制作以及AI对战匹配系统参会，与AI外挂防控系统共同组成了网易伏羲游戏AI解决方案，这几项AI技术都将在今年的全球游戏开发者大会上公开亮相。我们致力于解决游戏行业的痛点问题，遏制外挂作弊、打金工作室等现象的不断蔓延，同时从“帮助游戏降本增效、丰富游戏玩家体验、完善游戏匹配机制、营造精彩对战”入手，借助AI技术的优势来驱动游戏行业实现变革。<br>
<br>
<div align="center">
<img id="aimg_995681" aid="995681" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113220fjrrb17g14k4xg3q.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113220fjrrb17g14k4xg3q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113220fjrrb17g14k4xg3q.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">网易伏羲AI解决方案，助力产业升级</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img id="aimg_995682" aid="995682" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113220bm558pf5d5lxqmic.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113220bm558pf5d5lxqmic.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113220bm558pf5d5lxqmic.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">网易伏羲2021GDC公开演讲大满贯</font></font></div><br>
记者：谢谢风天老师，您还有其它什么内容想和大家分享的吗？<br>
<br>
风天：欢迎大家加入网易伏羲，一起用人工智能点亮游戏未来！<br>
<br>
网易伏羲官网 http://fuxi.163.com<br>
<br>
<div align="center">
<img id="aimg_995683" aid="995683" zoomfile="https://di.gameres.com/attachment/forum/202107/27/113526w1cr7dxak4rxdn5k.jpg" data-original="https://di.gameres.com/attachment/forum/202107/27/113526w1cr7dxak4rxdn5k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/27/113526w1cr7dxak4rxdn5k.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">主讲人介绍：</font></strong><br>
<br>
陶建容（花名风天，网易伏羲游戏AI技术负责人），浙江大学计算机博士，毕业后加入网易并参与组建伏羲游戏人工智能实验室，负责游戏用户画像方向前沿研究与技术转化工作，主要研究“面向游戏用户的智能画像服务系统与平台”，致力于解决游戏中外挂检测、战场匹配、智能推荐、预测归因等重点难题，在数据挖掘、人工智能、游戏等领域发表近40篇论文（KDD、AAAI、IJCAI、ACM MM、TKDE、TOIS、ToG等），获得Ubicomp2016、CoG2020、SMDS2020最佳论文奖，担任ACM信息与知识管理会议（2019）、ACM数据挖掘与知识发现会议（2019）、IEEE数据挖掘会议（2020-2021）程序委员会委员，担任ACM杭州分会执行委员会委员。申请30多项发明专利和10多项软件著作，相关研究成果在网易多款游戏中投入应用（《逆水寒》、《倩女幽魂》、《天谕》、《永劫无间》等）。目前负责网易伏羲游戏AI商业化工作，面向游戏行业推出涵盖研发、运营、营销全链路的人工智能解决方案（游戏竞技机器人、游戏外挂防控、游戏智能匹配推荐、游戏虚拟形象等），致力于用伏羲AI赋能游戏行业降本增效，全面释放创作者的生产力，革新玩家游戏体验。<br>
<br>
</td></tr></tbody></table>



  
</div>
            