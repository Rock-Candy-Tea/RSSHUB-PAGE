
---
title: '自制树莓派_防松鼠神器_在Reddit火了，13行代码就能让AI替你护食，成本300+元'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220209/v2_7c0a3a8ec14946f1be43fb43ae333100_img_000'
author: 36kr
comments: false
date: Wed, 09 Feb 2022 06:49:20 GMT
thumbnail: 'https://img.36krcdn.com/20220209/v2_7c0a3a8ec14946f1be43fb43ae333100_img_000'
---

<div>   
<p>没想到，有一天树莓派还能用在给鸟护食上！</p> 
<p>看这只松鼠抱着粮吃的正香……</p> 
<p class="image-wrapper"><img data-img-size-val="640,640" src="https://img.36krcdn.com/20220209/v2_7c0a3a8ec14946f1be43fb43ae333100_img_000" referrerpolicy="no-referrer"></p> 
<p>突然！就来了一股水流把它喷走了：</p> 
<p class="image-wrapper"><img data-img-size-val="640,640" src="https://img.36krcdn.com/20220209/v2_8a5e1ae415454e56ac2badf210f37680_img_000" referrerpolicy="no-referrer"></p> 
<p>再来一次？还是没能幸免，继续被水喷中：</p> 
<p class="image-wrapper"><img data-img-size-val="640,640" src="https://img.36krcdn.com/20220209/v2_b2776c713a8e49b6a6fae1195bdb9c40_img_000" referrerpolicy="no-referrer"></p> 
<p>此时松鼠内心OS：谁这么闲每天没事喷劳资？？？</p> 
<p class="image-wrapper"><img data-img-size-val="1080,1043" src="https://img.36krcdn.com/20220209/v2_ba2ecd1cecb84006973acb7cbc06b9dd_img_000" referrerpolicy="no-referrer"></p> 
<p>原来，这是一位小哥用树莓派做出的<strong>喂鸟器保护器</strong>。</p> 
<p>因为自己<a class="project-link" data-id="66129" data-name="后院" data-logo="https://img.36krcdn.com/20210807/v2_3b5edfde50ea43ed97ec33e0c7c33fac_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/66129" target="_blank">后院</a>鸟儿喂食器的粮被松鼠频频偷走，这位小哥赌上自己机器学习爱好者的尊严，开发了这个新装置。</p> 
<p>它能够让摄像头每30<a class="project-link" data-id="3969007" data-name="秒拍" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969007" target="_blank">秒拍</a>下一张照片，然后由CV算法来检测喂鸟器上是否有松鼠。如果有的话，信号就会发送给花园里的电控水龙头，让它朝着喂鸟器喷水赶走松鼠。</p> 
<p>而做出这个设备，小哥用到的AI模型只需<strong>13行</strong>代码就能搞定，训练甚至只花了45分钟。</p> 
<p>效果也是立竿见影的，用了几个星期后，松鼠造访的频率直线下降。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,682" src="https://img.36krcdn.com/20220209/v2_9aee25cc5a4d4352b43f865a088f48a2_img_000" referrerpolicy="no-referrer"></p> 
<p>嗯，此刻可能更多要心疼小哥家附近的松鼠了。</p> 
<h2><strong>“13行代码+树莓派”赶走松鼠</strong></h2> 
<p>效果这么好的设备，做起来难吗？</p> 
<p>非常easy，一共只需3步：</p> 
<p>第一，让摄像头每30秒拍下一张照片；</p> 
<p>第二，将照片发送到AWS Lambda端点，在端点上使用训练好的AI模型检测照片；</p> 
<p>第三，如果检测到照片中有松鼠，设备就会将信号发送给电控水龙头的开关，这时花园中的喷头就会持续喷出几秒钟水流赶走松鼠。</p> 
<p>大概效果就是这样：</p> 
<p class="image-wrapper"><img data-img-size-val="640,640" src="https://img.36krcdn.com/20220209/v2_e017dd5188354c49b9d9ad9ab23fa12b_img_000" referrerpolicy="no-referrer"></p> 
<p>判断画面中是否有松鼠，靠的则是小哥自己用fast.ai训练的一个模型。</p> 
<p>他首先自己收集了一个数据集——连续几个星期让相机每30秒就拍一次照片，然后手动将照片分类为“有松鼠”和“没有松鼠”两类。</p> 
<p>之后用这个数据集来训练模型，小哥是在Google Colab上搞定的。</p> 
<p>一共只有<strong>13行</strong>代码，训练全程花了大约<strong>45分钟</strong>。</p> 
<p>硬件端，这套设备运行的核心是一个带有摄像头的树莓派，在亚马逊商店能直接买到。</p> 
<p class="image-wrapper"><img data-img-size-val="876,942" src="https://img.36krcdn.com/20220209/v2_877713d711c146079790d61638acdc4f_img_000" referrerpolicy="no-referrer"></p> 
<p>由于在试验过程中弄出了短路、不小心烧坏了自己的Pi 4，所有小哥不得不用Pi 2+AWS Lambda的方式来完成整<a class="project-link" data-id="7583" data-name="个推" data-logo="https://img.36krcdn.com/20220120/v2_36285bc5bdd948668c363be6927c18f3_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4376601213?mp=zzquote" target="_blank">个推</a>理过程。</p> 
<p>在实际使用过程中，如果模型判断照片中有松鼠的置信度超过70%，就会启动装置。同时它还会拍下视频和照片，这样小哥就能从历史记录中看到模型是否判断正确了。</p> 
<p>小哥表示，这套装置的准确率为<strong>86.6%</strong>，赶走大部分来访的松鼠没什么问题，但也有失误的时候。</p> 
<p>从总共记录的321次防御中可以看到，其中有43次判断失误。</p> 
<p>有时画面中是鸽子在吃东西、有时画面中什么都没有，有时则是小哥本人路过了那一区域，设备也喷出了水流。</p> 
<p>针对鸽子的情况，小哥猜测可能是自己做数据集那段时间，很少有鸽子光顾他的喂食器，所以导致模型判断有误。</p> 
<p>其中有一天设备<a class="project-link" data-id="4140855" data-name="则一" data-logo="https://img.36krcdn.com/20210714/v2_fc235e3a06704408a62e6b8a13df703d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4375401210" target="_blank">则一</a>直在喷水，无论喂食器上站的是鸟还是松鼠，或者什么都没有。</p> 
<p>后来小哥发现，这是因为<a class="project-link" data-id="416084" data-name="有树" data-logo="https://img.36krcdn.com/20210811/v2_1a9d83c23c004f6388adda2d3feaafa7_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/416084" target="_blank">有树</a>枝刚好挡在了松鼠平常会出现的位置上。</p> 
<p class="image-wrapper"><img data-img-size-val="602,598" src="https://img.36krcdn.com/20220209/v2_94362966d86c47ff9c41b81d2e03a7b6_img_000" referrerpolicy="no-referrer"></p> 
<p>整体来看，这套设备一共花费了大约50美元，也就是人民币300多块。主要用来购买硬件设备，AWS Lambda则是小哥白嫖的（doge）。</p> 
<h2><strong>小哥本职是位记者</strong></h2> 
<p>最后来介绍一下这套设备的主人Jeremy B. Merrill，他是华盛顿邮报的一位记者，平常会用机器学习、数据分析来写一些调查新闻。</p> 
<p class="image-wrapper"><img data-img-size-val="400,402" src="https://img.36krcdn.com/20220209/v2_8e94d4d4e6494c2793ba456d1e3b2ad3_img_000" referrerpolicy="no-referrer"></p> 
<p>他的杰作也吸引了不少网友的关注，Reddit上热度300+。</p> 
<p>不少人受到他的启发，想通过类似的方法搞定后院里乱窜的松鼠、野猫。</p> 
<blockquote> 
 <p>是时候做出一个猫屎爆破神器阻止野猫来我的花园便便了！</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,236" src="https://img.36krcdn.com/20220209/v2_eb5cf59259194873af29718b403ff8a5_img_000" referrerpolicy="no-referrer"></p> 
