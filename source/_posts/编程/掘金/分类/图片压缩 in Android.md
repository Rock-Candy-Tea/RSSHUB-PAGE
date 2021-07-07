
---
title: '图片压缩 in Android'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://gitee.com/hss012489/picbed/raw/master/picgo/1617068183123-1617068169614-image-20210330093604413.jpg'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 03:57:07 GMT
thumbnail: 'https://gitee.com/hss012489/picbed/raw/master/picgo/1617068183123-1617068169614-image-20210330093604413.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">图片压缩</h1>
<h1 data-id="heading-1">背景</h1>
<p>成像系统两大核心: 镜头+感光元器件</p>
<p>底大一级压死人</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1617068183123-1617068169614-image-20210330093604413.jpg" alt="image-20210330093604413" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小米11发布会上:</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1617068253709-image-20210330093733661.jpg" alt="image-20210330093733661" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616399049871-v2-de2f98d025944e3096266ac6b0c0a3bf_720w.jpg" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一般全画幅单反/微单相机,厂家设置的有效像素为2400万像素   cmos面积:864mm2   每平方毫米上2.78个像素</p>
<p>asp-c                                                          有效像素为2400万像素   cmos面积 332.3mm2  每平方毫米上7.23个像素</p>
<p>华为mate40 pro  1/1.28英寸           5000万像素,常用1000w像素   cmos面积192.11mm2  每平方毫米26个/5.2个像素</p>
<blockquote>
<p>如果按全画幅单反的解析度,华为mate40 pro 应该配500万像素,而不是5000万.</p>
</blockquote>
<p>小米10 pro  1/1.33英寸      (15.28mmx11.46mm)  一亿像素            cmos面积175.09mm2   每平方毫米上57个像素</p>
<p>(1英寸约等于25.4mm)</p>
<p>从数值上看,手机1000w像素拍出来的放到最大,效果应该和asp-c 2400万像素放到最大的效果差不多</p>
<h3 data-id="heading-2">but: 细节见功夫</h3>
<p>放大到100%, 手机拍照的效果比相机差太多了.不是一个档次</p>
<h1 data-id="heading-3">压缩算法/图片格式</h1>
<p>gif:动图格式,兼容性好,画面质量较差.</p>
<p>png: 可带透明通道.文件偏大.无损压缩.</p>
<p>jpeg:无与伦比的兼容性,非常不错的压缩比. 有损压缩.</p>
<p>webp: 谷歌主推,没有流行起来</p>
<p>Guetzli: 谷歌出的玩具算法,以更高的压缩比压成jpg格式,但极度耗内存和cpu,基本不具有工业价值.</p>
<p>hevc/heif: h.265对应的图片压缩算法,有版权问题. 腹死胎中,只有苹果玩了几个版本.</p>
<p>avif: h.266对应的图片压缩算法,全开源. 压缩比超高,不惧反复压缩.各巨头火热开发中,很有前景.</p>
<h2 data-id="heading-4">质量压缩</h2>
<pre><code class="hljs language-java copyable" lang="java">bitmap.compress(Bitmap.CompressFormat.JPEG, quality, outputStream);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>quality: 取值0-100.</p>
<p>一般来说,手机/相机拍照的质量为96,98.</p>
<p>其实肉眼看,80和100并无明显差别.</p>
<p>用于存硬盘收藏的图片,推荐85</p>
<p>用于聊天,晒朋友圈之类的上传,推荐70</p>
<p>用于跑算法模型的上传,具体看算法的要求. 可以使用85的webp</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616405892708-image-20210322173812647.jpg" alt="image-20210322173812647" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616405956825-0-%E5%A9%BA%E6%BA%902.jpeg" alt="0-婺源2" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616406082524-image-20210322174122498.jpg" alt="image-20210322174122498" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616406102551-image-20210322174142524.jpg" alt="image-20210322174142524" loading="lazy" referrerpolicy="no-referrer"></p>
<p>![image-20210322174334485](/Users/hss/Library/Application Support/typora-user-images/image-20210322174334485.png)</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616406236065-image-20210322174356037.jpg" alt="image-20210322174356037" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616406253242-image-20210322174413216.jpg" alt="image-20210322174413216" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616406270433-image-20210322174430404.jpg" alt="image-20210322174430404" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616406343236-image-20210322174543208.jpg" alt="image-20210322174543208" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616407908117-image-20210322181148076.jpg" alt="image-20210322181148076" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">图片的缩与放</h1>
<blockquote>
<p>向下采样     向上插值</p>
</blockquote>
<p>相关算法:</p>
<ul>
<li>
<p>单线性/最近邻: 速度最快,但可能失真,有明显锯齿</p>
</li>
<li>
<p>双线性</p>
</li>
<li>
<p>双三次/双立方</p>
</li>
<li>
<p>Lanczos</p>
</li>
</ul>
<p>其中,Android只实现了单线性和双线性.</p>
<p>且直接读流的向下采样时,只支持单线性采样.</p>
<h2 data-id="heading-6">缩小: 向下采样:</h2>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616412133354-image-20210322192213318.jpg" alt="image-20210322192213318" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">放大: 向上插值</h2>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616412176939-image-20210322192256909.jpg" alt="image-20210322192256909" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616412194671-image-20210322192314640.jpg" alt="image-20210322192314640" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">Android里的单线性/双线性操作:</h2>
<h3 data-id="heading-9">从流中解码bitmap:</h3>
<pre><code class="hljs language-java copyable" lang="java">BitmapFactory.Options options = <span class="hljs-keyword">new</span> BitmapFactory.Options();
<span class="hljs-comment">//或者 inDensity 搭配 inTargetDensity 使用，算法和 inSampleSize 一样</span>
options.inSampleSize = <span class="hljs-number">2</span>;<span class="hljs-comment">//向下采样,仅支持单线性采样</span>
Bitmap compress = BitmapFactory.decodeFile(<span class="hljs-string">"/sdcard/test.png"</span>, options);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">bitmap的scale操作:</h3>
<pre><code class="hljs language-java copyable" lang="java">Bitmap bitmap = BitmapFactory.decodeFile(<span class="hljs-string">"/sdcard/test.png"</span>);
Bitmap compress = Bitmap.createScaledBitmap(bitmap, bitmap.getWidth()/<span class="hljs-number">2</span>, bitmap.getHeight()/<span class="hljs-number">2</span>, <span class="hljs-keyword">true</span>);<span class="hljs-comment">//最后一个参数 true代表使用双线性,false:使用单线性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者使用matrix操作:</p>
<pre><code class="hljs language-java copyable" lang="java">Bitmap bitmap = BitmapFactory.decodeFile(<span class="hljs-string">"/sdcard/test.png"</span>);
Matrix matrix = <span class="hljs-keyword">new</span> Matrix();
matrix.setScale(<span class="hljs-number">0.5f</span>, <span class="hljs-number">0.5f</span>);
bm = Bitmap.createBitmap(bitmap, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, bit.getWidth(), bit.getHeight(), matrix, <span class="hljs-keyword">true</span>);
<span class="hljs-comment">//最后一个参数 true代表使用双线性,false:使用单线性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">bitmap在view上的绘制:</h3>
<p>当把一个bitmap对象绘制到比bitmap尺寸大的view上时,默认使用单线性插值.此时锯齿明显</p>
<p>如果要使用双线性,重写view的onPreDraw(canvas)方法,给canvas加上抗锯齿即可:</p>
<pre><code class="hljs language-java copyable" lang="java">canvas.setDrawFilter(<span class="hljs-keyword">new</span> PaintFlagsDrawFilter(<span class="hljs-number">0</span>,Paint.ANTI_ALIAS_FLAG|Paint.FILTER_BITMAP_FLAG));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是一朵花放大四倍的对比:</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616412823838-image-20210322193343801.jpg" alt="image-20210322193343801" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616412838591-image-20210322193358557.jpg" alt="image-20210322193358557" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更多效果见:<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-1212-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-1212-1-1.html" ref="nofollow noopener noreferrer"><strong>QQ音乐团队分享：Android中的图片压缩技术详解（下篇）</strong></a></p>
<blockquote>
<p>在Android上,图片缩放推荐使用双线性</p>
</blockquote>
<h1 data-id="heading-12">jpeg压缩算法的改进</h1>
<p>JPEG压缩算法的过程有：</p>
<p>色彩模型变换(bitmap的RGB转YUV)，离散余弦变换、量化、Z字形编码、游程编码、Huffman编码</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhangqizky%2Fjpeg-compression" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhangqizky/jpeg-compression" ref="nofollow noopener noreferrer">压缩过程详解</a></p>
<ul>
<li>
<p>Android上开启霍夫曼压缩  :  7.0开始已经自动开启.</p>
</li>
<li>
<p>自适应的量化表: 不使用jpeg算法内置的两张量化表,而针对特定类型图片使用调教好的量化表</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.paper.edu.cn%2Fscholar%2Fshowpdf%2FOUD2AN1INTT0cxeQh" target="_blank" rel="nofollow noopener noreferrer" title="http://www.paper.edu.cn/scholar/showpdf/OUD2AN1INTT0cxeQh" ref="nofollow noopener noreferrer">自适应量化表的 JPEG 压缩技术</a></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616414113239-1614910763403-image-20210305101923363.jpg" alt="image-20210305101923363" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h1 data-id="heading-13">图像质量评价</h1>
<p>参考</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F40819506" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/40819506" ref="nofollow noopener noreferrer">无参考评价图像质量（主观评价客观化）</a></p>
<p>指标/维度:</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1616414296370-1612765776802-v2-3e04265cbd8bceb41da26ebe90df3663_720w.jpg" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>此处不关注图片本身质量,只关注jpg压缩过程中量化表所得压缩质量</p>
</blockquote>
<h2 data-id="heading-14">1 单图质量评价</h2>
<h3 data-id="heading-15">量化因子相关的质量</h3>
<blockquote>
<p>可用于避免重复压缩</p>
</blockquote>
<p>已知图像和量化表,反向估算量化因子,得到图片质量的估计值.</p>
<p>可使用库: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsephiroth74%2FAndroid-Exif-Extended" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sephiroth74/Android-Exif-Extended" ref="nofollow noopener noreferrer">github.com/sephiroth74…</a> 里的</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">int</span> jpeg_quality =  exif.getQualityGuess()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Ftomatomas%2Farticle%2Fdetails%2F62235963" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/tomatomas/article/details/62235963" ref="nofollow noopener noreferrer">如何获取JPEG图片质量和预测压缩图片大小</a>中单独的算法</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_40728599%2Farticle%2Fdetails%2F109185666" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_40728599/article/details/109185666" ref="nofollow noopener noreferrer">用c语言从JPEG（文件后缀为.jpg）中提取jpeg压缩的亮度和色度量化矩阵</a></p>
<p>两个算法的测试结果如下:</p>
<p>实际压缩质量50以上,可准确判断质量,50以下,已无法准确判断.</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1617160037431-%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_c710b92e-db33-4f7e-a485-fe57c4ddf50d.jpg" alt="企业微信截图_c710b92e-db33-4f7e-a485-fe57c4ddf50d" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1617160652089-image-20210331111732037.jpg" alt="image-20210331111732037" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是,这个准确也是取决于jpg压缩的实际算法,如果使用的是libjpeg,反推出的量化因子就准确.</p>
<p>如果使用的是mozjpeg,那么反推出的质量也会不准确:</p>
<p>比如,使用squoosh里的mozjpeg压缩一张图到75的质量,计算出的质量因子为:</p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1617160479094-image-20210331111439045.jpg" alt="image-20210331111439045" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://gitee.com/hss012489/picbed/raw/master/picgo/1617160397707-image-20210331111317646.jpg" alt="image-20210331111317646" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">工业上可用的两个质量评价指标</h3>
<ul>
<li>
<p>亮度: 计算平均亮度或者ROI的平均亮度, 绝对值可用.</p>
</li>
<li>
<p>模糊程度(高斯模糊):   opencv的拉普拉斯算子计算可得.可用于相对比较.</p>
</li>
</ul>
<h2 data-id="heading-17">压缩前后质量比对评价</h2>
<h3 data-id="heading-18">Butteraugli</h3>
<p>Butteraugli 项目是一个图片差异比较库，用于测试图片的心理视觉误差阈值，即查看者开始注意到图片质量下降的点。换句话说，此项目试图量化您的压缩图片的失真程度。</p>
<h3 data-id="heading-19">SSIM (Structural SIMilarity) 结构相似性</h3>
<blockquote>
<p>PNSR一般用于视频质量快速评价  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F50757421" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/50757421" ref="nofollow noopener noreferrer">图像质量评价指标之 PSNR 和 SSIM</a></p>
</blockquote>
<h1 data-id="heading-20">exif</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FExif" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/Exif" ref="nofollow noopener noreferrer">zh.wikipedia.org/wiki/Exif</a></p>
<blockquote>
<p>不仅仅是jpg图片可以有exif,webp也可以有</p>
</blockquote>
<p><strong>可交换图像文件格式</strong>（英语：Exchangeable image file format，官方简称<strong>Exif</strong>），是专门为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E6%2595%25B0%25E7%25A0%2581%25E7%259B%25B8%25E6%259C%25BA" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E6%95%B0%E7%A0%81%E7%9B%B8%E6%9C%BA" ref="nofollow noopener noreferrer">数码相机</a>的照片设定的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E6%2596%2587%25E4%25BB%25B6%25E6%25A0%25BC%25E5%25BC%258F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F" ref="nofollow noopener noreferrer">文件格式</a>，可以记录数码照片的属性信息和拍摄数据。</p>
<p>Exif最初由<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E6%2597%25A5%25E6%259C%25AC%25E9%259B%25BB%25E5%25AD%2590%25E5%25B7%25A5%25E6%25A5%25AD%25E7%2599%25BC%25E5%25B1%2595%25E5%258D%2594%25E6%259C%2583" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E9%9B%BB%E5%AD%90%E5%B7%A5%E6%A5%AD%E7%99%BC%E5%B1%95%E5%8D%94%E6%9C%83" ref="nofollow noopener noreferrer">日本电子工业发展协会</a>在1996年制定，版本为1.0。1998年，升级到2.1版，增加了对音频文件的支持。2002年3月，发表了2.2版。</p>
<p>Exif可以附加于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FJPEG" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/JPEG" ref="nofollow noopener noreferrer">JPEG</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FTIFF" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/TIFF" ref="nofollow noopener noreferrer">TIFF</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FRIFF" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/RIFF" ref="nofollow noopener noreferrer">RIFF</a>等文件之中，为其增加有关数码相机拍摄信息的内容和索引图或图像处理软件的版本信息。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FWindows_7" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/Windows_7" ref="nofollow noopener noreferrer">Windows 7</a>操作系统具备对Exif的原生支持，通过鼠标右键点击图片打开菜单，点击属性并切换到详细信息标签下即可直接查看Exif信息。</p>
<p>Exif信息是可以被任意编辑的，因此只有参考的功能。</p>
<p>Exif信息以0xFFE1作为开头标记，后两个字节表示Exif信息的长度。所以Exif信息最大为64 kB，而内部采用TIFF格式。</p>
<h2 data-id="heading-21">读写工具</h2>
<ul>
<li>
<p>Android:  androidx.exifinterface.media.ExifInterface  或者<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsephiroth74%2FAndroid-Exif-Extended" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sephiroth74/Android-Exif-Extended" ref="nofollow noopener noreferrer">Android-Exif-Extended</a></p>
</li>
<li>
<p>win/Mac: 命令行工具-可跨平台,跨语言使用:  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fexiftool%2Fexiftool" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/exiftool/exiftool" ref="nofollow noopener noreferrer">exiftool</a></p>
<p>题外话: 命令行工具的跨平台,跨语言使用</p>
<p>​              Mac/windows/linux  java,js,Python,c,c++</p>
<pre><code class="hljs language-java copyable" lang="java">Runtime runtime = Runtime.getRuntime();
Process process = runtime.exec(<span class="hljs-string">"cmd.exe /c dir d:\\"</span>);
<span class="hljs-comment">//exec(String command, String[] envp, File dir)</span>
InputStream inputStream = process.getInputStream();
BufferedReader br = <span class="hljs-keyword">new</span> BufferedReader(<span class="hljs-keyword">new</span> InputStreamReader(inputStream,<span class="hljs-string">"gb2312"</span>));
String line = <span class="hljs-keyword">null</span>;
<span class="hljs-keyword">while</span>((line = br.readLine()) != <span class="hljs-keyword">null</span>) &#123;
System.out.println(line);
&#125;

