
---
title: '基于 TuGraph Explore 挖掘网络黑灰产子图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9156fcc80d481b8725faaf4a736e0c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 03:35:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9156fcc80d481b8725faaf4a736e0c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>🙋🏻‍♀️ 编者按：TuGraph Explore 是基于 GraphInsight 为 TuGraph 打造的图探索分析平台，并随着 9 月 1 日 TuGraph 开源一起对外服务。本文作者是蚂蚁集团前端工程师聚则，记录了基于 TuGraph Explore ，在黑灰产网络资产图谱数据集中分别挖掘出具体的网络资产子图，识别子图中的核心网络资产和关键链路，并详细阐述黑灰产团伙网络运作机制，欢迎查阅～</p>
<p>*本文中使用的案例和数据来源于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fchinavis.org%2F2022%2Fchallenge.html" target="_blank" rel="nofollow noopener noreferrer" title="https://chinavis.org/2022/challenge.html" ref="nofollow noopener noreferrer">ChinaVis 挑战赛「数据安全可视分析」</a>。</p>
</blockquote>
<h3 data-id="heading-0">背景</h3>
<p>网络黑灰产是指利用信息技术和网络技术，实施各类违法犯罪活动来谋取不正当利益的产业形态。目前，在互联网运行的内容秩序威胁型黑灰产是最常见网络黑灰产类型，它们以公开网站为载体来传播违法违规内容，开展网络诈骗、网络赌博、网络色情、违禁品交易等犯罪活动，严重侵害网络生态的健康发展，甚至威胁着网民生命财产安全。</p>
<p>近年来，黄赌毒诈等黑灰产团伙的网络化运作严重破坏着网络生态和社会治安，是执法部门的重拳打击对象。一个黑灰产团伙需要掌握一定数量且相互关联的网络资产，比如：域名、IP地址、安全证书等，才能支撑业务的网络化运作。分析黑灰产团伙掌握的网络资产及其关联关系，有利于理解黑灰产团伙的业务运作机制、识别核心网络资产和关键资产链路、挖掘真实世界的嫌疑人信息、制定有效的打击策略。</p>
<h3 data-id="heading-1">目标</h3>
<p>基于警方提供的关键线索，在黑灰产网络资产图谱数据集中分别<strong>挖掘出具体的网络资产子图</strong>，识别子图中的<strong>核心网络资产和关键链路</strong>，并详细阐述黑灰产团伙网络<strong>运作机制</strong>。
线索数据如下表所示。</p>























