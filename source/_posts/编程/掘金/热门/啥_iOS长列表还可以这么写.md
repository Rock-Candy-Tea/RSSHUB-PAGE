
---
title: '啥_iOS长列表还可以这么写'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a16ea36ded44225b8036f2ada97d3b9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 14 Mar 2021 22:44:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a16ea36ded44225b8036f2ada97d3b9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一般说,iOS界面的一些长列表,比如首页,活动页,长的会比较长,那么写起来总感觉没有那么优雅,那么如何才能做到优雅呢?
我在实践工作利用swift枚举的关联值和自定义组模型方法来实现了</p>
<ul>
<li>下面是gif图效果</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a16ea36ded44225b8036f2ada97d3b9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到,有些组是杂乱无章的排列着,而且运营那边要求,他们可以在后台自定义这些组的顺序
这可怎么办!🥺
下面看我的实现方式</p>
<h1 data-id="heading-0">定义一个组模型枚举</h1>
<ul>
<li>包含可能的定义,每个枚举关联当前组需要显示的数据模型,有可能是一个对象数组,也有可能是一个对象</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">/// 新版首页组cell的类型</span>
<span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">OriginGroupCellType</span> </span>&#123;
    <span class="hljs-keyword">case</span> marquee(list: [<span class="hljs-type">MarqueeModel</span>]) <span class="hljs-comment">// 跑马灯</span>
    <span class="hljs-keyword">case</span> beltAndRoad(list: [<span class="hljs-type">GlobalAdModel</span>]) <span class="hljs-comment">// 一带一路广告位</span>
    <span class="hljs-keyword">case</span> shoppingCarnival(list: [<span class="hljs-type">GlobalAdModel</span>]) <span class="hljs-comment">// 购物狂欢节</span>
    <span class="hljs-keyword">case</span> walletCard(smallWelfare: <span class="hljs-type">WelfareSmallResutlModel</span>) <span class="hljs-comment">// 钱包卡片</span>
    <span class="hljs-keyword">case</span> wallet(list: [<span class="hljs-type">HomeNavigationModel</span>]) <span class="hljs-comment">// 钱包cell</span>
    <span class="hljs-keyword">case</span> otc(list: [<span class="hljs-type">GlobalAdModel</span>]) <span class="hljs-comment">// OTC</span>
    <span class="hljs-keyword">case</span> hxPrefecture(list: [<span class="hljs-type">GlobalAdModel</span>]) <span class="hljs-comment">// HX商品专区</span>
    <span class="hljs-keyword">case</span> middleNav(list: [<span class="hljs-type">HomeNavigationModel</span>]) <span class="hljs-comment">// 中部导航</span>
    <span class="hljs-keyword">case</span> bottomNav(list: [<span class="hljs-type">HomeNavigationModel</span>]) <span class="hljs-comment">// 底部导航</span>
    <span class="hljs-keyword">case</span> broadcast(topSale: <span class="hljs-type">HomeNavigationModel</span>, hot: <span class="hljs-type">OriginBroadcastModel</span>, choiceness: <span class="hljs-type">OriginBroadcastModel</span>) <span class="hljs-comment">// 直播cell</span>
    <span class="hljs-keyword">case</span> middleAd(list: [<span class="hljs-type">GlobalAdModel</span>]) <span class="hljs-comment">// 中间广告cell</span>
    <span class="hljs-keyword">case</span> localService(list: [<span class="hljs-type">LocalServiceModel</span>]) <span class="hljs-comment">// 本地服务cell</span>
    <span class="hljs-keyword">case</span> bottomFloat(headerList: [<span class="hljs-type">OriginBottomFloatHeaderModel</span>]) <span class="hljs-comment">// 底部悬停cell</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>考虑到要下拉刷新等问题,可以这些枚举都得遵守<code>Equatable</code>协议</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift">  <span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">OriginGroupCellType</span>: <span class="hljs-title">Equatable</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">==</span> (<span class="hljs-params">lhs</span>: <span class="hljs-type">OriginGroupCellType</span>, <span class="hljs-params">rhs</span>: <span class="hljs-type">OriginGroupCellType</span>)</span> -> <span class="hljs-type">Bool</span> &#123;
        <span class="hljs-keyword">switch</span> (lhs, rhs) &#123;
        <span class="hljs-keyword">case</span> (.marquee, .marquee): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.beltAndRoad, .beltAndRoad): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.shoppingCarnival, .shoppingCarnival): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.walletCard, .walletCard): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.wallet, .wallet): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.otc, .otc): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.hxPrefecture, .hxPrefecture): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.middleNav, .middleNav): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.bottomNav, .bottomNav): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.broadcast, .broadcast): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.middleAd, .middleAd): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.localService, .localService): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">case</span> (.bottomFloat, .bottomFloat): <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">default</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">接下来就是组模型的定义</h1>