<span class="hljs-comment">//表现形式上,命令行工具接受的string[]参数,与java的main方法入口类似:</span>
在命令行: java -Xms128m -Xmx256m -jar xxx.<span class="hljs-function">jar 
  
<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(string[] args)</span></span>&#123;
  <span class="hljs-comment">//args: 可以拿到执行java命令时传入的各种参数,对这些参数做出一些处理.</span>
&#125;

<span class="hljs-comment">//用java包装命令行工具的方法: 将丰富的参数包装成builder模式</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<blockquote>
<p>python里读写exif而不改变图片数据区如何实现?</p>
</blockquote>
<p>思路: 先把整个文件拷过去,然后把exif读到内存,内存修改exif,再把修改后的exif写入到拷贝的文件中,这样就不会改变图片质量了.</p>
<p>不要用PIL,有坑,会改变图片质量</p>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-keyword">import</span> piexif
<span class="hljs-keyword">from</span> shutil <span class="hljs-keyword">import</span> copyfile
<span class="hljs-keyword">import</span> exifread

original = <span class="hljs-string">"IMG_20200628_111551.jpg"</span>
target = <span class="hljs-string">"IMG_20200628_111551-3.jpg"</span>
copyfile(original, target)

exif_dict = piexif.load(original)
exif_dict[<span class="hljs-string">"0th"</span>][piexif.ImageIFD.Copyright] = <span class="hljs-string">"lalalla----"</span>