<table><thead><tr><th>黑灰产团伙</th><th>节点 id</th><th>节点 name</th><th>节点类型</th></tr></thead><tbody><tr><td>团伙</td><td>Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9</td><td><strong>c58c149eec.com</strong></td><td>Domain</td></tr><tr><td></td><td>Domain_f3554b666038baffa5814c319d3053ee2c2eb30d31d0ef509a1a463386b69845</td><td><strong>f3554b6660.com</strong></td><td>Domain</td></tr></tbody></table>
<h3 data-id="heading-2">演示视频</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1VP411V7kN%3Fspm_id_from%3D333.999.0.0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1VP411V7kN?spm_id_from=333.999.0.0" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1VP…</a></p>
<h3 data-id="heading-3">创建子图</h3>
<p>在 TuGraph console 中点击创建子图，如下图所示。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9156fcc80d481b8725faaf4a736e0c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
输入子图名称及描述信息，创建新的子图。</p>
<h3 data-id="heading-4">数据建模</h3>
<h4 data-id="heading-5">创建顶点</h4>
<p>切换到新创建的 TuGraphExplore 子图上，点击「顶点标签」按钮，添加顶点标签，如下图所示。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47dddb90ad1d4f9293ed05fc793cd14c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
填写顶点标签名称、属性及指定主键，即可完成顶点的创建。按照上述方法，分别创建 Domain、IP、ASN、Cert 等 8 类节点。</p>
<h4 data-id="heading-6">创建边</h4>
<p>点击「关系标签」，添加边标签。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a81bfa3ea3c24dc685e2e178a8b37396~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
填写边标签名称、起始标签及属性，即可完成边的创建。</p>
<p>填写完点边信息后，创建如下的图模型。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2810e2eea394956a1845ada88ea04ed~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述建模过程操作起来比较繁琐，您可以点击下载下面的 Schema 文件，然后通过「导入模型」的方式快速创建模型。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjson%2F2511393%2F1662549685678-7656e8a8-5455-4776-ac64-8d0de9b10f3f.json%3F_lake_card%3D%257B%2522src%2522%253A%2522https%253A%252F%252Fwww.yuque.com%252Fattachments%252Fyuque%252F0%252F2022%252Fjson%252F2511393%252F1662549685678-7656e8a8-5455-4776-ac64-8d0de9b10f3f.json%2522%252C%2522name%2522%253A%2522TuGraphExplore_schema.json%2522%252C%2522size%2522%253A3672%252C%2522type%2522%253A%2522application%252Fjson%2522%252C%2522ext%2522%253A%2522json%2522%252C%2522source%2522%253A%2522%2522%252C%2522status%2522%253A%2522done%2522%252C%2522download%2522%253Atrue%252C%2522taskId%2522%253A%2522ua202f727-8d8f-4138-ae41-25400b20dc8%2522%252C%2522taskType%2522%253A%2522upload%2522%252C%2522__spacing%2522%253A%2522both%2522%252C%2522id%2522%253A%2522u962e5927%2522%252C%2522margin%2522%253A%257B%2522top%2522%253Atrue%252C%2522bottom%2522%253Atrue%257D%252C%2522card%2522%253A%2522file%2522%257D" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/attachments/yuque/0/2022/json/2511393/1662549685678-7656e8a8-5455-4776-ac64-8d0de9b10f3f.json?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjson%2F2511393%2F1662549685678-7656e8a8-5455-4776-ac64-8d0de9b10f3f.json%22%2C%22name%22%3A%22TuGraphExplore_schema.json%22%2C%22size%22%3A3672%2C%22type%22%3A%22application%2Fjson%22%2C%22ext%22%3A%22json%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22ua202f727-8d8f-4138-ae41-25400b20dc8%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22u962e5927%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D" ref="nofollow noopener noreferrer">TuGraphExplore_schema.json</a></p>
<h3 data-id="heading-7">数据导入</h3>
<p>点击「文件导入」按钮，选择要导入的文件，选择标签和点类型，然后点击「开始映射」，配置具体的对应关系，如下图所示。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9de5dbf8b81a4b47b8615cac70dbd0fe~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
配置完属性映射以后，点击「映射」按钮完成映射，开始导入数据。
注意 选择从第 2 行开始导入，表头不需要导进去。</p>
<p>按照上面的步骤，依次完成 Domain、IP、IP_C、Cert 等节点文件的导入。</p>
<p>开始导入边文件，和点文件相比，点文件有两处不同：</p>
<ul>
<li>需要指定起点和终点列；</li>
<li>需要指定起点和终点类型。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dd458fc69d6409692477f27d48cf49a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有点边文件都导入成功以后，就可以根据提供的线索进行图探索分析了。</p>
<h3 data-id="heading-8">探索分析</h3>
<h4 data-id="heading-9">查询数据</h4>
<p><strong>按指定的 ID 查询</strong></p>
<pre><code class="hljs language-groovy copyable" lang="groovy">// 查询指定 ID 的节点
MATCH (n:Domain) 
WHERE n.id='Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9' 
RETURN n

// 查询多个节点
MATCH (n:Domain) 
WHERE n.id in ['Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9','Domain_f3554b666038baffa5814c319d3053ee2c2eb30d31d0ef509a1a463386b69845'] 
RETURN n
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据给定线索，使用以上 Cypher 语句查询（通过输入给定线索 ID 进行查询），通过「样式配置」资产，选择 name 作为节点显示的 label，得到两个具体的点  c58c149eec.com 和  f3554b6660.com 。</p>
<h4 data-id="heading-10">关系扩散</h4>
<p><strong>针对查询到的节点做关系扩散</strong></p>
<pre><code class="hljs language-groovy copyable" lang="groovy">MATCH (n)-[*..1]-(m) 
WHERE id(n)='Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9' 
return n, m

