
---
title: '《Divinuet》的互动音乐系统 – 第 1 部分'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202103/18/152004h8cmtg6qm8118hv4.jpg'
author: GameRes 游资网
comments: false
date: Thu, 18 Mar 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202103/18/152004h8cmtg6qm8118hv4.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2489462">
早前我开发了自己的第一款游戏《inter-view》，一方面是希望由影视作曲慢慢转型做游戏作曲，另一方面是想向潜在客户证明自己通晓互动音乐创作到 Wwise 整合的这一整套工作。没想到这种互动音乐游戏做着还挺有意思，于是便决定再来开发一款，就是今天要说的《Divinuet》。<br>
<br>
《Divinuet》是一款针对 PC 和 Mac 平台开发的塔罗牌游戏，它可以依据牌面解读结果为玩家提供别具情致的音乐体验。如果你对塔罗牌不熟悉，建议参阅一下这篇文章。至于 Divinuet 这个名字，其实是我机智的朋友格韦尔 (M Gewehr) 帮忙取的，它融合了 divination （占卜）和 minuet （小步舞曲）两个词的意思。<br>
<br>
<div align="center">
<img id="aimg_966379" aid="966379" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152004h8cmtg6qm8118hv4.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152004h8cmtg6qm8118hv4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152004h8cmtg6qm8118hv4.jpg" referrerpolicy="no-referrer">
</div><br>
游戏大致分为两个环节：占卜（“the reading phase”，还可再细分为洗牌、发牌、开牌、解读）和生成（“the generative phase”，游戏依据牌面组合及顺序生成不同的音乐和画面）。在这篇博文中，我想先着重探讨一下占卜环节当中播放的音乐。主要是因为生成环节的音乐系统还有一些细节尚待完善，而且把所有内容都放在一起说的话篇幅会显得太过冗长。不过别担心，稍后我会再写一篇博文来专门介绍生成环节的音乐设计。<br>
<br>
<strong><font color="#de5650">音乐</font></strong><br>
<br>
在占卜环节，将以牌面朝下的形式发三张牌。在翻开每张牌时都会揭示牌面含义，并针对这张牌播放一小段主题音乐（长约 45 秒）。整副塔罗牌共有 78 张，所以要创作 78 段主题。<br>
<br>
<div align="center">
<img id="aimg_966398" aid="966398" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152406ugujn63s22cpu318.gif" data-original="https://di.gameres.com/attachment/forum/202103/18/152406ugujn63s22cpu318.gif" width="480" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152406ugujn63s22cpu318.gif" referrerpolicy="no-referrer">
</div><br>
可是，中间过程怎么处理呢？比方说，正在发牌或者正要翻开下一张牌。什么声音都没有的话听起来肯定会很乏味，所以有必要在牌面主题（card theme）前后插入间奏音乐（interlude）。不过在确定接下来要播放哪段牌面主题的情况下，要怎样创作间奏音乐来实现平滑的过渡呢？<br>
<br>
最简单的方法是所有牌面主题全部采用一个调，这样的话直接把间奏音乐设为同样的调就行了。但是，我并不想那么做。因为玩家十有八九会因为缺少变化而感到枯燥乏味，而且牌面所蕴含的寓意和心境也得不到充分的体现。要是非得这么创作 78+ 段乐曲，恐怕我自己都会觉得很没意思。最终，我选择了自己在创作互动音乐时常用的一种方法：将创作要用的调限制在有限的几个调之内，而这些调相互之间存在共同音。具体来说，就是把大多数牌面主题均采用 Bb 调或 Eb 调来写作（调式方面可以是大调、小调、Dorian 或者其他调式），只有极少数例外（稍后我会详细说明）。<br>
<br>
说回间奏音乐，其必须能够平滑地过渡到上述音调的牌面主题。而且，最好有别于大调和小调。因为占卜结果可能会呈现出很多不同的心境，我不希望间奏音乐和牌面主题在这方面发生冲突。为此，我选择了牌面主题最有可能用到的 4 个调（Bb 大调、Bb 小调、Eb 大调和 Eb 小调），并确定了它们的共同音（Bb、C、Eb 和 F）。然后，间奏音乐从头到尾就只用这些音符来写作。<br>
<br>
对于间奏音乐，我结合运用了纵向分层和横向分段的作曲方式。先来说说纵向分层。为此，我专门设置了 3 个分层：High、Middle 和 Low。其中 Middle 分层是段简短的一小节无限重复的 Piano 乐句（前面 2 个 Bb与F 构成的四分音符，后面 2 个 Bb与Eb 构成的四分音符）。所有间奏音乐都将围绕该分层构建。<br>
<br>
<div align="center">
<img id="aimg_966381" aid="966381" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152005f9hhun0l070ix07u.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152005f9hhun0l070ix07u.jpg" width="336" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152005f9hhun0l070ix07u.jpg" referrerpolicy="no-referrer">
</div><br>
当然，仅仅只是听这么一段乐曲肯定会感到特别无聊。所以，我们要借助 Low 和 High 分层来使间奏音乐更加富有变化。对于这种情况，需要运用横向分段作曲方式来加以实现。为此，我制作了一些简短的一小节乐句。它们全都只用 Bb、C、Eb 和 F 音符，不过分别采用了不同的乐器来演奏。这里有几个例子，我们来看一下（为简单起见，我把 Bass Clarinet 乐句设为了音乐会音高A=440Hz）。<br>
<br>
<div align="center">
<img id="aimg_966382" aid="966382" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152008qlf1fff7znel15oe.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152008qlf1fff7znel15oe.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152008qlf1fff7znel15oe.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_966383" aid="966383" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152008hzs0i0b0ztkirrrt.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152008hzs0i0b0ztkirrrt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152008hzs0i0b0ztkirrrt.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_966384" aid="966384" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152009eyeeia5kkri55nrm.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152009eyeeia5kkri55nrm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152009eyeeia5kkri55nrm.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_966385" aid="966385" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152009emi6v31x4mg2p9ti.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152009emi6v31x4mg2p9ti.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152009emi6v31x4mg2p9ti.jpg" referrerpolicy="no-referrer">
</div><br>
整段循环的长度只有一小节。对于播放的每一小节音乐，都会随机播放一段 High 和一段 Low 乐曲。在 Wwise 中看起来就像这样：<br>
<br>
<div align="center">
<img id="aimg_966386" aid="966386" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152010g89feon2ne8983za.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152010g89feon2ne8983za.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152010g89feon2ne8983za.jpg" referrerpolicy="no-referrer">
</div><br>
所有分层被放在了同一 Music Segment 中，对应的 High、Middle 和 Low 音轨会同步播放。其中 Middle 音轨只有一段简短的 Piano 乐句，所以每次都会播放。High 和 Low 音轨被设为了 Random Step 类型，由多个子音轨组成。这两条音轨还分别包含有一条空白子音轨。也就是说，在播放每段循环的时候，High 和 Low 乐曲都有可能是没有声音的。这样间奏音乐会更加富有变化一些。<br>
<br>
不过我确实遇到了一个问题，就是有些 High 和 Low 乐曲只播放一小节就会停止，感觉稍微有点突兀。针对这种情况，我特地在乐曲结尾插入了一个附加音符，来让它在下一小节的第一拍开始播放，并将其作为post-exit编到了 Wwise 中。<br>
<br>
<div align="center">
<img id="aimg_966387" aid="966387" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152011c2k1kfl3k0ar1o5b.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152011c2k1kfl3k0ar1o5b.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152011c2k1kfl3k0ar1o5b.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_966388" aid="966388" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152011jwzw51g5vvgnfvgo.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152011jwzw51g5vvgnfvgo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152011jwzw51g5vvgnfvgo.jpg" referrerpolicy="no-referrer">
</div><br>
下面是合在一起之后的效果，不妨试听一下。注意，里面的 Music Playlist Container 其实包含了两个 Music Segment：Interlude_Intro（单次播放）和 Interlude（无限循环）。其中 Interlude_Intro 只有一段简短的一小节 MidPiano 乐句。也就是说，间奏音乐每次都会先播放这段 Piano 乐句，分层的其他器乐内容在一小节之后才会切入进来。在 Demo 视频中，我们可以听到前面展示的 Piano、Bass Clarinet、Violin 和 Flute 以及其他一些乐器演奏的乐曲。<br>
<br>
<div align="center">（<a href="https://www.bilibili.com/video/BV1Wy4y127ft/" target="_blank">国内观赏视频通道</a>）</div><br>
在从间奏音乐过渡到牌面主题的时候，我遇到了跟前面类似的问题：MidPiano 乐曲有时会突然停止，显得不够连贯。为此，我特地在每段牌面主题的第一小节插入了采用钢琴演奏的 Bb + F 或 Bb + Eb 音符，来顺畅地承接前面的 Piano 乐曲。下面截取了两段由间奏音乐过渡到 TheHighPriestess 牌面主题的音频，我们来对比一下插入附加音符之前和之后的效果。<br>
<br>
刚开始我试了一下把上述附加音符编到 Wwise 中，后来发现直接将其渲染到牌面主题的音频文件中反而更容易些。在插入这些附加音符的时候，我还发现其实可以酌情考虑采用 Eb 和 Bb 以外的音调，但前提是第一和弦中要包含 Bb + F 或 Bb + Eb 音符。就拿 AceOfCups 牌面主题来说，我想让它听起来有点法国印象派乐曲的味道。于是就选择了 C 小调七和弦作为开头，使用了其中的四个音符：C、Eb、G 和 Bb。<br>
<br>
下面是合在一起之后的效果，不妨试听一下。这段视频展示了游戏原型里的占卜环节，不过目前只构建了一个非常简单的框架，最终作品中会包含更多画面之类的元素。在视频开头，除了间奏音乐和牌面主题，还可以听到一段简短的 Synth Pad 乐曲，用以实现 Game State 之间的过渡。<br>
<br>
<div align="center">（<a href="https://www.bilibili.com/video/BV1rK4y157ji/" target="_blank">国内观赏视频通道</a>）</div><br>
仔细听的话不难发现，在播放牌面主题之后马上回到了间奏音乐。对此，有个朋友建议我在当中（牌面主题与间奏音乐之间）插入一些音乐，来让玩家有时间思考牌面含义。这主意挺不错，我打算制作几段简短、轻柔的 Synth Pad 乐曲，来让它随着牌面花色变换。<br>
<br>
<strong><font color="#de5650">实现</font></strong><br>
<br>
在构建好音乐系统之后，必须想清楚如何将其有效地运用到游戏中。同样，在此我们只着重探讨游戏的占卜环节，暂不深究各种 Game State 之间的音乐变换或是占卜环节以外的话题。<br>
<br>
首先，我创建了一个 "DuringReading"（ “占卜中”） State Group，并在其中添加了与牌面主题和间奏音乐对应的 State。藉此，来确定在占卜环节的任意给定时刻播放哪段乐曲。目前我只完成了 10 种牌面的音乐设计，不过最终作品中将会涵盖所有的牌面。<br>
<br>
<div align="center">
<img id="aimg_966389" aid="966389" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152011v482b57zt6ze2m94.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152011v482b57zt6ze2m94.jpg" width="168" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152011v482b57zt6ze2m94.jpg" referrerpolicy="no-referrer">
</div><br>
接着，我创建了一个 "Reading" （ “占卜”） Switch Container，并将牌面主题和间奏音乐分别放在了不同的 Music Playlist Container 中。随后，又把各个 Music Playlist Container 与对应的 State 关联了起来。<br>
<br>
<div align="center">
<img id="aimg_966390" aid="966390" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152011qa1it1pjuivpqt4p.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152011qa1it1pjuivpqt4p.jpg" width="212" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152011qa1it1pjuivpqt4p.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_966391" aid="966391" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152012lz099510z475bsj7.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152012lz099510z475bsj7.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152012lz099510z475bsj7.jpg" referrerpolicy="no-referrer">
</div><br>
最后，我在 Wwise 中创建了与牌面主题和间奏音乐对应的 Event。在占卜环节的开头，每次都会先播放一段间奏音乐。这时会发送第一个 Event，来直接将 State 设为 Interlude，并通过 Play 动作触发相应的乐曲（不过这只是暂时的，最终游戏将由主菜单开始，到时会先播放菜单音乐）。之后会根据开牌结果发送其余 Event，来播放牌面主题并切换回间奏音乐。比方说，当前正在解读 Ace Of Cups。这时会先将 State 设为 AceOfCups，然后延迟 5 秒再切换回 Interlude。<br>
<br>
<div align="center">
<img id="aimg_966392" aid="966392" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152012kz0v138ss3d3y810.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152012kz0v138ss3d3y810.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152012kz0v138ss3d3y810.jpg" referrerpolicy="no-referrer">
</div><br>
除此之外，我还对占卜音乐的过渡进行了如下设置：在 State 发生变化时，直至到达当前所播 Music Segment 的 Exit Cue，才会过渡到与新 State 对应的 Music Playlist Container。其中，Exit Cue 设在乐曲的末尾（如有混响尾音，则作为post-exit予以播放）。所以，就算 State 在 5 秒之后发生了变化，也不会在乐曲播完之前就切换回间奏音乐。<br>
<br>
<div align="center">
<img id="aimg_966393" aid="966393" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152012bzw8nx8zkhid00ot.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152012bzw8nx8zkhid00ot.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152012bzw8nx8zkhid00ot.jpg" referrerpolicy="no-referrer">
</div><br>
在此，我要先感谢一下我的程序员朋友索尔·鲁兹 (Sol Lutze)。他先是帮忙构建了游戏的基本框架，然后又在 Unity 中编写了一些代码，让我可以将脚本化对象（scriptable object）轻松应用于各种牌面。如此一来，便不必再单独为每种牌面创建一个游戏对象（这样会占用大量的内存），只需从脚本化对象中提取数据并填充到空白模板中即可。脚本化对象包含很多数据（比如牌面是哪种花色、为画面选用哪张图片、要显示哪些含义内容），不过这里只有 musicEvent 数据字段跟我们目前讨论的问题有关。<br>
<br>
<div align="center">
<img id="aimg_966394" aid="966394" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152014zz1aduat9addaclc.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152014zz1aduat9addaclc.jpg" width="445" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152014zz1aduat9addaclc.jpg" referrerpolicy="no-referrer">
</div><br>
下图是实际脚本中的内容。我圈出了关键的两行代码。<br>
<br>
<div align="center">
<img id="aimg_966395" aid="966395" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152015yl7k6wfy6fvgkkiy.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152015yl7k6wfy6fvgkkiy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152015yl7k6wfy6fvgkkiy.jpg" referrerpolicy="no-referrer">
</div><br>
using AK; 告知脚本接下来要使用一些 Audiokinetic 代码；public AK.Wwise.Event musicEvent; 告知其允许选择 Wwise 中所创建的 Event，以便与脚本化对象进行关联。<br>
<br>
经过上述设置之后，只需在 Unity 中单击与脚本化对象关联的 Music Event，系统便会直接列出 Wwise Event 来供我快速选择。<br>
<br>
<div align="center">
<img id="aimg_966399" aid="966399" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152407as6qq6qekgq8pqa7.gif" data-original="https://di.gameres.com/attachment/forum/202103/18/152407as6qq6qekgq8pqa7.gif" width="480" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152407as6qq6qekgq8pqa7.gif" referrerpolicy="no-referrer">
</div><br>
另外，索尔还设置了一系列 Game State 来告知游戏当前正在执行的操作（发牌、开牌、解读…），从而确定何时播放牌面主题或是间奏音乐。其中比较关键的是表示当前正在显示牌面含义的 ReadingCard。该 Game State 会调用一个名为 ReadCard 的函数。针对这种情况，我向该函数添加了一行代码，来告知其发送与所解读牌面关联的 Event。<br>
<br>
<div align="center">
<img id="aimg_966396" aid="966396" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152015ykgk7zgne1kb74e1.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152015ykgk7zgne1kb74e1.jpg" width="494" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152015ykgk7zgne1kb74e1.jpg" referrerpolicy="no-referrer">
</div><br>
简而言之，这行代码的含义就是告知脚本针对牌面选择并发送名为 musicEvent 的 Wwise Event。比方说，当前正在解读 Ace Of Cups。在这种情况下，会首先将 State 切换为 AceOfCups，来由间奏音乐过渡到对应的牌面主题。然后延迟 5 秒再恢复为 Interlude，以在播完牌面主题后切换回间奏音乐。也就是说，我们并不需要另外创建一个 Event 来实现后半部分操作。<br>
<br>
我们再来看看游戏视频，体验下实际的视听效果。<br>
<br>
<div align="center">（<a href="https://www.bilibili.com/video/BV1rK4y157ji/" target="_blank">国内观赏视频通道</a>）</div><br>
在前面谈到索尔所做的工作时，估计你也发现了，我并不是一名专业的程序员。事实上，我从来没有特地参加过类似的培训。好在网上有很多免费的资源，让我学到了不少 C# 编程知识。就拿 Unity 来说，其官网上就有好些精彩的 C# 教程。如果你对编程感兴趣，建议先到网上查一查，看看有什么免费资源。<br>
<br>
对于占卜环节当中播放的音乐，我目前做的差不多也就这些了。在完成整个游戏之后，情况可能会大不相同。不过，我对现在为止取得的成果还是挺满意的。<br>
<br>
对于想自己制作游戏的音频开发者，我觉得不妨放开手脚大胆地去试试。有些技能在平时工作中未必用得到，业余时间拿来练练手不是挺好的嘛。想用 Unity 或是 Unreal 都行。网上有很多免费教程，可以一边学一边实践。<br>
<br>
最后，我要给自己的项目做个小小的宣传。《Divinuet》目前正在 Indiegogo 上筹集资金（当然，我可以独立地完成开发。但是，若能找些人来帮忙，肯定会更轻松一些。这样也能把游戏做得更好）。如果你对这款游戏感兴趣，请点击此处了解募资活动。<br>
<br>
<div align="center">
<img id="aimg_966397" aid="966397" zoomfile="https://di.gameres.com/attachment/forum/202103/18/152017an8ya89yaym2zn0a.jpg" data-original="https://di.gameres.com/attachment/forum/202103/18/152017an8ya89yaym2zn0a.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202103/18/152017an8ya89yaym2zn0a.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">梅根·卡恩斯 (MEGAN CARNES)</font></font></div><div align="center"><font size="2"><font color="#808080">作曲家、游戏开发者</font></font></div><br>
<i><font color="#808080">梅根·卡恩斯 (Megan Carnes) 是一名来自洛杉矶的作曲家、游戏开发者。她对互动音乐和生成音乐比较感兴趣，目前开发有《inter-view》和《Divinuet》两款音乐游戏。据悉，稍后推出的独立 2D 平台游戏《A Crooked Heart》也将由她作曲。同时，她还是 Game Audio LA 的联合发起人。</font></i><br>
<i><font color="#808080"><br>
</font></i><br>
<i><font color="#808080">megancarnesmusic.com/</font></i><br>
<i><font color="#808080">megancarnes.itch.io/</font></i><br>
<i><font color="#808080">@megancomposer</font></i><br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<font size="2"><font color="#808080">来源：audiokinetic</font></font><br>
<font size="2"><font color="#808080">原文：https://blog.audiokinetic.com/zh/the-interactive-music-systems-of-divinuet-part-1/</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            