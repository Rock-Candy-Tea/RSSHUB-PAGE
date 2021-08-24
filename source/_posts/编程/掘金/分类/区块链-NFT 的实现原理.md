
---
title: '区块链-NFT 的实现原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=191'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 16:17:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=191'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：林冠宏 / 指尖下的幽灵。转载者，请: 务必标明出处。</p>
</blockquote>
<blockquote>
<p>掘金：<a href="https://juejin.im/user/1785262612681997" target="_blank" title="https://juejin.im/user/1785262612681997">juejin.im/user/178526…</a></p>
</blockquote>
<blockquote>
<p>博客：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cnblogs.com%2Flinguanh%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cnblogs.com/linguanh/" ref="nofollow noopener noreferrer">www.cnblogs.com/linguanh/</a></p>
</blockquote>
<blockquote>
<p>GitHub ： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faf913337456%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/af913337456/" ref="nofollow noopener noreferrer">github.com/af913337456…</a></p>
</blockquote>
<blockquote>
<p>出版的书籍：</p>
</blockquote>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fitem.jd.com%2F12652730.html" target="_blank" rel="nofollow noopener noreferrer" title="https://item.jd.com/12652730.html" ref="nofollow noopener noreferrer">《1.0-区块链以太坊DApp开发实战》</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fitem.jd.com%2F13002444.html" target="_blank" rel="nofollow noopener noreferrer" title="https://item.jd.com/13002444.html" ref="nofollow noopener noreferrer">《2.0-区块链DApp开发：基于以太坊和比特币公链》</a></li>
</ul>
<hr>
<h2 data-id="heading-0">目录</h2>
<ul>
<li>第一步: 制作id
<ul>
<li>如何操作？</li>
<li>获取图片的唯一id</li>
<li>获取衣服的唯一id</li>
</ul>
</li>
<li>第二步：通证化
<ul>
<li>基于不同公链的流程</li>
<li>NFT 的智能合约</li>
</ul>
</li>
<li>第三步：展示与修改
<ul>
<li>展示 NFT 内容</li>
<li>修改 NFT 内容</li>
</ul>
</li>
<li>所有权共识</li>
<li>第三方平台</li>
</ul>
<hr>
<blockquote>
<p>NFT (Non-Fungible Token)，这2年又火了起来，早在18年已经火过一波。</p>
</blockquote>
<p>本文只从<code>写代码实现NFT的技术方案</code>层面去介绍 NFT，不从其金融意义、案例，等层面去谈，因为这类内容可以随便在浏览器搜索到，而我接下来要谈的内容，浅层搜索下，数量不多。</p>
<h3 data-id="heading-1">第一步: 制作id</h3>
<p>制作id，这是把物质制作成 NFT 的第一步。物质有哪些？一段文字、一张图片，一件衣服等，夸张的说，现实世界的物质，无论是虚拟的(游戏装备)或实质物质，都可以被通证化。</p>
<h4 data-id="heading-2">如何操作？</h4>
<p>通过<code>第三方技术手段</code>获取物质的唯一标志性中间产物。</p>
<p>因此制作 NFT 第一步，广义于下面等式：</p>
<ul>
<li>id = F(I)
<ol>
<li>I = 输入的物质</li>
<li>F = 处理函数，代表一种方法</li>
<li>id 唯一标志性的中间产物</li>
</ol>
</li>
</ul>
<p>最简单的例子就是哈希函数，不考虑哈希碰撞，它就可以根据不同的内容输出不同的哈希值。<code>思维在这里不要局限于哈希函数。</code></p>
<h4 data-id="heading-3">获取图片的唯一id</h4>
<p>这里用图片代表一系列的文件类数据。</p>
<ol>
<li>我们可以将图片转换成 []byte 字节数组，然后计算其哈希值。这种操作虽然比较简单，但是图片别人却不能访问，看不到；</li>
<li>如果我们想向外部任何人提供图片的读权限，在计算完 id 后，有两种做法：
<ol>
<li>上传图片到文件服务器，任何人可以通过 url 链接访问。这里的服务器是中心化的；</li>
<li>增加区块链属性。上传文件到 IPFS (ipfs是什么，自行搜索)，如此一来，文件别人能访问，同时还具备了区块链的去中心化等属性。其中 IPFS 会在上传完文件后，会使用它的算法，帮你计算好哈希值返回，可以直接用它的作为id。</li>
</ol>
</li>
</ol>
<h4 data-id="heading-4">获取衣服的唯一id</h4>
<p>这里用衣服来代表一系列的实际物质。如果获取它们的唯一id呢？做法可以放飞思维去思考，比如可以：</p>
<ul>
<li>衣服的出厂信息、扫描内容、照片，等系列关于它的信息，数据化，然后用这些数据制作成文件，最后参考图片的做法。</li>
</ul>
<h3 data-id="heading-5">第二步：通证化</h3>
<p>第一步中获取了物质的id，现在要把它们通证化。切记一点：目前公认的 NFT 都是基于区块链公链的，那么以后是不是会一直这样呢？不一定，说不准出来了新的共识。</p>
<h4 data-id="heading-6">基于不同公链的流程</h4>
<p>通证化的流程如下：</p>
<ol>
<li>选择一条区块链公链。这里的选择会决定后面<code>智能合约</code>等系统组件的技术栈，这一点很核心；</li>
<li>在所选的公链上开发智能合约；</li>
<li>所开发的智能合约需要遵循一些基础约定，比如至少能保证物质的id能达到验证去重，什么意思呢？意思是，如果 A 在今天上传了 id=1 到链上，明天 B 也上传同个 id=1 到链上，合约要能告诉 B，你不能上传了，id 已经存在；</li>
<li>部署智能合约到链上，此时它变成 DApp；</li>
<li>通过发交易的方式，调用该智能合约的方法，将id等相关数据存储到链上。</li>
</ol>
<h4 data-id="heading-7">NFT 的智能合约</h4>
<p>NFT 智能合约可以基于不同的公链开发，它不局限于任何一条公链。不同公链的智能合约方案实现也不同，下面以 以太坊 公链举例说明。</p>
<p>在以太坊上面，开发 NFT 智能合约，已经有很多标准，比如 ERC-721 \1155 \998，各有各的特点，但它们的特点是在基础属性上拓展而来的。(各标准文档: <a target="_blank" href="https://link.juejin.cn/?target=https%3A%2F%2Feips.ethereum.org%2FEIPS%2Feip-721" rel="nofollow noopener noreferrer" title="https://eips.ethereum.org/EIPS/eip-721" ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=https%3A%2F%2Feips.ethereum.org%2FEIPS%2Feip-721" target="_blank" rel="nofollow noopener noreferrer" title="https://eips.ethereum.org/EIPS/eip-721" ref="nofollow noopener noreferrer">eips.ethereum.org/EIPS/eip-72…</a>)</p>
<p>如果选择 ERC-721 标准开发 NFT 智能合约，在元数据存储部分，就有 tokenUrl 这项，它相当于物质的唯一id，像下面的样子, <code>_tokenURIs</code> 存储的就是通证当前计数id与其对应的 tokenUrl，这里的tokenUrl 是字符串格式，一般是文件url，存储在 IPFS 或其他服务上面的文件的链接，但不局限于链接，也可以是其它的内容。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 伪代码</span>
contract MyERC721 is IERC721Metadata, ... &#123;
    ...
    mapping(<span class="hljs-function"><span class="hljs-params">uint256</span> =></span> address) private _tokenOwner;
    mapping(<span class="hljs-function"><span class="hljs-params">uint256</span> =></span> string) private _tokenURIs;
    
    uint256 public tokenCounter; <span class="hljs-comment">// 计数，当前总的 NFT 的数量，累增</span>
    
    <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) <span class="hljs-title">public</span> <span class="hljs-title">ERC721</span> (<span class="hljs-params"><span class="hljs-string">"name"</span>, <span class="hljs-string">"symbol"</span></span>)&#123;
        tokenCounter = <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-comment">// 外部调用方，调用这个函数，传参数：tokenURI 即物质的id，tokenURI 唯一</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createNFT</span>(<span class="hljs-params">string memory tokenURI</span>) <span class="hljs-title">public</span> <span class="hljs-title">returns</span> (<span class="hljs-params">uint256</span>) </span>&#123;
        uint256 tokenId = tokenCounter;
        _mint(msg.sender, tokenId); <span class="hljs-comment">// 将交易发送者和当前的 tokenId 绑定</span>
        _setTokenURI(tokenId, tokenURI); <span class="hljs-comment">// tokenId 映射到 tokenUrl</span>
        tokenCounter = tokenCounter + <span class="hljs-number">1</span>; <span class="hljs-comment">// 累加</span>
        <span class="hljs-keyword">return</span> tokenId;
    &#125;
    <span class="hljs-comment">// _exists 函数判断 tokenId 是否存在，_tokenOwner[tokenId]</span>
    <span class="hljs-comment">// 根据 id 读取对应的 url</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tokenURI</span>(<span class="hljs-params">uint256 tokenId</span>) <span class="hljs-title">external</span> <span class="hljs-title">view</span> <span class="hljs-title">returns</span> (<span class="hljs-params">string memory</span>) </span>&#123;
        <span class="hljs-built_in">require</span>(_exists(tokenId));
        <span class="hljs-keyword">return</span> _tokenURIs[tokenId];
    &#125;
    <span class="hljs-comment">// 根据 tokenId 和 url 建立 map 数据关系</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_setTokenURI</span>(<span class="hljs-params">uint256 tokenId, string memory uri</span>) <span class="hljs-title">internal</span> </span>&#123;
        <span class="hljs-built_in">require</span>(_exists(tokenId)); <span class="hljs-comment">// _exists</span>
        _tokenURIs[tokenId] = uri;
    &#125;
    ... <span class="hljs-comment">// 省略系列接口，包含读接口</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 tokenUrl 是标准要求的存储数据项。整个合约具备下面约束功能：</p>