// 查询多个节点的一度关系
MATCH (n)-[*..1]-(m)
WHERE n.id in ['Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9','Domain_f3554b666038baffa5814c319d3053ee2c2eb30d31d0ef509a1a463386b69845'] 
RETURN n, m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提示 建议每次按 1 度扩散，否则返回数据量太大，会导致浏览器奔溃。</p>
<h4 data-id="heading-11">探索可疑线索</h4>
<p>对 c58c149eec.com 节点做一度关系扩散，发现 61befc7014.com 与 c58c149eec.com 是子域名关系，且都是涉黄域名，这两个域名与另一个正常域名 1d8e02f35e.com 使用同一个 IP 123.1.xxx.xxx  和同一个证书 fe794a69ea ,且两个涉黄域名是同一个人 Linxxxxx Xu 使用同一个电话 +86.533xxxxx 和同一个 Email <a href="https://link.juejin.cn/?target=mailto%3A54498xxxxx%40xxx.xx" target="_blank" title="mailto:54498xxxxx@xxx.xx" ref="nofollow noopener noreferrer">54498xxxxx@xxx.xx</a> 注册，因此用户  **Linxxxxx Xu **有非常大的嫌疑。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1412e86d1b1847d390d873fdd778294b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">锁定嫌疑人</h4>
<p>对 Linxxxxx Xu 做一度扩散，通过「节点重要性」资产，对画布中的节点执行 PageRank 算法，重要程度映射到节点大小上面。使用「筛选器」资产，发现该用户注册了 50+ 域名，其中 4+ 涉黄、2+ 涉毒、12+ 涉枪，非法域名占比将近 40%，因此可以认定该用户涉嫌黑灰产犯罪，需要重点打击和整治。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/696c5e2b64204fde9a2b550d655fb78e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">锁定证书</h4>
<p>我们发现证书 fe794a69ea 关联了两个涉赌域名，所有有必要对该证书进行深入的分析。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77fd0c8160474897b784258fc6df891c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对证书 fe794a69ea 做一度关系扩散，共扩散出 100+ 节点，其中涉及到涉黄、诈骗、非法交易平台等 10+ 非法节点，因此，我们可以认定该证书存在严重的问题，建议警方对该证书进行处理，如封掉、监控等。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccddacc1d8b74016b718e3b9eefa883e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">关联分析</h4>
<p>截至现在，我们都还是只针对提供的第一个线索分析分析，给定的两个线索之前还没有任何联系，所以接下来我们对第二个线索点进行关系扩散。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6deb2317ab244f3f8115ff148641550c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
对第二个涉枪线索节点 f3554b6660.com 做一度关系扩散后，发现该节点与跳转的域名 afd826f13.com 节点涉枪，且与 9b137c5215.com、cee489b4e7.com 和 91de97019b.com 三个正常域名使用同一个证书 392d981eaf，涉枪节点 f3554b6660.com 和 afd826f13.com 与正常域名 91de97019b.com、cee489b4e7.com 使用同一个 IP 156.239.xxx.xxx，更为关键的是正常域名 91de97019b.com 是涉嫌犯罪的  Linxxxxx Xu 注册的。</p>
<p>由于涉枪节点 afd826f13.com 三个节点使用同一个证书 392d981eaf ，因此我们对证书节点 392d981eaf 做一度关系扩散，扩散出来了一个节点 c01f10c61a，再扩展 c01f10c61a 节点，扩散出 50+ 证书节点，我们随机选择一批证书节点进行一度关系扩散，扩散出的两个子网络中 90% 以上的节点都涉赌，因此，我们认定证书节点 **392d981eaf **存在严重的风险。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b4ac8d9463543eeae171d8d82c3d068~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Domxxxxmin 用户同时申请了两个涉枪域名，因此我们有必要对其进行进一步的分析。
对涉枪节点 f3554b6660.com 的申请者 Domxxxxmin 做一度关系扩散，扩散出 100+ Domain 类型的节点，其中 4 个涉黄、1 个涉赌节点，非法节点占比 5% 左右，初步可以判断该子图非核心网络。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda03c083ce3443d8f631a99c0dc64ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">路径分析</h4>
<p>通过网络我们可以发现，通过正常域名 91de97019b.com 将两个小型的黑灰产网络关联了起来，我们使用「路径分析」资产，在图上选择起点 c58c149eec.com 和终点 f3554b6660.com ，计算出的路径中由于有环的存在，我们只筛查过最关键的 2 条最短路径，如下图所示。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fde7cd086b7b445bb8bc788c9646785d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 2 条关键路径上，有两个起桥接作用的正常 Domain 节点引起了我们的注意，虽然这两个节点是正常的节点，但他们所处的位置却非常关键，对名称为 cee489b4e7.com 和 91de97019b.com 的两个节点做一度关系扩散，并没有扩散出有价值的节点，所以我们判断这两个节点的作用就是使用正常 Domain 用来连接涉赌和涉枪 Domain 的。</p>
<h4 data-id="heading-16">验证判断</h4>
<p>为了进一步验证我们的判断，我们对线索节点的注册电话、Email 及证书等节点做一度关系扩散，我们可以得到如下比较完整的网络子图，从下图中，我们基本上就可以得到该团伙的关键链路和核心资产。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce05ada525a94aee84776bb3e78e7275~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">归纳整理</h4>
<p>使用右键菜单中的「收起节点」资产，过滤掉非核心的节点，得到核心的黑灰产网络子图，如下图所示。
说明 目前「收起节点」的实现逻辑是隐藏节点，并没有真正删除掉画布上的节点，所以隐藏后画布上节点数量并不会减少。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f10d257a2654c32a445f5e2374354e1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">结论呈现</h3>
<p>在上面的核心子图中，我们就可以很方便地筛选出核心网络资产和关键链路。</p>
<p><strong>核心网络资产</strong></p>















