<p>也有人脑洞大开，认为长此以往松鼠会觉得这是个不错的水源地，总之就还是要经常造访了。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,225" src="https://img.36krcdn.com/20220209/v2_b243ff7fdd3b447a8cbdf2058ece85dd_img_000" referrerpolicy="no-referrer"></p> 
<p>看来，各种突然造访的动物们的确有够让歪果人头痛的。</p> 
<p>此前YouTube上有一位博主在后院做了一套非常复杂的设备，就是为了来恶搞突然来捣乱的松鼠。</p> 
<p class="image-wrapper"><img data-img-size-val="640,329" src="https://img.36krcdn.com/20220209/v2_7b18f22388054b7984c029d63da0bb85_img_000" referrerpolicy="no-referrer"></p> 
<p>相比之下，用AI识别然后精准“打击”的方法似乎实用性更强。</p> 
<p>由于最近已经入冬，小哥暂时停用了这套设备，松鼠也鲜少造访了，他表示之后天气转暖还会继续用下去。</p> 
<p>不知重新启动后的效果会是如何呢？蹲个后续~</p> 
<p>参考链接：</p> 
<p>[1]<a href="https://jeremybmerrill.com/blog/2022/01/squirrel-soaker-9000-repelling-squirrels-with-ai.html" _src="https://jeremybmerrill.com/blog/2022/01/squirrel-soaker-9000-repelling-squirrels-with-ai.html">https://jeremybmerrill.com/blog/2022/01/squirrel-soaker-9000-repelling-squirrels-with-ai.html</a></p> 
<p>[2]<a href="https://www.reddit.com/r/MachineLearning/comments/sctxqh/p_i_built_a_robot_to_protect_my_birdfeeder_from/" _src="https://www.reddit.com/r/MachineLearning/comments/sctxqh/p_i_built_a_robot_to_protect_my_birdfeeder_from/">https://www.reddit.com/r/MachineLearning/comments/sctxqh/p_i_built_a_robot_to_protect_my_birdfeeder_from/</a> </p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/nZyRVq7IZZ_THrdOSIDZ5Q">“量子位”（ID:QbitAI）</a>，作者：明敏，36氪经授权发布。</p>  
</div>
            