piexif.insert(piexif.dump(exif_dict), target)

<span class="hljs-comment"># 打印</span>
f = <span class="hljs-built_in">open</span>(target, <span class="hljs-string">'rb'</span>)
tags = exifread.process_file(f)
<span class="hljs-built_in">print</span>(tags.__len__())
<span class="hljs-keyword">for</span> tag <span class="hljs-keyword">in</span> tags.keys():
    <span class="hljs-built_in">print</span>(<span class="hljs-string">" &#123;&#125;:  &#123;&#125;"</span>.<span class="hljs-built_in">format</span>(tag, tags[tag]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-22">代码库</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FskyNet2017%2FLuban" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/skyNet2017/Luban" ref="nofollow noopener noreferrer">luban2</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcoobird%2Fthumbnailator" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/coobird/thumbnailator" ref="nofollow noopener noreferrer">thumbnailator</a></p>
<h1 data-id="heading-23">一些应用</h1>
<p>app开发中,上传图片</p>
<p>typora写blog时,上传博客图片</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJuZiSang%2Fpicgo-plugin-compress" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JuZiSang/picgo-plugin-compress" ref="nofollow noopener noreferrer">github.com/JuZiSang/pi…</a></p>
<h1 data-id="heading-24">扩展阅读</h1>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-1208-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-1208-1-1.html" ref="nofollow noopener noreferrer"><strong>QQ音乐团队分享：Android中的图片压缩技术详解（上篇）</strong></a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-1212-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-1212-1-1.html" ref="nofollow noopener noreferrer"><strong>QQ音乐团队分享：Android中的图片压缩技术详解（下篇）</strong></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1359246" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/article/1359246" ref="nofollow noopener noreferrer">gif图像的压缩</a></p></div>  
</div>
            