<table><thead><tr><th>属性 ID</th><th>名称</th><th>类型</th><th>黑灰产类型</th></tr></thead><tbody><tr><td>Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9</td><td>c58c149eec.com</td><td>Domain</td><td>涉赌</td></tr><tr><td>Cert_fe794a69eacd63b21245bf4eda826222fc6c5862bebf77aa05459cb308cfd063</td><td>fe794a69ea</td><td>Cert</td><td></td></tr><tr><td>IP_94fb4d47d3920b6a5b74a8ce9e304377460fdffdf6582eca97eda2037bbe0b47</td><td>123.1.xxx.xxx</td><td>IP</td><td></td></tr><tr><td>Domain_f3554b666038baffa5814c319d3053ee2c2eb30d31d0ef509a1a463386b69845</td><td>f3554b6660.com</td><td>Domain</td><td>涉枪</td></tr><tr><td>Cert_392d981eaf712a3ecb8553b3b90974d538e484bad7ccff19f6ef89d1b6456226</td><td>392d981eaf</td><td>Cert</td><td></td></tr><tr><td>IP_e9d4d0c9b504b782a7e04f78cf471fc52abba41c1330dec1bd5cfb583add10ce</td><td>156.239.xxx.xxx</td><td>IP</td><td></td></tr></tbody></table>
<p><strong>关键链路</strong></p>









































<table><thead><tr><th>关键路径</th><th></th></tr></thead><tbody><tr><td><strong>路径 1</strong></td><td><strong>Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9</strong></td></tr><tr><td></td><td>Whois_Name_db0925a5aeb1849fa7b41f7a29c1192d38e12e97fb6e82e72e894e3c733130ef</td></tr><tr><td></td><td>Domain_cee489b4e75d3b79f86fc13516688cb4ed6a84e39f139f25014bf97c0d7bfbf1</td></tr><tr><td></td><td><strong>Domain_f3554b666038baffa5814c319d3053ee2c2eb30d31d0ef509a1a463386b69845</strong></td></tr><tr><td><strong>路径 2</strong></td><td><strong>Domain_c58c149eec59bb14b0c102a0f303d4c20366926b5c3206555d2937474124beb9</strong></td></tr><tr><td></td><td>Whois_Name_db0925a5aeb1849fa7b41f7a29c1192d38e12e97fb6e82e72e894e3c733130ef</td></tr><tr><td></td><td>Domain_91de97019b99f9e4b03f9d1bec9fd8925b15a3687a10ea0124baab42e36170b7</td></tr><tr><td></td><td><strong>Domain_f3554b666038baffa5814c319d3053ee2c2eb30d31d0ef509a1a463386b69845</strong></td></tr></tbody></table>
<p>通过上面的分析，我们可以得到黑灰产团伙的运行机制：犯罪嫌疑人使用同样的手机号码和 Email 注册一大批域名，其中 30% 左右域名都涉赌、涉枪、涉黄等，70% 左右属于正常域名，实际上这些违法域名及正常域名背后使用的都是同一个 IP 和同一个证书。黑灰产团伙将少量的正常域名 CNAME 到涉黄涉赌等违法域名上，当用户访问正常域名时，在不知情的情况下就会自动跳转到涉赌涉枪等违规域名上，从而达到传播违法违规内容、开展网络诈骗、网络赌博、网络色情、违禁品交易等犯罪活动。</p>
<p>通过分析获取到上述的核心资产和关键链路后，就可以通过封掉手机号码、Email、证书和 IP 阻止违规违法域名的访问，从而有效减少网络诈骗、网络赌博、网络色情等犯罪活动。通过抓捕犯罪嫌疑人，从而有效打击黑灰产团伙。</p></div>  
</div>
            