<ul>
<li>同时我抽取一个协议<code>GroupProvider</code>,方便复用</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">GroupProvider</span> </span>&#123;
    <span class="hljs-comment">/// 占位</span>
    <span class="hljs-keyword">associatedtype</span> <span class="hljs-type">GroupModel</span> <span class="hljs-keyword">where</span> <span class="hljs-type">GroupModel</span>: <span class="hljs-type">Equatable</span>
    
    <span class="hljs-comment">/// 是否需要往组模型列表中添加当前组模型</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">isNeedAppend</span>(<span class="hljs-params">with</span> <span class="hljs-params">current</span>: <span class="hljs-type">GroupModel</span>, <span class="hljs-params">listMs</span>: [<span class="hljs-type">GroupModel</span>])</span> -> <span class="hljs-type">Bool</span>
    <span class="hljs-comment">/// 获取当前组模型在组模型列表的下标</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">index</span>(<span class="hljs-params">with</span> <span class="hljs-params">current</span>: <span class="hljs-type">GroupModel</span>, <span class="hljs-params">listMs</span>: [<span class="hljs-type">GroupModel</span>])</span> -> <span class="hljs-type">Int</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">GroupProvider</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">isNeedAppend</span>(<span class="hljs-params">with</span> <span class="hljs-params">current</span>: <span class="hljs-type">GroupModel</span>, <span class="hljs-params">listMs</span>: [<span class="hljs-type">GroupModel</span>])</span> -> <span class="hljs-type">Bool</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-operator">!</span>listMs.contains(current)
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">index</span>(<span class="hljs-params">with</span> <span class="hljs-params">current</span>: <span class="hljs-type">GroupModel</span>, <span class="hljs-params">listMs</span>: [<span class="hljs-type">GroupModel</span>])</span> -> <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">return</span> listMs.firstIndex(of: current) <span class="hljs-operator">??</span> <span class="hljs-number">0</span>
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>OriginGroupModel,同样也遵守<code>Equatable</code>协议,防止重复添加</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addTo</span>(<span class="hljs-params">listMs</span>: <span class="hljs-keyword">inout</span> [<span class="hljs-type">OriginGroupModel</span>])</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这个方法是方便于下拉刷新时,替换最新数据所用</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">OriginGroupModel</span>: <span class="hljs-title">GroupProvider</span> </span>&#123;
    <span class="hljs-keyword">typealias</span> <span class="hljs-type">GroupModel</span> <span class="hljs-operator">=</span> <span class="hljs-type">OriginGroupModel</span>
    
    <span class="hljs-comment">/// 组模型的类型</span>
    <span class="hljs-keyword">var</span> cellType: <span class="hljs-type">OriginGroupCellType</span>
    <span class="hljs-comment">/// 排序</span>
    <span class="hljs-keyword">var</span> sortIndex: <span class="hljs-type">Int</span>

    <span class="hljs-comment">/// 把groupModel添加或替换到listMs中</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">addTo</span>(<span class="hljs-params">listMs</span>: <span class="hljs-keyword">inout</span> [<span class="hljs-type">OriginGroupModel</span>])</span> &#123;
        <span class="hljs-keyword">if</span> isNeedAppend(with: <span class="hljs-keyword">self</span>, listMs: listMs) &#123;
            listMs.append(<span class="hljs-keyword">self</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">let</span> index <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>.index(with: <span class="hljs-keyword">self</span>, listMs: listMs)
            listMs[index] <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>
        &#125;
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">OriginGroupModel</span>: <span class="hljs-title">Equatable</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">==</span> (<span class="hljs-params">lhs</span>: <span class="hljs-type">OriginGroupModel</span>, <span class="hljs-params">rhs</span>: <span class="hljs-type">OriginGroupModel</span>)</span> -> <span class="hljs-type">Bool</span> &#123;
        <span class="hljs-keyword">return</span> lhs.cellType <span class="hljs-operator">==</span> rhs.cellType
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>考虑要自定义顺序,所以需要定义一个排序的实体</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// MARK: - 新版首页组模型的排序规则模型</span>
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">OriginGroupSortModel</span> </span>&#123;
    <span class="hljs-comment">/// 搜索历史的排序</span>
    <span class="hljs-keyword">var</span> marqueeIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> beltAndRoadIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> shoppingCarnivalIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> walletCardIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> walletIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> otcIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> hxPrefectureIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> middleNavIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> bottomNavIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> broadcastIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> middleAdIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> localServiceIndex: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">var</span> bottomFloatIndex: <span class="hljs-type">Int</span>

    <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> defaultSort: <span class="hljs-type">OriginGroupSortModel</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-type">OriginGroupSortModel</span>(
            marqueeIndex: <span class="hljs-number">0</span>,
            beltAndRoadIndex: <span class="hljs-number">1</span>,
            shoppingCarnivalIndex: <span class="hljs-number">2</span>,
            walletCardIndex: <span class="hljs-number">3</span>,
            walletIndex: <span class="hljs-number">4</span>,
            otcIndex: <span class="hljs-number">5</span>,
            hxPrefectureIndex: <span class="hljs-number">6</span>,
            middleNavIndex: <span class="hljs-number">7</span>,
            bottomNavIndex: <span class="hljs-number">8</span>,
            broadcastIndex: <span class="hljs-number">9</span>,
            middleAdIndex: <span class="hljs-number">10</span>,
            localServiceIndex: <span class="hljs-number">11</span>,
            bottomFloatIndex: <span class="hljs-number">99</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">控制器里定义一个 组模型数组</h1>
<ul>
<li>这里有关键代码是</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift">listMs.sort(by: &#123; <span class="hljs-keyword">return</span> <span class="hljs-variable">$0</span>.sortIndex <span class="hljs-operator"><</span> <span class="hljs-variable">$1</span>.sortIndex &#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>所有的数据加载完毕后,会根据我们的自定义排序规则去排序</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift">    <span class="hljs-comment">/// 组模型数据</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">var</span> listMs: [<span class="hljs-type">OriginGroupModel</span>] <span class="hljs-operator">=</span> [] &#123;
        <span class="hljs-keyword">didSet</span> &#123;
            listMs.sort(by: &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-variable">$0</span>.sortIndex <span class="hljs-operator"><</span> <span class="hljs-variable">$1</span>.sortIndex
            &#125;)
            collectionView.reloadData()
        &#125;
    &#125;
    
    <span class="hljs-comment">/// 组模型排序规则(可以由后台配置返回,在这里我们先给一个默认值)</span>
    <span class="hljs-comment">/// 需要做一个请求依赖,先请求排序接口,再请求各组的数据</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">lazy</span> <span class="hljs-keyword">var</span> sortModel: <span class="hljs-type">OriginGroupSortModel</span> <span class="hljs-operator">=</span> <span class="hljs-type">OriginGroupSortModel</span>.defaultSort
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">网络请求代码</h1>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">loadData</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">update</span>: <span class="hljs-type">Bool</span> <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>, <span class="hljs-keyword">_</span> <span class="hljs-params">isUHead</span>: <span class="hljs-type">Bool</span> <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>)</span> &#123;
        <span class="hljs-comment">// 定义队列组</span>
        <span class="hljs-keyword">let</span> queue <span class="hljs-operator">=</span> <span class="hljs-type">DispatchQueue</span>.<span class="hljs-keyword">init</span>(label: <span class="hljs-string">"getOriginData"</span>)
        <span class="hljs-keyword">let</span> group <span class="hljs-operator">=</span> <span class="hljs-type">DispatchGroup</span>()
        
        <span class="hljs-comment">// MARK: - 文字跑马灯</span>
        group.enter()
        queue.async(group: group, execute: &#123;
            <span class="hljs-type">HomeNetworkService</span>.shared.getMarqueeList &#123; [<span class="hljs-keyword">weak</span> <span class="hljs-keyword">self</span>] (state, message, data) <span class="hljs-keyword">in</span>
                <span class="hljs-keyword">guard</span> <span class="hljs-keyword">let</span> `self` <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span> <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> &#125;
                <span class="hljs-keyword">self</span>.collectionView.uHead.endRefreshing()
                
                <span class="hljs-keyword">defer</span> &#123; group.leave() &#125;
                <span class="hljs-keyword">let</span> groupModel <span class="hljs-operator">=</span> <span class="hljs-type">OriginGroupModel</span>(cellType: .marquee(list: data), sortIndex: <span class="hljs-keyword">self</span>.sortModel.marqueeIndex)
                <span class="hljs-keyword">guard</span> <span class="hljs-operator">!</span>data.isEmpty <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> &#125;
                
                <span class="hljs-comment">/// 把groupModel添加到listMs中</span>
                groupModel.addTo(listMs: <span class="hljs-operator">&</span><span class="hljs-keyword">self</span>.listMs)
            &#125;
        &#125;)
        
        <span class="hljs-comment">/// .... 此处省略其它多个请求</span>

        group.notify(queue: queue) &#123;
            <span class="hljs-comment">// 队列中线程全部结束,刷新UI</span>
            <span class="hljs-type">DispatchQueue</span>.main.sync &#123; [<span class="hljs-keyword">weak</span> <span class="hljs-keyword">self</span>] <span class="hljs-keyword">in</span>
                <span class="hljs-keyword">self</span><span class="hljs-operator">?</span>.collectionView.reloadData()
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">collectionView的代理方法处理</h1>
<pre><code class="hljs language-swift copyable" lang="swift">    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">numberOfSections</span>(<span class="hljs-params">in</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>)</span> -> <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">return</span> listMs.count
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">numberOfItemsInSection</span> <span class="hljs-params">section</span>: <span class="hljs-type">Int</span>)</span> -> <span class="hljs-type">Int</span> &#123;
        <span class="hljs-keyword">let</span> groupModel <span class="hljs-operator">=</span> listMs[section]
        <span class="hljs-keyword">switch</span> groupModel.cellType &#123;
        <span class="hljs-keyword">case</span> .marquee, .beltAndRoad, .walletCard, .wallet, .otc, .hxPrefecture, .shoppingCarnival, .middleAd:
            <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
        <span class="hljs-keyword">case</span> .middleNav(<span class="hljs-keyword">let</span> list):
            <span class="hljs-keyword">return</span> list.count
        <span class="hljs-keyword">case</span> .bottomNav(<span class="hljs-keyword">let</span> list):
            <span class="hljs-keyword">return</span> list.count
        <span class="hljs-keyword">case</span> .broadcast:
            <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
        <span class="hljs-keyword">case</span> .localService(<span class="hljs-keyword">let</span> list):
            <span class="hljs-keyword">return</span> list.count
        <span class="hljs-keyword">case</span> .bottomFloat:
            <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>同理,collectionView的代理方法中,都是先拿到 cellType 来判断,达到精准定位, 举个<code>栗子</code></li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift">    <span class="hljs-comment">/// Cell大小</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">collectionView</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">collectionView</span>: <span class="hljs-type">UICollectionView</span>, <span class="hljs-params">layout</span> <span class="hljs-params">collectionViewLayout</span>: <span class="hljs-type">UICollectionViewLayout</span>, <span class="hljs-params">sizeForItemAt</span> <span class="hljs-params">indexPath</span>: <span class="hljs-type">IndexPath</span>)</span> -> <span class="hljs-type">CGSize</span> &#123;
        <span class="hljs-keyword">let</span> groupModel <span class="hljs-operator">=</span> listMs[indexPath.section]
        <span class="hljs-keyword">let</span> width <span class="hljs-operator">=</span> screenWidth <span class="hljs-operator">-</span> <span class="hljs-number">2</span> <span class="hljs-operator">*</span> margin
        <span class="hljs-keyword">switch</span> groupModel.cellType &#123;
        <span class="hljs-keyword">case</span> .marquee:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: screenWidth, height: <span class="hljs-number">32</span>)
        <span class="hljs-keyword">case</span> .beltAndRoad:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: width, height: <span class="hljs-number">46</span>)
        <span class="hljs-keyword">case</span> .walletCard:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: width, height: <span class="hljs-number">85</span>)
        <span class="hljs-keyword">case</span> .wallet:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: width, height: <span class="hljs-type">OriginWalletCell</span>.eachHeight <span class="hljs-operator">*</span> <span class="hljs-number">2</span> <span class="hljs-operator">+</span> <span class="hljs-number">10</span>)
        <span class="hljs-keyword">case</span> .otc, .hxPrefecture:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: width, height: <span class="hljs-number">60</span>)
        <span class="hljs-keyword">case</span> .middleNav:
            <span class="hljs-keyword">let</span> row: <span class="hljs-type">CGFloat</span> <span class="hljs-operator">=</span> <span class="hljs-number">5</span>
            <span class="hljs-keyword">let</span> totalWidth: <span class="hljs-type">CGFloat</span> <span class="hljs-operator">=</span> <span class="hljs-number">13</span> <span class="hljs-operator">*</span> (row <span class="hljs-operator">-</span> <span class="hljs-number">1</span>) <span class="hljs-operator">+</span> <span class="hljs-number">2</span> <span class="hljs-operator">*</span> margin
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: (screenWidth <span class="hljs-operator">-</span> totalWidth) <span class="hljs-operator">/</span> row, height: <span class="hljs-type">CGFloat</span>(<span class="hljs-number">98</span>.zh(<span class="hljs-number">80</span>).vi(<span class="hljs-number">108</span>)))
        <span class="hljs-keyword">case</span> .bottomNav:
            <span class="hljs-keyword">let</span> isFirstRow: <span class="hljs-type">Bool</span> <span class="hljs-operator">=</span> indexPath.item <span class="hljs-operator"><</span> <span class="hljs-number">2</span>
            <span class="hljs-keyword">let</span> row: <span class="hljs-type">CGFloat</span> <span class="hljs-operator">=</span> isFirstRow <span class="hljs-operator">?</span> <span class="hljs-number">2</span> : <span class="hljs-number">3</span>
            <span class="hljs-keyword">let</span> totalWidth: <span class="hljs-type">CGFloat</span> <span class="hljs-operator">=</span> <span class="hljs-number">4</span> <span class="hljs-operator">*</span> (row <span class="hljs-operator">-</span> <span class="hljs-number">1</span>) <span class="hljs-operator">+</span> <span class="hljs-number">2</span> <span class="hljs-operator">*</span> margin
            <span class="hljs-keyword">let</span> width <span class="hljs-operator">=</span> (screenWidth <span class="hljs-operator">-</span> totalWidth) <span class="hljs-operator">/</span> row
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: floor(<span class="hljs-type">Double</span>(width)), height: <span class="hljs-number">70</span>)
        <span class="hljs-keyword">case</span> .shoppingCarnival:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: width, height: <span class="hljs-number">150</span>)
        <span class="hljs-keyword">case</span> .broadcast:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: screenWidth <span class="hljs-operator">-</span> <span class="hljs-number">20</span>, height: <span class="hljs-number">114</span>)
        <span class="hljs-keyword">case</span> .middleAd:
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: width, height: <span class="hljs-number">114</span>)
        <span class="hljs-keyword">case</span> .localService:
            <span class="hljs-keyword">let</span> width <span class="hljs-operator">=</span> (<span class="hljs-number">82</span> <span class="hljs-operator">*</span> screenWidth) <span class="hljs-operator">/</span> <span class="hljs-number">375</span>
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: width, height: <span class="hljs-number">110</span>)
        <span class="hljs-keyword">case</span> .bottomFloat:
            <span class="hljs-keyword">let</span> h <span class="hljs-operator">=</span> bottomCellHeight <span class="hljs-operator">></span> <span class="hljs-type">OriginBottomH</span> <span class="hljs-operator">?</span> bottomCellHeight : <span class="hljs-type">OriginBottomH</span>
            <span class="hljs-keyword">return</span> <span class="hljs-type">CGSize</span>(width: screenWidth, height: h)
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">总结一下这种写法的优势</h1>
<ul>
<li>
<p>方便修改组和组之前的顺序问题,甚至可以由服务器下发顺序</p>
</li>
<li>
<p>方便删减组,只要把数据的添加组注释掉</p>
</li>
<li>
<p>用枚举的方式,定义每个组,更清晰,加上swift的关联值优势,可以不用在控制器里定义多个数组</p>
</li>
<li>
<p>考虑到要下拉刷新,所以抽取了一个协议 GroupProvider,里面提供两个默认的实现方法</p>
<ul>
<li>方法一:获取当前cellType在listMs中的下标</li>
<li>方法二:是否要添加到listMs中</li>
</ul>
</li>
<li>
<p>界面长什么样,全部由数据来驱动,这组没有数据,界面就对应的不显示(<code>皮之不存,毛将焉附</code>),有数据就按预先设计好的显示</p>
</li>
</ul>
<h1 data-id="heading-6">源码地址(源码内容和gif图中有差异,但是思路是一致的)</h1>
<p><a href="https://github.com/XYXiaoYuan/GroupModelTest" target="_blank" rel="nofollow noopener noreferrer">github.com/XYXiaoYuan/…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            