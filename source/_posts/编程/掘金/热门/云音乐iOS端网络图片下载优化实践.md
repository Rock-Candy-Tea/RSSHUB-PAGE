
---
title: '云音乐iOS端网络图片下载优化实践'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6.music.126.net/obj/wo3DlcOGw6DClTvDisK1/17349274858/6362/7dd6/3c53/f0f2e3af04d93be1baa652ccea09dc60.png'
author: 掘金
comments: false
date: Mon, 29 Aug 2022 01:19:07 GMT
thumbnail: 'https://p6.music.126.net/obj/wo3DlcOGw6DClTvDisK1/17349274858/6362/7dd6/3c53/f0f2e3af04d93be1baa652ccea09dc60.png'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>图片来自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Funsplash.com" target="_blank" rel="nofollow noopener noreferrer" title="https://unsplash.com" ref="nofollow noopener noreferrer">unsplash.com</a><br>
本文作者： lgq</p>
</blockquote>
<h2 data-id="heading-0">背景</h2>
<p>图片展示，在各大APP中不可或缺，众所周知云音乐是一款带有社交属性的音乐软件，那么在任何社交场景，都会有展示图片的诉求，并且常常会有重图片场景，比如一个云音乐中Mlog的Feed流场景全都是图片，或者就是Mlog中的图集，都需要展示大量的图片，要是图片无法及时的展示出来，不能及时的被用户消费，那么会造成用户浏览信息不顺畅，导致用户的流失，因此优化图片下载迫在眉睫。</p>
<h2 data-id="heading-1">现有图片下载技术</h2>
<p>这里简单了解下云音乐APP中接入的图片资源服务，它可以通过拼接参数，在远端进行裁剪，质量压缩从而下载到不同的图片。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsf.163.com%2Fhelp%2Fdocuments%2F66982522786074624" target="_blank" rel="nofollow noopener noreferrer" title="https://sf.163.com/help/documents/66982522786074624" ref="nofollow noopener noreferrer">更多信息参考</a></p>
<h2 data-id="heading-2">影响图片下载的因素</h2>
<ol>
<li>图片大小</li>
<li>网络情况</li>
<li>本地缓存</li>
<li>cdn缓存</li>
</ol>
<p>综上所述，如何提高图片的下载速度可以从上面几点开始优化。</p>
<h3 data-id="heading-3">优化方式</h3>
<h4 data-id="heading-4">网络优化</h4>
<ul>
<li>传统 HTTP1.0 的架构下没法多路复用，采用 HTTP2.0 的方式，请求同一ip域名的资源可以从节省大量建连及传输时间。</li>
<li>除此之外笔者在做音视频场景较重的页面时，发现音视频流媒体的数据有时候会抢占大量带宽，导致图片下载非常的慢，这时需要对音视频场景资源下载做适当的控制，如限流等操作，具体看业务优先级。如音视频场景使用socket下载时可以适当调中recv buffer 大小。</li>
</ul>
<h4 data-id="heading-5">图片大小优化</h4>
<ul>
<li>格式优化
这是最容易想的到的也是最有效的，如果正常使用jpg，png等常规图片，那图片的大小会是比较大的，目前我们的nos服务支持指定类型，将图片转成特定的格式，所以我们这里使用webp，从而减少图片的大小。（只需要在请求参数中拼接类型为webp即可）</li>
</ul>
<p><strong>那除此之外呢，我们还可以做一些什么？</strong></p>
<ul>
<li>
<p>按需裁剪
比如一个 100 * 100 的控件，3 倍屏的情况下，我们只需要下载 300 * 300 的图就可以了，如果图片超过个尺寸，我们去下载那么大的也没有意义。所以根据控件大小，可以决定我们下的图片大小，从而减小我们所需下载的图片。</p>
</li>
<li>
<p>压缩质量
比如要求没有那么高的场景我们只需要质量为 80 的图就可以了。</p>
</li>
</ul>
<p><strong>思考</strong>
以上几项做完，我们可以发现速度至少提升 30%，但是是不是可以做的更多，或者这个方案有什么纰漏？</p>
<p><strong>取证</strong>
为此我们简单的拉取了一下后台数据。发现有以下问题：</p>
<ol>
<li>URL拼接的参数不同，导致无法命中本地缓存，这样会有重复下载的问题，比如用户头像，用户头像再各个场景重复出现，而且大小不一，会下载多次这样会导致一定的资源浪费。同时由于链接参数各异 <strong>cdn命中度不高</strong></li>
<li>不同机型的UI尺寸大小可能不太一致，导致下载的片尺寸会不一样，机型种类越多，拼接的尺寸情况也越多，服务端需要重复裁剪。</li>
<li>质量参数由上层业务自行决定，会导致不同端没有约定好，下载到各式各样的图片</li>
</ol>
<p><strong>解决手段</strong></p>
<ol>
<li>URL 参数标准化
所谓的标准化是规范大前端使用的参数拼接，分为顺序标准化，参数值拟合。
我们知道一个下载图片的URL链接<code>http://path?imageView=1&enlarge=1&quality=80&thumbnail=80x80&type=webp</code>。</li>
</ol>
<ul>
<li>其中参数我们按首字母排序，这样在参数要求一致的情况下，不会出现重复请求。</li>
<li>thumbnail 参数其实对应的是需要下载的图片大小，我们做拟合（根据后端统计的到的数据），分成多档（档位可以配置），按照宽边对其等比例缩放，这样可以尽可能少的避免机型屏幕差一点点，出现了其他size的case。</li>
<li>quality也同样分级，分成多档（档位可以配置）。</li>
<li>去重，参数可能多拼接，对冗余参数去重复</li>
</ul>
<ol start="2">
<li>本地大小图片重用
简单理解是本地有大图，取小图的时候无需额外网络请求，直接本地裁剪。
我们优化了读取本地缓存的逻辑，在取缓存的时候，我们会进行关联查找，找到可用的图片进行裁剪，直接返回。
具体规则如下：</li>
</ol>
<ul>
<li>不同裁剪参数可以转化，x，z裁剪参数可以转为y，y不可以转x，z。都可以转为相同的裁剪参数。其中x（内缩略）,y（裁剪缩略）,z（外缩略）的含义在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsf.163.com%2Fhelp%2Fdocuments%2F66982522786074624" target="_blank" rel="nofollow noopener noreferrer" title="https://sf.163.com/help/documents/66982522786074624" ref="nofollow noopener noreferrer">本篇文档中有</a>，代表着不同的填充模式。</li>
<li>质量高的图片可以复用为质量低的图片，质量低的图片不可以复用为质量高的图片</li>
</ul>
<h2 data-id="heading-6">iOS 代码实现</h2>
<p>说完了方案之后，我们可以上代码了，这里是 iOS的实现方案：</p>
<p>首先我们是基于SDWebImage进行一定的封装，先简单了解下SDWebImage中大概的流程。</p>
<p><img src="https://p6.music.126.net/obj/wo3DlcOGw6DClTvDisK1/17349274858/6362/7dd6/3c53/f0f2e3af04d93be1baa652ccea09dc60.png" alt="SDWebImage原流程" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中我们可以看出，下载图片主要是使用了imageLoader，查找缓存这里是用了imageCache，这两个都在manager中被管理</p>
<h3 data-id="heading-7">改造流程</h3>
<p><img src="https://p6.music.126.net/obj/wo3DlcOGw6DClTvDisK1/17348449350/3720/6375/59d4/51fc59fd2a16ddf251a8e282644cdd38.png" alt="改造后的流程" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们只需要在数据流转的最开始对URL进行Fix，同时在查找缓存的时候对图片增加额外查找即可。</p>
<h3 data-id="heading-8">URL FIX</h3>
<p>我们给URL增加一个分类，对URL进行一个fix操作，方案就是用系统提供的 <code>NSURLComponts</code>对齐进行操作，提取出他的参数，进行去重，标准化，同时我们有一些历史原因，一些老的参数将其转为正确的格式，最后一步进行排序，fix流程就完成了。</p>
<pre><code class="hljs language-ini copyable" lang="ini">- (NSURL *)demo_fixImageURL &#123;

    NSURLComponts *<span class="hljs-attr">componts</span> = [NSURLComponts compontsWithURL:self
                                             resolvingAgainstBaseURL:<span class="hljs-literal">YES</span>]<span class="hljs-comment">;</span>
    NSMutableArray<NSURLQueryItem *> *<span class="hljs-attr">queryItems</span> = componts.queryItems.mutableCopy<span class="hljs-comment">;</span>

    ... 从URL取出 NSURLQueryItem 省略一些代码

    if (qualityItem) &#123;
        //quality 拟合， 将质量参数分为几档
        NSString *<span class="hljs-attr">defaultQualityStr</span> = @<span class="hljs-string">"39,69,89"</span><span class="hljs-comment">;</span>

        //这里是伪代码，就是为了获取配置信息
        NSArray<NSString *> *<span class="hljs-attr">qualityLevel</span> = CustomConfigQualityLevels<span class="hljs-comment">;</span>

        //固定 4档
        if (<span class="hljs-attr">qualityLevel.count</span> == <span class="hljs-number">3</span>) &#123;
            NSInteger <span class="hljs-attr">quality</span> = [qualityItem.value intValue]<span class="hljs-comment">;</span>
            NSString *<span class="hljs-attr">fixQuality</span> = @<span class="hljs-string">""</span><span class="hljs-comment">;</span>
            if (quality <= <span class="hljs-section">[[qualityLevel _objectAtIndex:0]</span> intValue]) &#123;
                <span class="hljs-attr">fixQuality</span> = [@(ImageQualityLevelLow) stringValue]<span class="hljs-comment">;</span>
            &#125; else if (quality <= <span class="hljs-section">[[qualityLevel _objectAtIndex:1]</span> intValue]) &#123;
                <span class="hljs-attr">fixQuality</span> = [@(ImageQualityLevelMed) stringValue]<span class="hljs-comment">;</span>
            &#125; else if (quality <= <span class="hljs-section">[[qualityLevel _objectAtIndex:2]</span> intValue]) &#123;
                <span class="hljs-attr">fixQuality</span> = [@(ImageQualityLevelHigh) stringValue]<span class="hljs-comment">;</span>
            &#125; else &#123;
                <span class="hljs-attr">fixQuality</span> = [@(ImageQualityLevelOrigin) stringValue]<span class="hljs-comment">;</span>
            &#125;
            NSURLQueryItem *<span class="hljs-attr">fixQualityItem</span> = [[NSURLQueryItem alloc] initWithName:@<span class="hljs-string">"quality"</span> value:fixQuality]<span class="hljs-comment">;</span>
            <span class="hljs-section">[queryItems removeObject:qualityItem]</span><span class="hljs-comment">;</span>
            <span class="hljs-section">[queryItems addObject:fixQualityItem]</span><span class="hljs-comment">;</span>
        &#125;
    &#125;

    if (sizeItem) &#123;
        //size 按照宽边拟合 分为几档且 等比缩放
        NSString *<span class="hljs-attr">defaultSizeStr</span> = @<span class="hljs-string">"30,60,90,120,180,256,315,512,720,1024"</span><span class="hljs-comment">;</span>

        //这里是伪代码 就是为了获取配置信息
        NSArray<NSString *> *<span class="hljs-attr">sizeLevels</span> = CustomConfigSizeLevels<span class="hljs-comment">;</span>
        NSString *<span class="hljs-attr">originSizeStr</span> = sizeItem.value<span class="hljs-comment">;</span>

        CGSize <span class="hljs-attr">originSize</span> = CGSizeZero<span class="hljs-comment">;</span>

        NSString *<span class="hljs-attr">separatedStr</span> = nil<span class="hljs-comment">;</span>
        for (NSString *separated in @<span class="hljs-section">[@"x", @"z", @"y"]</span>) &#123;
            NSArray *<span class="hljs-attr">sizeList</span> = [originSizeStr compontsSeparatedByString:separated]<span class="hljs-comment">;</span>
            if (<span class="hljs-attr">sizeList.count</span> == <span class="hljs-number">2</span>) &#123;
                <span class="hljs-attr">originSize</span> = CGSizeMake([sizeList[<span class="hljs-number">0</span>] intValue], [sizeList[<span class="hljs-number">1</span>] intValue])<span class="hljs-comment">;</span>
                <span class="hljs-attr">separatedStr</span> = separated<span class="hljs-comment">;</span>
                break<span class="hljs-comment">;</span>
            &#125;
        &#125;

        CGSize <span class="hljs-attr">finalSize</span> = CGSizeZero<span class="hljs-comment">;</span>
        if (!CGSizeEqualToSize(originSize, CGSizeZero)) &#123;
            BOOL <span class="hljs-attr">isW</span> = originSize.width > originSize.height<span class="hljs-comment">;</span>
            NSInteger <span class="hljs-attr">len</span> = isW ? originSize.width : originSize.height<span class="hljs-comment">;</span>
            NSInteger <span class="hljs-attr">requestSize</span> = <span class="hljs-number">0</span><span class="hljs-comment">;</span>
            for (NSString *sizeLevel in sizeLevels) &#123;
                NSInteger <span class="hljs-attr">sizeNumber</span> = [sizeLevel integerValue]<span class="hljs-comment">;</span>
                if (sizeNumber >= len) &#123;
                    if (<span class="hljs-attr">requestSize</span> == <span class="hljs-number">0</span>) &#123;
                        <span class="hljs-attr">requestSize</span> = sizeNumber<span class="hljs-comment">;</span>
                    &#125; else &#123;
                        <span class="hljs-attr">requestSize</span> = MIN(requestSize, sizeNumber)<span class="hljs-comment">;</span>
                    &#125;
                &#125;
            &#125;
            if (isW) &#123;
                if (originSize.width != 0) &#123;
                    NSInteger <span class="hljs-attr">h</span> = (requestSize / (originSize.width * <span class="hljs-number">1</span>.f)) * originSize.height<span class="hljs-comment">;</span>
                    <span class="hljs-attr">finalSize</span> = CGSizeMake(requestSize, floor(h))<span class="hljs-comment">;</span>
                &#125;

            &#125; else &#123;
                if (originSize.height != 0) &#123;
                    NSInteger <span class="hljs-attr">w</span> = (requestSize / (originSize.height * <span class="hljs-number">1</span>.f)) * originSize.width<span class="hljs-comment">;</span>
                    <span class="hljs-attr">finalSize</span> = CGSizeMake(w, floor(requestSize))<span class="hljs-comment">;</span>
                &#125;
            &#125;
        &#125;

        if (!CGSizeEqualToSize(finalSize, CGSizeZero)) &#123;
            NSString *<span class="hljs-attr">fixSize</span> = [NSString stringWithFormat:@<span class="hljs-string">"%ld%@%ld"</span>,(NSInteger)finalSize.width, separatedStr, (NSInteger)finalSize.height]<span class="hljs-comment">;</span>
            NSURLQueryItem *<span class="hljs-attr">fixSizeItem</span> = [[NSURLQueryItem alloc] initWithName:@<span class="hljs-string">"thumbnail"</span> value:fixSize]<span class="hljs-comment">;</span>
            <span class="hljs-section">[queryItems removeObject:sizeItem]</span><span class="hljs-comment">;</span>
            <span class="hljs-section">[queryItems addObject:fixSizeItem]</span><span class="hljs-comment">;</span>
        &#125;

    &#125;

    //去重复
    NSMutableArray<NSString *> *<span class="hljs-attr">keys</span> = @[].mutableCopy<span class="hljs-comment">;</span>
    <span class="hljs-attr">queryItems</span> = [queryItems bk_select:^BOOL(NSURLQueryItem *obj) &#123;
        BOOL containsObject = [keys containsObject:obj.name]<span class="hljs-comment">;</span>
        [keys addObject:obj.name]<span class="hljs-comment">;</span>
        return !containsObject<span class="hljs-comment">;</span>
    &#125;].mutableCopy<span class="hljs-comment">;</span>

    //首字母排序
    <span class="hljs-attr">queryItems</span> = [queryItems sortedArrayUsingComparator:^NSComparisonResult(NSURLQueryItem *obj1, NSURLQueryItem *obj2) &#123;
        return [obj1.name compare:obj2.name options:NSCaseInsensitiveSearch]<span class="hljs-comment">;</span>
    &#125;].mutableCopy<span class="hljs-comment">;</span>

    //最终组合
    <span class="hljs-attr">componts.queryItems</span> = queryItems.copy<span class="hljs-comment">;</span>
    NSURL *<span class="hljs-attr">finalURL</span> = componts.URL<span class="hljs-comment">;</span>

    return finalURL<span class="hljs-comment">;</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">SDWebImageManager</h3>
<p>修复了URL之后，下一步要做什么，如何将修复后的URL传递下去呢？也可以从上面的SDWebImage流程中看出，所有的图片下载流程，离不开SDWebImageManager，所以我们继承 <code>SDWebImageManager</code>，重写以下方法</p>
<pre><code class="hljs language-erlang copyable" lang="erlang">- <span class="hljs-params">(SDWebImageCombidOperation *)</span>loadImageWithURL:<span class="hljs-params">(nullable NSURL *)</span>url
                                          options:<span class="hljs-params">(SDWebImageOptions)</span>options
                                          context:<span class="hljs-params">(nullable SDWebImageContext *)</span>context
                                         progress:<span class="hljs-params">(nullable SDImageLoaderProgressBlock)</span>progressBlock
                                        completed:<span class="hljs-params">(nonnull SDInternalCompletionBlock)</span>completedBlock
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后续如果要走修复流程的只需要用我们封装好的manager即可，实现如果下</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (SDWebImageCombidOperation *)loadImageWithURL:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSURL</span> *)url
                                          options:(SDWebImageOptions)options
                                          context:(<span class="hljs-keyword">nullable</span> SDWebImageContext *)context
                                         progress:(<span class="hljs-keyword">nullable</span> SDImageLoaderProgressBlock)progressBlock
                                        completed:(<span class="hljs-keyword">nonnull</span> SDInternalCompletionBlock)completedBlock
                                         corp:(<span class="hljs-type">BOOL</span>)corp &#123;

    <span class="hljs-built_in">NSURL</span> *fixURL = [<span class="hljs-keyword">self</span>.class fixURLWithUrl:url];
    SDInternalCompletionBlock fixBlock = completedBlock;
    <span class="hljs-keyword">if</span> (![fixURL.absoluteString isEqualToString:url.absoluteString] && corp) &#123;
        fixBlock = [<span class="hljs-keyword">self</span>.class fixcompletedBlockWithOriginCompletedBlock:completedBlock url:url];
    &#125;
    <span class="hljs-keyword">return</span> [<span class="hljs-variable language_">super</span> loadImageWithURL:fixURL options:options context:context progress:progressBlock completed:^<span class="hljs-type">void</span>(<span class="hljs-built_in">UIImage</span> * _Nullable image, <span class="hljs-built_in">NSData</span> * _Nullable data, <span class="hljs-built_in">NSError</span> * _Nullable error, SDImageCacheType cacheType, <span class="hljs-type">BOOL</span> finished, <span class="hljs-built_in">NSURL</span> * _Nullable imageURL) &#123;

        <span class="hljs-keyword">if</span> (fixBlock) &#123;
            fixBlock(image,data,error,cacheType,finished,imageURL);
        &#125;
    &#125;];

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>细心的同学可以发现我们增加了一个参数 <code>corp</code>,如果上层业务就是需要按照他传入的大小来的话，我们做一层裁剪缩放操作。具体操作放在了<code>fixBlock</code>中。<strong>默认是不进行fix的，因为本身nos服务器下发的图片也不一定是业务传入希望的尺寸。</strong></p>
<p>fixblock 核心的代码是用了sd_webimage自带的裁剪</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-attr">cutImage</span> = [image sd_resizedImageWithSize:requestSize scaleMode:[urlInfo.cropStr isEqualToString:@<span class="hljs-string">"x"</span>] ? SDImageScaleModeAspectFit : SDImageScaleModeAspectFill]<span class="hljs-comment">;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码到这里基本<code>fixURL</code>操作基本完成，但是如果需要兼容老的缓存（本地已经有的，而且永久缓存（特殊case），但是线上已经下架的资源图片的），在fixblock中，我们在加载失败的情况下，用老的URL捞了一次本地缓存。</p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-attr">[[self sharedManager]</span> loadImageWithURL:url options:options | SDWebImageFromCacheOnly context:mutContext.copy progress:nil completed:completedBlock];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：<strong>已经fix过的URL不会再fix，是否是永久缓存是通过imageCache区分的</strong></p>
<p>SDWebImageFromCacheOnly 表示只从缓存了读取，避免了重复发请求的问题。</p>
<h3 data-id="heading-10">imageCache</h3>
<p>上面说到要实现复用，需要修改imageCache，这里不得不提以下SDWebImage找到缓存的流程</p>
<p><img src="https://p6.music.126.net/obj/wo3DlcOGw6DClTvDisK1/17348618635/91c4/dc86/66c4/521565f12d1e22cfc3ec64290c2c190e.png" alt="SDWebImage查询缓存" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，URL需要转为cacheKey，然后再从内存或者磁盘中捞出缓存。那么我们如何改造呢，因为我们需要通过URL找到本地可以重用的图片</p>
<p>cacheKey需要保留一定规则，通过cache可以看到原始URL的一些东西。所以我们cachekey是这么生成的</p>
<pre><code class="hljs language-ini copyable" lang="ini">+ (NSString *)cacheKeyForURL:(NSURL *)url  &#123;

    NSURL *<span class="hljs-attr">wUrl</span> = url<span class="hljs-comment">;</span>
    NSString *<span class="hljs-attr">host</span> = wUrl.host<span class="hljs-comment">;</span>
    NSString *<span class="hljs-attr">absoluteString</span> = wUrl.absoluteString<span class="hljs-comment">;</span>
    if (!host)
    &#123;
       return absoluteString<span class="hljs-comment">;</span>
    &#125;

    NSRange <span class="hljs-attr">hostRange</span> = [absoluteString rangeOfString:host]<span class="hljs-comment">;</span>
    if (hostRange.location + hostRange.length < absoluteString.length)
    &#123;
       NSString *<span class="hljs-attr">subString</span> = [absoluteString substringFromIndex:hostRange.location + hostRange.length]<span class="hljs-comment">;</span>
       if (subString.length != 0)
       &#123;
           return subString<span class="hljs-comment">;</span>
       &#125;
    &#125;
    return absoluteString<span class="hljs-comment">;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简而言之，就是去掉host，保留剩余的参数。<strong>ps：因为fixURL去过请求参数重复，所以cacheKey也能同一张图片保证唯一。</strong></p>
<p>那通过URL怎么找到本地的其他图片呢，如何关联上呢？</p>
<p><img src="https://p5.music.126.net/obj/wo3DlcOGw6DClTvDisK1/17348671494/d1a2/4464/fd97/a7fda682fb31f444077999b350054959.png" alt="cacheKey关联imageInfo" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以通过path，再查找关联的cachekey，然后找到对应的图片</p>
<p>找到图片后，选择出一张可以使用的，对其进行裁剪操作，流程如下：
<img src="https://p5.music.126.net/obj/wo3DlcOGw6DClTvDisK1/17348692528/e9dd/17cc/16c6/fb46a5bd17aad9f886c67c053812cb24.png" alt="裁剪流程" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们这里对缓存的图片信息封装了一个对象，注意 会用数据库持久化 <code>ImageCacheKeyAndURLObject</code>数组,他的key是请求URL链接中的 <code>path</code>，注意数据库有上限大小，同时会在适当的时机清理（如图片缓存过期等）</p>
<p>下面是封装持久化的对象</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">WebImageCacheImageInfo</span> : <span class="hljs-title">NSObject</span></span>

<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-type">BOOL</span> isAnimation;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">CGFloat</span> sizeW;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">CGFloat</span> sizeH;

- (<span class="hljs-built_in">CGSize</span>)size;

<span class="hljs-keyword">@end</span>

<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">WebImageURLInfo</span> : <span class="hljs-title">NSObject</span></span>

<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">CGSize</span> requestSize;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">NSString</span> *cropStr;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">NSInteger</span> quality;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">NSInteger</span> enlarge;

<span class="hljs-keyword">@end</span>

<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">WebImageCacheKeyAndURLObject</span> : <span class="hljs-title">NSObject</span><<span class="hljs-title">NMModel</span>></span>


<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">readonly</span>) <span class="hljs-built_in">NSString</span> *path;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>) <span class="hljs-built_in">NSString</span> *cacheKey;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">nullable</span>) <span class="hljs-built_in">NSURL</span> *url;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">nullable</span>) WebImageCacheImageInfo *imageInfo;

- (<span class="hljs-built_in">NSArray</span><WebImageCacheKeyAndURLObject *> *)relationObjects;
- (<span class="hljs-keyword">nullable</span> WebImageCacheKeyAndURLObject *)canReuseObject;
- (WebImageURLInfo *)urlInfo;
- (<span class="hljs-type">void</span>)storeImage:(<span class="hljs-built_in">UIImage</span> *)image;
- (<span class="hljs-type">void</span>)remove;
<span class="hljs-keyword">@end</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何存储图片信息呢</p>
<pre><code class="hljs language-ini copyable" lang="ini">- (void)storeImage:(UIImage *)image &#123;
    if (<span class="hljs-attr">self.path.length</span> == <span class="hljs-number">0</span>) &#123;
        return<span class="hljs-comment">;</span>
    &#125;
    BOOL <span class="hljs-attr">isAniamtion</span> = image.sd_isAnimated<span class="hljs-comment">;</span>
    CGSize <span class="hljs-attr">size</span> = image.size<span class="hljs-comment">;</span>
    if (image) &#123;
        <span class="hljs-attr">_imageInfo</span> = [WebImageCacheImageInfo new]<span class="hljs-comment">;</span>
        <span class="hljs-attr">_imageInfo.sizeH</span> = size.height<span class="hljs-comment">;</span>
        <span class="hljs-attr">_imageInfo.sizeW</span> = size.width<span class="hljs-comment">;</span>
        <span class="hljs-attr">_imageInfo.isAnimation</span> = isAniamtion<span class="hljs-comment">;</span>
    &#125;

    NSMutableArray<WebImageCacheKeyAndURLObject *> *<span class="hljs-attr">items</span> = [[self searchfromDBUsePath:self.path] mutableCopy]<span class="hljs-comment">;</span>
    if (<span class="hljs-attr">items.count</span> == <span class="hljs-number">0</span>) &#123;
        <span class="hljs-attr">items</span> = @[].mutableCopy<span class="hljs-comment">;</span>
    &#125;
    if (<span class="hljs-section">[items containsObject:self]</span>) &#123;
        <span class="hljs-section">[items removeObject:self]</span><span class="hljs-comment">;</span>
    &#125;
    <span class="hljs-section">[items addObject:self]</span><span class="hljs-comment">;</span>
    <span class="hljs-section">[self saveDBForPath:self.path item:items]</span><span class="hljs-comment">;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何判断图片是否可以复用呢？</p>
<pre><code class="hljs language-ini copyable" lang="ini">- (WebImageCacheKeyAndURLObject *)canReuseObject &#123;

    WebImageURLInfo *<span class="hljs-attr">info</span> = self.urlInfo<span class="hljs-comment">;</span>
    if (CGSizeEqualToSize(CGSizeZero, info.requestSize)) &#123;
        return nil<span class="hljs-comment">;</span>
    &#125;
    NSArray<WebImageCacheKeyAndURLObject *> *<span class="hljs-attr">relationObjects</span> = [self relationObjects]<span class="hljs-comment">;</span>

    // 非动图 尺寸非0

    <span class="hljs-attr">relationObjects</span> = [relationObjects bk_select:^BOOL(WebImageCacheKeyAndURLObject *obj) &#123;
        return !obj.imageInfo.isAnimation && obj.imageInfo.size.width > <span class="hljs-number">0</span> && obj.imageInfo.size.height > <span class="hljs-number">0</span><span class="hljs-comment">;</span>
    &#125;]<span class="hljs-comment">;</span>

    @weakify(self)
    <span class="hljs-attr">relationObjects</span> = [relationObjects bk_select:^BOOL(WebImageCacheKeyAndURLObject *obj) &#123;
        @strongify(self)
        return ![obj.cacheKey isEqualToString:self.cacheKey]<span class="hljs-comment">;</span>
    &#125;]<span class="hljs-comment">;</span>

    // 质量大于请求的图
    <span class="hljs-attr">relationObjects</span> = [relationObjects bk_select:^BOOL(WebImageCacheKeyAndURLObject *obj) &#123;

        WebImageURLInfo *objInfo = obj.urlInfo<span class="hljs-comment">;</span>

        NSInteger quality = objInfo.quality == <span class="hljs-number">0</span> ? <span class="hljs-number">75</span> : objInfo.quality<span class="hljs-comment">;</span>
        NSInteger requestQuality = info.quality == <span class="hljs-number">0</span> ? <span class="hljs-number">75</span> : info.quality<span class="hljs-comment">;</span>
        return quality >= requestQuality<span class="hljs-comment">;</span>
    &#125;]<span class="hljs-comment">;</span>

    //缩放能支持的
    NSArray<WebImageCacheKeyAndURLObject *> *<span class="hljs-attr">canUses</span> = nil<span class="hljs-comment">;</span>
    if (<span class="hljs-section">[info.cropStr isEqualToString:@"x"]</span> || <span class="hljs-section">[info.cropStr isEqualToString:@"z"]</span>) &#123;
        <span class="hljs-attr">canUses</span> = [relationObjects bk_select:^BOOL(WebImageCacheKeyAndURLObject *obj) &#123;
            WebImageURLInfo *objInfo = obj.urlInfo<span class="hljs-comment">;</span>
            if ([objInfo.cropStr isEqualToString:@<span class="hljs-string">"x"</span>] || [objInfo.cropStr isEqualToString:@<span class="hljs-string">"z"</span>]) &#123;
                CGSize displaySize = WebImageDisplaySizeForImageSizeContentSizeContentMode(obj.imageInfo.size, info.requestSize, [info.cropStr isEqualToString:@<span class="hljs-string">"x"</span>] ? UIViewContentModeScaleAspectFit :  UIViewContentModeScaleAspectFill)<span class="hljs-comment">;</span>

                CGFloat p = <span class="hljs-number">0</span><span class="hljs-comment">;</span>
                if (info.requestSize.width > <span class="hljs-number">0</span>) &#123;
                    p = displaySize.width / obj.imageInfo.size.width<span class="hljs-comment">;</span>
                &#125; else &#123;
                    p = displaySize.height / obj.imageInfo.size.height<span class="hljs-comment">;</span>
                &#125;
                return p <= <span class="hljs-number">1</span><span class="hljs-comment">;</span>
            &#125; else &#123;
                // y 不可以转z/x
                return <span class="hljs-literal">NO</span><span class="hljs-comment">;</span>
            &#125;
        &#125;]<span class="hljs-comment">;</span>
    &#125; else if (<span class="hljs-section">[info.cropStr isEqualToString:@"y"]</span>) &#123;
        <span class="hljs-attr">canUses</span> = [relationObjects bk_select:^BOOL(WebImageCacheKeyAndURLObject *obj) &#123;
            WebImageURLInfo *objInfo = obj.urlInfo<span class="hljs-comment">;</span>
            if ([objInfo.cropStr isEqualToString:@<span class="hljs-string">"x"</span>] || [objInfo.cropStr isEqualToString:@<span class="hljs-string">"z"</span>]) &#123;
                CGSize displaySize = WebImageDisplaySizeForImageSizeContentSizeContentMode(obj.imageInfo.size, info.requestSize, UIViewContentModeScaleAspectFill)<span class="hljs-comment">;</span>
                CGFloat p = <span class="hljs-number">0</span><span class="hljs-comment">;</span>
                if (info.requestSize.width > <span class="hljs-number">0</span>) &#123;
                    p = displaySize.width / obj.imageInfo.size.width<span class="hljs-comment">;</span>
                &#125; else &#123;
                    p = displaySize.height / obj.imageInfo.size.height<span class="hljs-comment">;</span>
                &#125;
                return p <= <span class="hljs-number">1</span><span class="hljs-comment">;</span>
            &#125; else  if ([objInfo.cropStr isEqualToString:@<span class="hljs-string">"y"</span>]) &#123;
                return (obj.imageInfo.size.width >= info.requestSize.width && obj.imageInfo.size.height >= info.requestSize.height)<span class="hljs-comment">;</span>
            &#125;
            return <span class="hljs-literal">NO</span><span class="hljs-comment">;</span>
        &#125;]<span class="hljs-comment">;</span>
    &#125;
    return canUses.firstObject<span class="hljs-comment">;</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>要过滤动图，因为动图本地裁剪比较难处理，而且占比不高，所以这里先忽略他，<code>WebImageCacheKeyAndURLObject</code>记录了<code>cacheKey</code>等一些关联信息，核心还记录了实际缓存的图片尺寸。方便查询。<code>WebImageDisplaySizeForImageSizeContentSizeContentMode</code>就是传入图片大小，容器大小，填充模式计算出缩放后的图片大小。</p>
<p>关联关系有了，再什么时机去查找呢？
我们继承SDImageCache，重写了他</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSData</span> *)diskImageDataBySearchingAllPathsForKey:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSString</span> *)key;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法，在找不到data的情况下更进一步查找。找到的关联图片进行裁剪，使用和上面一样的修正方法</p>
<pre><code class="hljs language-ini copyable" lang="ini">if (<span class="hljs-section">[objInfo.cropStr isEqualToString:@"x"]</span> || <span class="hljs-section">[objInfo.cropStr isEqualToString:@"z"]</span>) &#123;
                <span class="hljs-attr">result</span> = [result fixResizedImageWithSize:requestSize scaleMode:[objInfo.cropStr isEqualToString:@<span class="hljs-string">"x"</span>] ? UIViewContentModeScaleAspectFit : UIViewContentModeScaleAspectFill needCorp:<span class="hljs-literal">NO</span>]<span class="hljs-comment">;</span>
            &#125; else if (<span class="hljs-section">[objInfo.cropStr isEqualToString:@"y"]</span>) &#123;
                <span class="hljs-attr">result</span> = [result fixResizedImageWithSize:requestSize scaleMode:UIViewContentModeScaleAspectFill needCorp:<span class="hljs-literal">YES</span>]<span class="hljs-comment">;</span>
            &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里补充下fixsize方法</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-built_in">UIImage</span> *)fixResizedImageWithSize:(<span class="hljs-built_in">CGSize</span>)size scaleMode:(<span class="hljs-built_in">UIViewContentMode</span>)scaleMode needCorp:(<span class="hljs-type">BOOL</span>)needCorp &#123;

    <span class="hljs-keyword">if</span> (scaleMode != <span class="hljs-built_in">UIViewContentModeScaleAspectFit</span> && scaleMode!= <span class="hljs-built_in">UIViewContentModeScaleAspectFill</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">self</span>;
    &#125;

    <span class="hljs-comment">// 如果是fill模式，实际size会大于容器size 如果需要裁剪为容器大小就不走这一步了</span>
    <span class="hljs-keyword">if</span> (scaleMode == <span class="hljs-built_in">UIViewContentModeScaleAspectFill</span> && !needCorp) &#123;
        size = WebImageDisplaySizeForImageSizeContentSizeContentMode(<span class="hljs-keyword">self</span>.size, size, scaleMode);
    &#125;

    <span class="hljs-built_in">UIImage</span> *fixImage = [<span class="hljs-keyword">self</span> sd_resizedImageWithSize:size scaleMode:scaleMode == <span class="hljs-built_in">UIViewContentModeScaleAspectFit</span> ? SDImageScaleModeAspectFit : SDImageScaleModeAspectFill];
    <span class="hljs-keyword">return</span> fixImage;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就可以得到修复后的图片，流程完成。</p>
<h3 data-id="heading-11">UIImageView 及 UIButton 等分类</h3>
<p>我们包装一层自己的下载，然后传入我们的manager即可。</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-attr">context</span> = @&#123;
           SDWebImageContextCustomManager:<span class="hljs-section">[WebImageManager sharedManager]</span>
       &#125;<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">额外说一点</h3>
<p>CDN命中率和这个资源是否曾经被请求过有关，命中CDN的key又是请求的URL，所以大前端请求都保持一致的规则很重要！这样每一端都可以蹭到其他端预热过的图片资源。</p>
<h3 data-id="heading-13">总结</h3>
<p>我们核心点就<code>修正了URL</code>改造了<code>SDWebImageManager</code>,<code>SDImageCache</code>,并且建立了<code>CacheKey</code>关联关系，并且<code>兼容一些老逻辑</code>这样本地流程就都算走通了。本文除了常规优化图片的思路外提供了一种新的思路，本地利用已经下载过的大小图做文章，从而起到加速及节流的效果，并取得一定的收益，如果读者也是采用类似拼接url下载图片的方式的话，这种优化方式可以一试。全部做完取得成果具体数值不便展示，大概为提升下载速度 50%，同时能节省一定的 CDN带宽，日均节约至少 10% 。</p>
<blockquote>
<p>本文发布自网易云音乐技术团队，文章未经授权禁止任何形式的转载。我们常年招收各类技术岗位，如果你准备换工作，又恰好喜欢云音乐，那就加入我们 grp.music-fe(at)corp.netease.com！</p>
</blockquote></div>  
</div>
            