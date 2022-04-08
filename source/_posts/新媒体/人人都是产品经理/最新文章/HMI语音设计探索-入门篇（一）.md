
---
title: 'HMI语音设计探索-入门篇（一）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/04/qKGgbL9LD3ATzR8oHM10.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 08 Apr 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/04/qKGgbL9LD3ATzR8oHM10.jpg'
---

<div>   
<blockquote><p>编辑导语：语音交互是未来的一大趋势，HMI语音设计也有其背后的逻辑。这篇文章以介绍语音交互内容为基础，并结合作者的实际工作项目经验，提出了一些想法和思路，一起看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-783566 aligncenter" src="https://image.yunyingpai.com/wp/2022/04/qKGgbL9LD3ATzR8oHM10.jpg" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<p>开头必须来一句，我相信语音一定是未来，我非常确认。</p>
<p>这篇HMI的语言探索以介绍语音交互内容为基础，结合我的实际工作项目经验，输出总结关于语音设计的内容，最后在结合案例，在对话设计中会进行深度的探索，并提出个人的想法和思路，因为有的时候深度去思考觉得我们项目还可以有很多优化的点。</p>
<p>进入我们今天的正题：</p>
<p>在说语音交互之前，先给大家讲一下题外话，关于人机交互（Human Computer Interaction）简称HCI，可能日后我想去攻读这个硕士学位，简单来说就是指人与计算机之间通过使用某种对话语言，以一定的交互方式，为完成确定任务的人与计算机之间的信息交换过程。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/Cm5D3X1q9H1ddfhkmB0x.png" alt width="700" height="437" referrerpolicy="no-referrer"></p>
<p>语音助手最初的载体是手机APP，通过与用户之间的对话方式，能够帮助用户来解决问题的，随着我们现在人工智能的研发技术不断发展，包括让机器学习，语音识别、图像识别、自然语言处理、智能搜索等一系列。</p>
<p>语音交互运用的很普遍了，不仅仅只是智能手机，现在涉及到的领域是越来越多了，如智能家居、汽车、可穿戴设备、就连商场普遍也有机器人语音对话。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/2AukVPHZAxQmpcfqG5Y4.png" alt width="654" height="368" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、HMI语音介绍</h2>
<p>我这边就不打算讲语音的发展历史了，不然又是水了一大堆内容，我可是一个讲干货的小作家呢，如果我的小粉丝们需要的话，就私信我，我会在微信公众号更文。</p>
<p>语言是传递信息重要方式，对于我们用户来说，语音交互也是学习成本相对较低、容易掌握的，语音交互设计简称为 VUI。</p>
<p>新能源汽车不断的发展，智能车载系统也是我们最看重的。随着语音交互的的普及，语音识别开始走入人们生活，凭借其实用性和准确性得到了用户的认可，因此在发展的过程中摒弃了传统的、繁杂的手动操作，提高安全驾驶属性和更高效的处理问题的能力，但是，在现阶段的新能源汽车发展过程中还不能完全替换掉手动操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/JYsyhMDT6szKxEB5bkLo.png" alt width="723" height="407" referrerpolicy="no-referrer"></p>
<p>现在为什么用户在驾驶车的过程中，还是不会常用到语音交互，首先提到的就是用户习惯，根据数据调查，在使用语音交互的人群中，年轻人占了主力军，其余年龄段的人由于常年驾驶都是通过硬按键来操控车内空调、电话、音乐、电台、内置导航。</p>
<p>其实就算是苹果手机中的siri都很少用到， 在使用初期因为技术的不成熟，再加上冰冷的对话方式使得用户不对他这个买单，像我现在生活中，用到的siri频率也会很少，最多就是定一个闹钟，app实在找不到就会使用到，还有无聊的时候和他进行无聊的对话，嗯就这样子。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/LmJt8zLNo6IDX6qVnZqE.png" alt width="670" height="377" referrerpolicy="no-referrer"></p>
<p>国内做语音头部公司有我们熟悉的科大讯飞，还有和多家车企合作的思必驰、云知声，对内服务的百度，搜狗，腾讯，阿里这些大咖都有自己的语音技术。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/1t2UGzqvWfggi0Yd9SXe.png" alt width="747" height="374" referrerpolicy="no-referrer"></p>
<p>再讲一下语音的基础原理内容，这一块比较难懂一点，首先你要说出你需要解决的需求、要处理什么事情，通过车载系统设备收到指令的语音、自动语音识别 (ASR)、将指令转化为文本、自然语言处理 (NLP)、了解用户需要解决什么问题、通过Skill（普及一下知识：SKill 是一个脚本语言 运行在cadence的设计环境，是cadence设计工具的API，好了不啰嗦了），将处理好的结果处理成回复文本，最后再通过TTS 播报形式，形成回复音频，通过车载系统回复给用户解决结果，听起来是不是有点复杂了，我相信我是全网说的最细的了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/Zq5EPhPzflcRmvGGE3U2.png" alt width="627" height="353" referrerpolicy="no-referrer"></p>
<p>如何去定义一个产品的语音的好坏？我觉得吧，能够让用户对于这个语音系统的满意度达到一个高标准，首先能够让系统能够听懂你所说的内容，并且给出相对应的解决方案，语音系统运用的简而易用即可，如何做到以上的要求，我会再下面对话设计中会着重讲解深挖的。</p>
<p>如何去定义一个产品的语音的好坏？我觉得吧，能够让用户对于这个语音系统的满意度达到一个高标准，首先能够让系统能够听懂你所说的内容，并且给出相对应的解决方案，语音系统运用的简而易用即可，如何做到以上的要求，我会再下面对话设计中会着重讲解深挖的。</p>
<h2 id="toc-3">三、车载语音交互（VUI）基本原则</h2>
<p><strong>车载场景下的语音交互核心基本原则有三点：</strong></p>
<h3>1. 首先是安全</h3>
<p>驾驶过程中，司机的眼睛、耳朵和手占据了大部分多任务操作，如果一些功能还需要通过眼睛和手来操作的话，会降低安全驾驶的系数，所以车载语音交互更有助于辅佐司机安全驾驶，减少注意力的分散。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/hdRBG32FFGeGqyUjL66l.png" alt width="660" height="337" referrerpolicy="no-referrer"></p>
<h3>2. 其次是便利</h3>
<p>语音交互设计之初，一定要考虑便利、快捷，尽量的减少每一个任务的对话次数、快速响应、将对话流程简单化，从而打破VUI对于用户的一个心理障碍（便利这块内容我会在后面对话设计中着重讲解）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/EDSUvXCCBtBjWC7aJaQj.png" alt width="709" height="418" referrerpolicy="no-referrer"></p>
<h3>3. 最后是愉悦</h3>
<p>为什么要谈到愉悦，因为市场上最初的语音对话交谈，都是冷冰冰的，几乎没有情感可谈，像极了和机器人对话，并且有的时候无法处理任务就会说，超出能力范围，这是一个很不好的用户体验。</p>
<p>现在市场上可以看到，导航软件也有语音包可以选择，这也是增加了情感化设计，这是其中的一个点。还有一个小点就是自然的对话交流，很流畅的完成用户提出的每一项任务，尽可能的规避对话中的错误，让整体的对话过程达到一个愉悦的感觉。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/lTKa6orwvNjSAGIo483n.png" alt width="652" height="353" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、用户语音的目的</h2>
<p>用户在语音交互的时候，绝大多数都是带有明确指示任务指令的，也有可能是闲聊状态。</p>
<p><strong><span style="font-family: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', STHeiti, 'WenQuanYi Micro Hei', Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal;">任务状态下</span>：</strong><span style="font-size: 16px;">任务式对话中，用户需要尽快的得到想要反馈和解决方案，并且快速的完成，此类任务的反馈要求还需要清晰、简单明了。</span></p>
<p><strong>闲聊状态下：</strong>我们经常也会问Siri一些无聊的问题，比如：“siri给我来一段Rap” 通常这类的任务带有的目的性不是很强，但是对于趣味性要求会高。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/9l0fM1FHFqObvgw1Urfz.png" alt width="594" height="334" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、市场现状（VUI+GUI）</h2>
<p>语音是最舒服的交互形式，但是他不能完全取代GUI，相互协作才是更佳的方案，所以现在市场上的车载系统大多数都是以语音（VUI）和 图形用户界面（GUI）相组合的，也有少部分车加入其他交互方式譬如手势交互。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/Iw3zmJDn4BsGTXvHKfiu.png" alt width="576" height="324" referrerpolicy="no-referrer"></p>
<p>语音与图形的交互是交叉处理，从而形成了多模，多模态在我第二篇文章也有讲到，第一次看我文章的同学们可以回顾一下，用户在对车载系统发送一个指令的同时，设备会有多种的反馈方式，首先你可以听到系统虚拟形象给你做出回答，其次你看到图形界面的变化，举一个例子，你说：“我要听周杰伦的七里香”系统就会处理讲页面跳转到音乐界面，并且播放周杰伦的七里香，如果声音小了，你可以说：“声音大一点”</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/Yh2JoHsFnFKRfvB0dMTa.png" alt width="677" height="353" referrerpolicy="no-referrer"></p>
<p>大家是不是发现一个问题呀？我在前面说系统首先会做出回答，然后界面才会发生变化，但是实际情况，系统语音形象没有做出任何多余的回答，而是直接听取到用户的需求，直接反馈出结果，播放了周杰伦的 #七里香#，这就是我准备在下面会重点讲到的“对话设计”。</p>
<p>再说对话设计之前，我们先了解一下VUI设计师，想必大家头一次听说，还有语音（VUI）设计师嘛，国内不太注重培养VUI设计师，大家可以去招聘平台搜索一下语音交互设计师，很少有公司专门针对这个职位去招聘的，就算有，也是招聘算法等研发岗的职位，VUI设计师的工作任务一般都是公司的产品经理或者交互设计师代劳了，这会肯定就有产品经理或者交互设计师想出来吐槽了，哈哈哈。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/Zbt33GvlWnIOtGJLwOpD.png" alt width="689" height="488" referrerpolicy="no-referrer"></p>
<p>语音交互方式给用户听和说两个动作，相信大家也有听过7±2法则，因此在听到的信息设计发面需要考量，因为用户听到一遍内容之后就消失了，除非这款车机语音系统，有再次复述上一段话的功能，不然在语音设计的时候，千万不要让用户产生的认知负荷，更不要挑战用户的短时间的记忆力，最强大脑除外，我们大多数人可不是什么最强大脑是不是。</p>
<p>再次强调一下，就算拥有复述这个功能，也要注意设计的语音内容，该功能点只是加分项而已，不能打破底线，将语音设计的原则抛之脑后。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/04/7CklvcyvTp3XZ617eQZf.png" alt width="504" height="367" referrerpolicy="no-referrer"></p>
<p>文章中如有不足之处，欢迎补充交流，我们下期见。</p>
<p>下期文章预告：HMI语音设计探索-实际案例篇（二）</p>
<p> </p>
<p>本文由@设计界的影帝 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议吗</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5382629" data-author="1144194" data-avatar="http://image.woshipm.com/wp-files/2021/02/7ff0E7qRVbu3wtH8GNE0.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            