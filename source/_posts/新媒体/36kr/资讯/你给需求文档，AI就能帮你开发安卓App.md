
---
title: '你给需求文档，AI就能帮你开发安卓App'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210607/v2_1fe0e955fe0e48ad92f7f795bae1c862_img_000'
author: 36kr
comments: false
date: Mon, 07 Jun 2021 11:50:30 GMT
thumbnail: 'https://img.36krcdn.com/20210607/v2_1fe0e955fe0e48ad92f7f795bae1c862_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/-PFBlVGCiKKgABLNR6p2LQ">“量子位”（ID:QbitAI）</a>，作者：关注前沿科技，36氪经授权发布。</p> 
<p>丰色 发自 凹非寺<a class="project-link" data-id="397416" data-name="量子位" data-logo="https://img.36krcdn.com/20200729/v2_ac002e38e2904e0280dae679728d9e3e_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/397416" target="_blank">量子位</a> 报道 | 公众号 QbitAI</p> 
<p>用自然语言生成代码不算稀奇，但现在，这项技术涉及的业务范围真是越来越广了。</p> 
<p>就有一个叫做Text2App的“AI”，你“喂”给它一串文字需求，它就能直接给你“消化”成安卓应用！</p> 
<p class="image-wrapper"><img data-img-size-val="451,242" src="https://img.36krcdn.com/20210607/v2_1fe0e955fe0e48ad92f7f795bae1c862_img_000" referrerpolicy="no-referrer"></p> 
<p>不信你看。</p> 
<p>这是输入的文字：</p> 
<blockquote> 
 <p>创建一个APP，上面有一个视频、一个按钮，一个文本转语音的功能以及一个手机加速传感器。点击按钮，播放视频；摇晃手机，念出文字“happy Text2App”。</p> 
</blockquote> 
<p>整个过程除了等编译花上几分钟，无需别的代码操作，就能直接生成一个安卓应用。</p> 
<p>不知广大程序员们尤其是安卓开发，感觉如何？</p> 
<h2>介于文字描述和源码之间的“中间语言”</h2> 
<p>Text2App这个框架出自加州大学洛杉矶分校和孟加拉国工程技术大学。</p> 
<p class="image-wrapper"><img data-img-size-val="996,194" src="https://img.36krcdn.com/20210607/v2_2a36b10d08f74753baf82b08e5b90e2f_img_000" referrerpolicy="no-referrer"></p> 
<p>它不是直接将自然语言生成源码，而是先生成中间语言，再由编译器生成源码。</p> 
<p>为什么要先生成中间语言呢？</p> 
<p>因为此前大多数根据文字描述生成程序的研究都是基于端到端的神经机器翻译 (NMT) 模型，类似于Google 翻译，将自然语言直接翻译成源码。</p> 
<p>虽然其中一些效果还不错，但大多数无法生成大一点的、上百行代码的程序。</p> 
<p>为了克服这个限制，研究人员就在这个过程发明了一个新的形式语言 （formal language）做“桥梁”。</p> 
<p>它能“搞懂”复杂的源码，并将用户给定的自然语言转换出一小部分tokens（标记），再形成一个简单的程序表示代码。</p> 
<p>最后用研究人员开发的一个编译器，就能把这个中间语言转换成源码。</p> 
<p>最理解编程语言的还是编译器，完全让AI来生成复杂的程序还不行，所以离不开编译器的大力支持。</p> 
<p>当然，生成中间语言还是靠的神经机器翻译模型。</p> 
<p>下面是“文字描述转换成APP”的具体流程：</p> 
<p class="image-wrapper"><img data-img-size-val="540,220" src="https://img.36krcdn.com/20210607/v2_0849a58d01244a10bae5913f1b350057_img_000" referrerpolicy="no-referrer"></p> 
<p>文字描述：</p> 
<blockquote> 
 <p>Create an app with a textbox, a button named “Speak”, and a text2speech. When the button is clicked, speak the text in the text box.</p> 
</blockquote> 
<p>上面这段自然语言首先被格式化（例如将“Speak”转为“ ‘STRING0’:’Speak’ ”），然后交给一个有编码器和解码器的Seq2Seq神经网络翻译成简单的应用程序表示（SAR）——这就是上面说的中间语言：</p> 
<blockquote> 
 <p><complist> <textbox> <button> string0 </button> <text2speech> </complist><code> <button1clicked> <text2speech1> <textboxtext1> </text2speech1></button1clicked> </code></p> 
</blockquote> 
<p>再通过SAR编译器将中间语言转换成MIT App Inventor源码文件(.scm/.bky)，由MIT打包成最终可用的安卓端应用程序即可。</p> 
<p>下面是自然语言和中间语言（SAR）自动合成的示意图，很直观：</p> 
<p class="image-wrapper"><img data-img-size-val="675,224" src="https://img.36krcdn.com/20210607/v2_6be70bc153334048b183cebfcfebe166_img_000" referrerpolicy="no-referrer"></p> 
<h2>功能还比较初级</h2> 
<p>正如大家所料，这个框架还是比较初级，目前描述文字需要被限定在一个固定范围：</p> 
<p>只能描述11种组件：文本框、按钮、标签、播放器、时间选择器……</p> 
<p>能实现的事件、操作等倒是没有明确限制，感兴趣的可以具体测测能实现多少。</p> 
<p class="image-wrapper"><img data-img-size-val="1000,621" src="https://img.36krcdn.com/20210607/v2_78b38b60092541bc8185838e295fa8b1_img_000" referrerpolicy="no-referrer"></p> 
<p>目前的功能也很单一，广大安卓开发程序员们还远远不用担心AI“抢饭碗”。</p> 
<p>不过研究人员说了，最终目的是使Text2App 成为一个成熟的基于自然语言的APP开发平台。</p> 
<p>需要多久呢？还未可知。</p> 
<p>论文地址：<a target="_blank" rel="noopener noreferrer" href="https://arxiv.org/abs/2104.08301">https://arxiv.org/abs/2104.08301</a></p> 
<p>完整视频及试玩链接：https://text2app.github.io/</p> 
<p>参考链接：https://techxplore.com/news/2021-06-text2app-framework-android-apps-text.html</p>  
</div>
            