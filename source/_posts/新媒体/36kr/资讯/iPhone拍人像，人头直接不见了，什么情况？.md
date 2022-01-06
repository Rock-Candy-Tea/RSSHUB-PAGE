
---
title: 'iPhone拍人像，人头直接不见了，什么情况？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220106/v2_4e5316bcfd7046bfac654afc419cbddd_img_000'
author: 36kr
comments: false
date: Thu, 06 Jan 2022 07:41:47 GMT
thumbnail: 'https://img.36krcdn.com/20220106/v2_4e5316bcfd7046bfac654afc419cbddd_img_000'
---

<div>   
<p>随手拿iPhone拍了张照，结果……诶我头呢？</p> 
<p class="image-wrapper"><img data-img-size-val="878,1231" src="https://img.36krcdn.com/20220106/v2_4e5316bcfd7046bfac654afc419cbddd_img_000" referrerpolicy="no-referrer"></p> 
<p>我头怎么没了？！</p> 
<p>这是什么误入什么恐怖电影了吗？</p> 
<p>负责拍照的老哥看着自己手机里的“树叶人”，百思不得其解，于是将照片和相机参数<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>丢到了推特上，并表示：</p> 
<blockquote> 
 <p>从2007年到现在，我总共拍了大概47000张照片，还从来没有遇到过这种情况！</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="946,978" src="https://img.36krcdn.com/20220106/v2_6c209b726dba481ca907038ebec965f3_img_000" referrerpolicy="no-referrer"></p> 
<p>而大批吃瓜网友也火速赶到，短短一天在推特就有了上千热度，在Hacker News也引发了大量讨论。</p> 
<h2><strong>真相只有一个</strong></h2> 
<p>这位老哥先梳理了一下情况：</p> 
<p>首先，肯定不是叶子正好掉下来挡住了人脸。</p> 
<p>因为照片上是能依稀看到<a class="project-link" data-id="3969467" data-name="人物" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969467" target="_blank">人物</a>头部的侧面轮廓的，而且仔细看，替代掉人头的那部分完全就是一个连着枝干的树叶局部图。</p> 
<p class="image-wrapper"><img data-img-size-val="826,458" src="https://img.36krcdn.com/20220106/v2_224ba947192b49acbede03ed477b6e9a_img_000" referrerpolicy="no-referrer"></p> 
<p>而老哥最后也确定：代替了脸部的这部分叶子确实来自人物身后的背景。</p> 
<p>那有没有可能是光线问题，或者图像被算法自动锐化造成的呢？</p> 
<p>马上就有人跳出来反驳：</p> 
<blockquote> 
 <p>和那没关系，这很明显就是出现了图像信息的丢失或替换。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="995,391" src="https://img.36krcdn.com/20220106/v2_6ff85943152d4660a6c4b87ff657f9c3_img_000" referrerpolicy="no-referrer"></p> 
<p>再看相机参数，又非常正常，于是就有人提出，可能是现在手机的智能拍摄背后的<strong>算法</strong>问题。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,345" src="https://img.36krcdn.com/20220106/v2_ad0c3aefe72b4fcfa40dd019d187f2e4_img_000" referrerpolicy="no-referrer"></p> 
<p>没错，就是现在很多智能手机都在用的<strong>HDR</strong>技术。</p> 
<p>截一段iPhone的官方解释就是：</p> 
<p>在不同的曝光条件下连续快速拍摄多张照片，然后将它们合成一张图片，以带来更多的高光和阴影细节。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,535" src="https://img.36krcdn.com/20220106/v2_526a6a7fcef34837aeaa5b26fb2cf1ba_img_000" referrerpolicy="no-referrer"></p> 
<p>而这次的“无头式”拍摄很可能出现在合成阶段，也就是像这条评论解释的一样：</p> 
<blockquote> 
 <p>深度融合（Deep Fusion）技术试图将多张照片合成修补成一张，但是失败了。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,225" src="https://img.36krcdn.com/20220106/v2_4d14223462644614be0573bfa8dca2a9_img_000" referrerpolicy="no-referrer"></p> 
