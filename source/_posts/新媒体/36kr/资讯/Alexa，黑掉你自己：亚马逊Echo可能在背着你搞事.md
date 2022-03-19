
---
title: 'Alexa，黑掉你自己：亚马逊Echo可能在背着你搞事'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220319/v2_0e4b362b05114815b423584938ef8723_img_000'
author: 36kr
comments: false
date: Sat, 19 Mar 2022 04:00:51 GMT
thumbnail: 'https://img.36krcdn.com/20220319/v2_0e4b362b05114815b423584938ef8723_img_000'
---

<div>   
<p>文｜杜晨</p> 
<p>编辑｜VickyXiao</p> 
<p>像亚马逊 Echo Dot、Google Home Mini 这样的小型智能音箱，价格非常便宜，功能也非常强大。调查显示，疫情之前这两个智能音箱系列的渗透率在美国达到了35%的家庭，预计在2025年将会达到75%</p> 
<p>不过，几位来自英国和意大利的安全研究者最近发现，亚马逊的 Echo 智能音箱存在一个相当棘手的社会工程学漏洞。</p> 
<p><strong>这个漏洞能够让攻击者激活并劫持音箱，背着用户进行各种操作。影响方面，除了侵犯了用户隐私之外，还可能导致更加严重的财产损失，甚至人身伤害的风险。</strong></p> 
<p><strong>离谱的是，这个漏洞并不需要什么复杂的黑客代码，只靠 Echo 音箱自己就可以实现</strong>——简单来说，Echo 音箱通过音乐和电台技能 (skill)，如果播放了某段特定的音频，而音频当中包含了某个特定的触发词/指令，漏洞就被触发了。</p> 
<p>研究者将这个漏洞命名为 Alexa versus Alexa (简称 AvA)——顾名思义，就是 Alexa（亚马逊的虚拟语音助理）自己黑掉自己……</p> 
<h3><strong>体验越好，漏洞越大</strong></h3> 
<p>为了让智能音箱和语音助理产品被更多人使用，厂商们都在研究如何进一步提升体验。然而，很多设计初衷是为了提升体验的功能，都给用户添了麻烦，甚至还有可能成为本文所讨论的安全漏洞。</p> 
<p>包括 Siri、Google Assistant (GA)，Alexa 在内的虚拟语音助手，都会保持麦克风开启，因为它们需要监听 "Hey Siri", "Ok Google", "Hey Alexa" 等唤醒口令。然而因为识别并不是完全准确的，这些虚拟语音助手经常会被误触发——苹果手机用户过去经常遭遇此类情况。</p> 
<p>研究者发现，除了识别不准之外，Echo 音箱还有另一个问题：它对自己发出的声音的干扰排除能力不是很好。简而言之，如果我们让 Echo 去播放一段音频，而这段音频当中正好包含了能够控制 Echo 去做其他事情的命令——结果，Echo 就会给自己发号施令。</p> 
<p>经过测试，被这种方式劫持的 Echo 所能做的包括并不限于<strong>：播放音频文件或在线电台、监听房间内的对话、调整闹钟、修改用户日历项、给任意号码打电话、操控智能家庭设备，甚至用主人的亚马逊账号在网上乱买东西等……</strong></p> 
<p>让我们来更详细地看一下这个漏洞的攻击方式：</p> 
<p><strong>1）首先，黑客制作一段听起来完全没有问题的音频文件，</strong>比如一首歌，或者一个 podcast，并且在音频文件中加入能够激活 Alexa/Echo 并且让其执行特定操作的命令；</p> 
<p><strong>2）黑客有两种攻击角度可选：</strong>在距离攻击对象家的足够距离内，用手机蓝<a class="project-link" data-id="320891" data-name="牙链" data-logo="https://img.36krcdn.com/20210810/v2_1f8c404b14af45d1b87ad07e4b92deee_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/320891" target="_blank">牙链</a>接 Echo 音箱，然后播放音频（下图中的1.2），也可以直接把音频做成在线电台，通过社工学的方式让攻击对象 Echo 播放（下图中的1.1）；</p> 
<p class="image-wrapper"><img data-img-size-val="850,393" src="https://img.36krcdn.com/20220319/v2_0e4b362b05114815b423584938ef8723_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">漏洞攻击方式</p> 
<p>注意：Echo 无需安装额外应用就具备播放在线电台的技能 (Skill) ，这些技能是在云端运行的（如上图右侧所示）。并且，任何人都可以自己开发类似的技能，发布到亚马逊的 Alexa 技能商店里。虽然亚马逊会对首次发布的技能进行安全核查，但开发者仍然可以在后续更新中加入恶意代码，并且不会被亚马逊发现。</p> 
<p><strong>3）Echo 播放了可疑的音频文件，接受了音频中的指令，</strong>就能够在用户不知情的前提下进行各种操作，给用户添麻烦，比如修改甚至取消闹钟，让人睡过头；开关智能灯泡，让人以为家里闹鬼；修改日历项，让人错过重要事情等等；</p> 
<p>不要以为这些都是无害的小玩笑，这个漏洞完全可能导致更严重的隐私泄露、财产损失和人身危险。</p> 
<p>举三个场景为例：</p> 
<p>1. 隐私泄露：黑客可以在可疑的音乐文件里加入 "go on“。这个词组也对应了 Echo 音箱支持的一个技能，可以极大延长 Echo 保持激活的时间，监听用户说话的时间；进而，黑客还可以将用户讲话内容发送到网络服务器。在最极端的情况下，黑客完全有能力结合 go on 和其它技能来完全劫持 Echo 音箱，把用户发布的命令替换成自己的……</p> 
<p>2. 财产损失：过去我们偶尔会看到这样的新闻：有人收到了亚马逊的包裹，但是自己并没有买过里面的东西——通过本文所探讨的这个漏洞，黑客是完全可以劫持 Echo 去乱买东西的。</p> 
<p>这是因为通常 Echo 只会在购买后首次配置时验证用户的身份和账户信息，后续无论是安装技能还是网上下单，都无需做额外的身份校验——这些设计原本是为了让使用体验更流畅，现在可能被漏洞利用。</p> 
<p>3. 人身伤害和财产严重损失：如果用户家里装了兼容 Alexa 的智能门锁的话，坏人可以在门口蓝牙连上音箱，播放指令，打开门锁——这可就成了严重的入室抢劫风险了……</p> 
<p>此次漏洞被命名为 CVE-2022-25809：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,825" src="https://img.36krcdn.com/20220319/v2_ffd64ed76b35496b96a806d956fba481_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc"> CVE-2022-25809</p> 
<p>研究的结果也已经写成了论文，放在 arXiv 上。</p> 
<h3><strong>受影响产品和严重程度</strong></h3> 
<p>令人担忧的是，如果结合前面提到的在线电台（远程）和蓝牙连接（现场）这两种攻击角度的话，这一漏洞的凶险程度是非常高的：</p> 
<p><strong>可以在全世界任何地点对目标实现远程侵入，</strong></p> 
<p><strong>可以一次性劫持多个 Echo 设备，</strong></p> 
<p><strong>可以不采用社工学方法发起攻击，</strong></p> 
<p><strong>可以在断线之后重新发起攻击，</strong></p> 
<p><strong>甚至可以在首次攻击完成并建立连接后进行遮掩，从而实现长期入侵，将其变成“肉鸡”等等……</strong></p> 
<p class="image-wrapper"><img data-img-size-val="543,117" src="https://img.36krcdn.com/20220319/v2_046e73d6df4e4b65b04daec7c3030297_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Attack Vectors</p> 
<p><strong>研究人员已经将这次的主要漏洞 AvA，以及顺道发现的另外两个小漏洞 Full Volume 和 Break Tag Chain 的 资料直接提交给了亚马逊。</strong></p> 
<p>Full Volume 漏洞可以增大音箱播放内容的音量，从而提高受影响的 Echo 设备以及同房屋内的其它联网 Echo 设备被劫持的几率；</p> 
<p>Break Tag Chain 能够在用户不知情的前提下延长特定技能持续运行的时间，对黑客进一步完善社工学攻击场景起到帮助。</p> 
<p>漏洞的验证和复现工作是在第三代 Echo Dot 上进行的，不过研究人员指出：三代和四代的所有 Echo 智能音箱产品都存在此漏洞。</p> 
<p><strong>亚马逊将漏洞严重性评为”中级“，并且也在最近对受影响的 Echo 产品发布了补丁更新（版本号：3代6812454788，4代 6409855108）。</strong></p> 
<p>这次补丁在一定程度上降低 Echo 设备被自己所播放内容当中的触发词激活的几率，然而它并没有完全补上漏洞。因为正如我们在前面所提到的：这个漏洞并非由代码缺陷，而是由功能设计所导致的。</p> 
<p>原则上，只要 Echo 音箱还是麦克风<a class="project-link" data-id="38841" data-name="全时" data-logo="https://img.36krcdn.com/20210520/v2_41f8d68c1867416cbe41adf1444c69b0_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/38841" target="_blank">全时</a>开启监听触发词，只要技能 (skill) 的发布、审核和调用机制保持现状，只要 Echo 为了确保使用体验而不在特定操作的时候进行用户身份验证——这个漏洞就将继续存在。</p> 
<p>研究人员指出，想要对抗这一漏洞，有几种思路可以参考：</p> 
<p>1）压制智能音箱被自己播放的内容触发的能力：这一点上，Echo 已经有了类似的机制设计，采用了多麦克风阵列可以更加准确地侦测语音命令的来源方位，便于判断命令来自于用户还是自己。</p> 
<p>2）检测语音命令的声<a class="project-link" data-id="217488" data-name="波信" data-logo="https://img.36krcdn.com/20210809/v2_d0a00fa83fce43bb96b90c1ceb7fdc55_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/217488" target="_blank">波信</a>息：如果声波当中包括了人的声道发不出来的低频声波，则有很大的几率是来自自己或者另一台扬声器。</p> 
<p>3）在更多的场景里严格使用已知用户的声音：很多智能音箱在初次设置的时候，都会让用户多说几句话，这样就能听出来说话的人是谁，从而有针对性地完成操作。然而至少对于目前 Echo 音箱来说，它并不会在进行高风险操作（如支付、操控其它智能设备）的时候验证命令是否来自已知的用户。亚马逊应该在这一点上进行优化。</p> 
<p>如果正在阅读本文的你也在用 Echo 音箱产品，可以检查一下设备是否已经更新到最新版本。</p> 
<p>一般来说，我们还是可以正常使用智能音箱的，但如果你实在担心音箱被劫持的话，可以在长时间不用的时候（比如出门前）把音箱上的麦克风完全关掉，只要按下麦克风的按钮，指示灯变为红色就可以了。</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/CoNHw6liU_K1_sXmFNOzvg">“硅星人”（ID:guixingren123）</a>，作者：光谱 杜晨，36氪经授权发布。</p>  
</div>
            