<ol>
<li>NFT 持有者，即 msg.sender(owner) 和 tokenId 一对多关系，代表一个人可以拥有多个 NFT；</li>
<li>tokenId 和 tokenUrl 一对一关系，代表每份数据一个链上的唯一id，同时 tokenUrl 没要求是唯一，但在调用方，一般会把 tokenUrl 设置唯一，即使不唯一也没关系，冲突的时候，tokenId 越小的，其当初被设置的时间就越早；</li>
<li>NFT 持有者在将数据写入链上后，能够获取 NFT 的链上唯一 id，后续可以根据 id 进行系列的读写操作。</li>
</ol>
<p>一般来说，我们常规的 NFT 有一个和数据建立关系的项就足够了，但并不局限于此，合约在实现了标准要求的接口后，完全<code>可以自己添加自定义数据项及其读写函数。</code></p>
<h3 data-id="heading-8">第三步：展示与修改</h3>
<h4 data-id="heading-9">展示 NFT 内容</h4>
<p>所谓展示，就是对 NFT 的数据进行读取再展示。一般的流程如下：</p>
<ol>
<li>根据当初设置 NFT 数据到链上时获得的 id 去智能合约读取信息；</li>
<li>将获得的信息通过某介质应用还原出原始的 NFT 数据。</li>
</ol>
<p>比如将图片 NFT 展示出。(借助上面的 721 合约标准和 IPFS 结合为例)</p>
<ol>
<li>假设调用合约存储数据时候得到的 tokenId 是 3，那么使用这个 tokenId 去调用合约的读数据方法；</li>
<li>执行完 1 步骤，可以得到 tokenUrl，即文件存储在 IPFS 中所得到的链接；</li>
<li>直接将 tokenUrl 链接在浏览器打开，看到图片。</li>
</ol>
<h4 data-id="heading-10">修改 NFT 内容</h4>
<p>修改是一项 NFT 智能合约的拓展功能，可有可无，具体是怎样的方式，完全看需求的实现。比如：</p>
<ol>
<li>允许重置 tokenId 所对应的内容；</li>
<li>在 NFT 原数据中增加其他字段内容，再允许修改这些字段；</li>
<li>转让 NFT，可以把某 tokenId 对应的 NFT 信息转让给其他 owner，达到转让目的；</li>
<li><code>出售 NFT</code>、<code>拍卖 NFT</code> 等操作....</li>
</ol>
<h3 data-id="heading-11">所有权共识</h3>
<p>目前 NFT，非同质化通证。本质是想借助区块链的属性来标示一种资产的所有权证明。</p>
<p>比如曾拍卖出6000多万美金的数字作品(图片)《Everydays: The First 5000 Days》，中标者能获得原图 和 该图的 NFT。这两样东西，一样是实质的作品，一样是它的所有权者的证明。</p>
<p>我们假设下，如果持有某作品的人，是一位匿名者A，过了多年后，该作品本身不小心被盗并被找回。那么如何证明 A 是真正的拥有者，此时 A 只需要展示他对该作品的 NFT 拥有权，就可以证明。</p>
<p>那么 NFT 是不是类似于我们现实中的证书？不全是，分两点：</p>
<ol>
<li>NFT 和证书都能证明某资产的所有权；</li>
<li>对比的存储介质 与 永恒时效：
<ol>
<li>证书可能要找个保险柜保养放着，但它终究占据一方土地，仅受一方土地容纳的保险柜保证安全，在时过境迁的影响下，持续性存储下去的时间会较短；</li>
<li>NFT 存储在区块链上，受整个互联网的链节点所保护。它能够存活到整个链网络垮掉那天，对于节点数量众多的公链来说，这个概率几乎等同于互联网终结那天。</li>
</ol>
</li>
</ol>
<h3 data-id="heading-12">第三方平台</h3>
<p>现在已经有很多的第三方的 NFT 制作与发布平台。比如 opensea、rarible 等，这些平台自己实现了 NFT 的智能合约 和 NFT 展示应用(介质应用---网站)，方便大众 0 代码基础体会 NFT。但也有一些门槛，需要具备钱包和发交易的油费。</p></div>  
</div>
            