<p>啥意思呢？假设当事人老哥在0.2秒内按下了快门，拍了大概20帧左右的图像。</p> 
<p>在这段时间里，不管是人物还是背景中的叶子，都会产生一些移动。</p> 
<p>本来的情况是，智能算法追踪图像中的固定主体，并“撤销”或“删除”主体在不同图像中产生的移动（也就是丢弃“异常值”），使图像尽可能对齐。</p> 
<p>然后再通过取图像像素的中位数或平均值，把上面的图像合并，最终<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>一张正常人像照。</p> 
<p class="image-wrapper"><img data-img-size-val="500,500" src="https://img.36krcdn.com/20220106/v2_0f0b5c9c726845d3bdaa6154d8805354_img_000" referrerpolicy="no-referrer"></p> 
<p>但如果背景中的叶子在快速飘动，在每<a class="project-link" data-id="397963" data-name="一帧" data-logo="https://img.36krcdn.com/20210811/v2_1420e162949a44c8a20f873730fdc29c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/397963" target="_blank">一帧</a>图像间都产生了较大幅度的移动，那么在很多图像上的追踪效果就不会太好，很可能丢弃掉的“异常值”才是真正的图像内容。</p> 
<p>因此，最后也就得到了一张“树叶人”照片。</p> 
<p>对于这一猜测，很多人都表示认同。</p> 
<p>而当事人老哥目前也没有艾特官方要说法的意思，只是将其当作一个因缺思听的小故事。</p> 
<p>现在，他将原始图片和详细信息分享给了评论区的一位热心网友——就是这位4.5万粉的摄影师兼个人开发者，委托他帮忙调查。</p> 
<p>目前还没有进一步结果。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,226" src="https://img.36krcdn.com/20220106/v2_cf34f527c7864a45b5d3c6bb6e9a0b72_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>“会不会手机才是对的？”</strong></h2> 
<p>其实，虽然当事人老哥觉得这事儿闻所未闻，但评论区还是出现了不少“受害者”交流情况。</p> 
<p>比如这位……等等你这是连头带胳膊整个上半身都没了啊！</p> 
<p class="image-wrapper"><img data-img-size-val="1080,862" src="https://img.36krcdn.com/20220106/v2_24dc2ba9d22844909669caab02bc3cc5_img_000" referrerpolicy="no-referrer"></p> 
<p>还有痛失清晰头部的酒瓶：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1100" src="https://img.36krcdn.com/20220106/v2_d131ca2f78064504b0752323fbab9ff5_img_000" referrerpolicy="no-referrer"></p> 
<p>评论区不少人都觉得，这些图片稍微处理一下就能拿去当超自然现象的证据了好吗！</p> 
<p>不过一位疑似社恐的用户则留言道：</p> 
<p>什么恐怖不恐怖的，这种每次拍照脸部就会被树叶代替的技术给我也整一个！</p> 
<p class="image-wrapper"><img data-img-size-val="1080,188" src="https://img.36krcdn.com/20220106/v2_ebdca638e52741b5aebe123b99049f88_img_000" referrerpolicy="no-referrer"></p> 
<p>最后，来分享评论区的一个最高赞：</p> 
<blockquote> 
 <p>如果手机是对的，而我们才是错的呢？</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,223" src="https://img.36krcdn.com/20220106/v2_803cf44ab7a240babc7c9acaaf19d640_img_000" referrerpolicy="no-referrer"></p> 
<h3>参考链接：</h3> 
<p>[1]https://twitter.com/mitchcohen/status/1476351601862483968</p> 
<p>[2]https://news.ycombinator.com/item?id=29739235</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/uQ2wkUYUFOTrmsKIhqsjyg">“量子位”（ID:QbitAI）</a>，作者：博雯，36氪经授权发布。</p>  
</div>
            