
---
title: '针对多状态订单详情的前端mock方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee8f80f9e2584031a8aa0279f12db350~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 00:57:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee8f80f9e2584031a8aa0279f12db350~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：闲鱼技术——树城</p>
<h2 data-id="heading-0">背景</h2>
<p>闲鱼作为国内最大的二手交易电商平台，有着验货宝/省心卖/优品等有着闲鱼特色的交易链路，而作为交易链路的闭环，一旦形成有效订单，就会有对应的订单详情页，订单详情页往往承载着复杂的交易状态的变化。以验货宝为例， 验货宝是闲鱼推出针对二手商品存在的质量/真伪的不确定性，提出的先验货后交易模式。 作为交易订单节点： **就有买家拍下->付款->卖家发货->鉴定方收货->鉴定为真->发货给买家->买家收货 **等多个交易节点,一个订单详情页在不同流转状态下可能存在数十种细分状态，每种状态之间存在着有着文案/操作按钮/进度条等视觉交互上的差别, 如下图所示：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee8f80f9e2584031a8aa0279f12db350~tplv-k3u1fbpfcp-zoom-1.image" alt title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">存在问题</h2>
<p>订单详情页的不同的状态视图流转，依赖于接口返回的字段的改变，但服务端的接口变化往往对应真实订单的场景推进且不可逆，特别其中还包含第三方接口交互，显然每种状态依赖后端接口变化存在较大沟通成本； 而前端的直接mock的方式，像集团内的山海关,dummy更多是通用性地将请求和不同的mock数据建立起映射关系, 需要修改status的值来进行修改mock.json。在真机调试时，依赖的Charles或Fiddler代理工具，往往通过pc侧代理字段来修改网路字段，单次切换成本高； 测试同学在回归此类页面时也无法快速切到想要订单状态，导致测试回归的成本高. UI同学在视觉走查中的不同状态切换更是完全黑盒，难以覆盖全部视觉，进而导致页面上线后，才从用户侧反馈某一机型下的订单状态样式显示有异。要还原用户的这种订单状态又是得服务端慢慢推进订单状态，排查周期长，容易引起线上舆情。 总结来说，面对此类订单的订单详情页的前端开发测试，我们现有的mock存在着以下问题：</p>
<blockquote>
<p>•开发联调周期长，自测难以充分；•测试/视觉回归成本高；•线上样式问题定位还原周期长；</p>
</blockquote>
<h2 data-id="heading-2">需求分析</h2>
<p>针对以上的问题，能否让订单状态页面的mock方式更为易用，我们通过真实的开发体验，提出了针对此类页面的mock方式要达到好用，应该具备以下特点：</p>
<ol>
<li></li>
</ol>
<p><strong>调试方便</strong></p>
<blockquote>
<p>mock方式应该在本地pc端调试和真机调试都能够方便使用；</p>
</blockquote>
<ol start="2">
<li></li>
</ol>
<p><strong>业务语义</strong></p>
<blockquote>
<p>不同状态的切换交互应该带有业务语义，能够方便开发和测试快速找到想要的订单状态，而不只是简单的修改接口的某个字段值；</p>
</blockquote>
<ol start="3">
<li></li>
</ol>
<p><strong>代码解耦</strong></p>
<blockquote>
<p>mock的方式本身应该和业务代码尽量解耦，即不会将mock的逻辑引入线上环境；</p>
</blockquote>
<ol start="4">
<li></li>
</ol>
<p><strong>mock数据精简</strong></p>
<blockquote>
<p>订单页面状态虽多，但是接口往往统一，接口字段，对mock数据的维护不应该每一种状态都是单独一份mock数据而是应该在一份主的mock数据上针对产生变化的字段进行单独mock;</p>
</blockquote>
<h2 data-id="heading-3">技术方案</h2>
<h3 data-id="heading-4">方案总揽</h3>
<p>基于以上需求，我们尝试设计开发更为贴近此类业务的mock方案。先别看广告，看疗效， 此方案的真实效果如下图所示:<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6db320776b2f45a6a3080e2b18da3c0d~tplv-k3u1fbpfcp-zoom-1.image" alt title="null" loading="lazy" referrerpolicy="no-referrer">从效果图可以看出我们通过按钮点击实现了状态视图的变更，也就实现了目标一、二，而这个按钮本身不会在线上环境所带入也就不实现了代码解耦；那么这套方案是如何实现的呢？如下图所示，我们将整体方案设计为三大模块:<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21d3c0b42aa34df9944e3511991fe05a~tplv-k3u1fbpfcp-zoom-1.image" alt title="null" loading="lazy" referrerpolicy="no-referrer">​</p>
<p><strong>胶水层</strong>：是整个方案的编译层基座，负责在编译层将视图层插件和mock层插件按照生产环境状态加载进入业务层，实现在本地和预发环境下具有mock能力，并负责在视图层进行状态切换时按照状态码重新生成对应mock.json，利用胶水层的打包逻辑做到了与业务解耦的目标； <strong>mock层：<strong>负责将前端发起的mtop请求拦截，根据路由映射到本地webserver下的mock.json并模拟返回对应结果，利用mock层方式实现了mock数据精简，调试方便的目标</strong>；</strong> **视图层： **负责页面处的整体mock状态切换的交互逻辑，我们将交互入口设计为类似于eruda调试工具的唤起方式，在需要的订单页面侧植入, 点击会唤起弹层，弹层展示所有可枚举的订单状态文案以及其他可枚举会影响订单视图的变量条件，点击对应状态进行页面重载展示对应状态的视觉; 视图层负责实现了业务语义的目标。</p>
<h3 data-id="heading-5">胶水层实现</h3>
<p>在具体实现过程中，由于闲鱼前端开发使用集团提供的rax的前端方案，rax-app也提供了在编译层可以定制的插件机制, rax-app基于工程构建工具 build-scripts 封装，因此在插件能力上也完整继承了build-scripts。除了通过插件定制工程能力以外，rax-app 还为插件扩展了运行时定制的能力, 我们定制了@ali/build-plugin-rax-mock和本地的selfBuild两个编译插件，分别对应mock层和胶水层的设计需求，以如下方式在项目的build.json里进行引入，很好地实现与业务层代码的解耦。</p>
<pre><code class="copyable">&#123;
  "plugins": [
    [
      "build-plugin-rax-app",
      &#123;
        "targets": [
          "web"
        ],
        "type": "mpa"
      &#125;
    ],
    "@ali/build-plugin-rax-mock",
    "./selfBuild"
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​rax-app的插件机制提供的针对webpack打包方案所提供的onGetWebpackConfig api将视图层组件植入业务页面， 如下方代码所示，会在打包过程中根据根据指定页面文件路径选择性地注入，并且判断编译环境在真实生产环境中不做任何mock模块的打包。</p>
<pre><code class="copyable">if (api.context.command === 'build') return;
    api.onGetWebpackConfig('web', (config) => &#123;
      config.entryPoints.values().forEach(entry => &#123;
        const entrys = entry.values();
        const entryName = entrys[1];
        // 只对订单页面注入
        if (!/pages\/Order\/index$/.test(entryName)) &#123;
          return;
        &#125;

        const prefixLoader = __filename;
        const debugOrderPath = path.resolve(__dirname, 'src/components/DebugOrder');
        const newOrderPage = `$&#123;prefixLoader&#125;?debugOrderPath=$&#123;debugOrderPath&#125;!$&#123;entryName&#125;`;

        entry.clear();
        // 视图层组件 
        entry.add(entrys[0]);
        entry.add(newOrderPage);
      &#125;);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此通过胶水层，我们可以快速将mock模块和视图层模块快速引入到工程方案中，并能按需引入，不对业务造成明显侵入痕迹。</p>
<h3 data-id="heading-6">mock层实现</h3>
<p>首先我们会根据状态合集所需订单详情接口生成一份mock.json数据的合集，这样就能涵盖所有状态下所需消费字段，一般接口格式如下所示：</p>
<pre><code class="copyable">&#123;
    "api": "mtop.a.order.info",
    "data": &#123;
      "status": 0,
      "orderStatus": 1001,
        ...
      "trade": &#123;
        "actions": [],
          ....
        "amount": "2189.00",
        "attributes": &#123;
          "consis": "10",
            ...
          "ultronPP": "a_3_0@c",
         &#125;
       &#125;
     &#125;,
     "ret": [
      "SUCCESS::调用成功"
        ],
        "v": "1.0"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图所示，mock层既要更新视图层切换状态而组成新的mock.json, 也要拦截页面侧发起的mtop网络请求定向到对应的mock.json文件；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ecd32150ed24408b09cb50d231600da~tplv-k3u1fbpfcp-zoom-1.image" alt title="null" loading="lazy" referrerpolicy="no-referrer">为了真实能够把接口请求到本地，需要对h5页面侧发起的mtop请求进行拦截，这里利用了淘宝mtop库的运行机制会将mtop对象加载到页面全局的window.lib对象上，利用Proxy的代理机制监听window.lib对象的挂载mtop时机set进行hook, 并根据所处的生产环境判断是否使用发送请求到本地的自定义request请求, 实现代码如下：</p>
<pre><code class="copyable">lib = window.lib;
// 拦截Mtop对象的request方法挂载
const getMtop = (originValue) => 
new Proxy(originValue, &#123;
  set(target, p, v, r) &#123;
    if (p === 'request' 
    || p === 'H5Request') &#123;
      Reflect.set(target, p, getRequest(v), r);
    &#125; else &#123;
      Reflect.set(target, p, v, r);
    &#125;

    return true;
  &#125;
&#125;);

// 拦截window.lib对象挂载mtop
if (!lib) &#123;
    lib = new Proxy(&#123;&#125;, &#123;
    set(target, p, v, r) &#123;
      if (p.toLowerCase() === 'mtop') &#123;
        Reflect.set(target, p, v,r);
      &#125; else &#123;
        Reflect.set(target, p, v, r);
      &#125;
      return true;
    &#125;
  &#125;);
&#125; else if (!lib.mtop) &#123;
lib.mtop = getMtop(&#123;&#125;);
&#125; else &#123;
lib.mtop.request = getRequest(lib.mtop.request);
lib.mtop.H5Request = getRequest(lib.mtop.H5Request);
&#125;

// 根据运行环境选择加载对应的request请求
function getRequest(originRequest) &#123;
  return async function () &#123;
    if (getMockSwitch()) &#123;
      //
    &#125;

    return originRequest();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当挂载完成即可实现接口的mock功能：</p>
<blockquote>
<p>1.当本地页面发起 mtop 请求，如：mtop.com.test.one；2.请求被注入的插件代码 hold 住，当判断是在本地开发环境或者链接带上mock query时， 用本地的mtopRquest替换，请求以 <a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%2F%255C_mtop%255C_mock%255C_%2Fcom.test.one" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1/%5C_mtop%5C_mock%5C_/com.test.one" ref="nofollow noopener noreferrer">http://127.0.0.1/\_mtop\_mock\_/com.test.one</a> 格式重新发起请求；3.请求打到本地 webpack-dev-server 上，server 再去本地 mock 目录上找 com.test.one.js4.如果找到就执行 com.test.one.js 文件，将执行结果返回5.如果未找到，则走原有的 mtop 请求；</p>
</blockquote>
<h3 data-id="heading-7">视图层实现</h3>
<p>视图层UI由页面侧直接可见的切换icon和弹层构成，icon设置为dragable方便用户随时拖动， 弹层的渲染考虑到扩展性由树状节点组成。目前根据真实的业务需要，将节点层级分为2层（可扩展），一级节点代表：<strong>已下单，已验货</strong>等核心节点， 二级节点代表在一级节点下可能存在的正负向交易细节节点， 如：在已下单环节下存在取消订单的副状态； 单点数据结构为如下代码所示，包含有每个枚举状态的语义文案，每种状态对应接口字段的主副状态码，状态枚举值，子节点。</p>
<pre><code class="copyable">// 状态数据结构
export interface ClassifyDataItem &#123;
  [key: string]: any;
  /**
   * 节点名称
   */
  nodeName: string;
  /**
   * 节点枚举值
   */
  node?: StatusEnum;
  /**
   * 对应的协议主状态
   */
  status?: string;
  /**
   * 对应的协议副状态
   */
  subStatus?: string;
  childNode?: ClassifyDataItem[];
&#125;

// 真实的状态数据枚举
export const classifyData: ClassifyDataItem[] = [
  &#123;
    nodeName: '已下单，等待顺丰上门取件',
    status: '1',
    subStatus: '10',
    node: StatusEnum.BUYER_CREATE,
    childNode: [
     ...classifyData
    ]
  &#125;
  ...
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个节点在渲染过程中采用树状递归渲染，视觉层展示nodeName, 同时绑定点击回调onItemChange。当弹窗的某一状态结点发生点击行为时，设置节点选中态样式，同时通过Modal组件通过props传入的函数方法向外层传递绑定在结点上的status和subStatus值，从而实现了点击单个选项能够修改对应的mock.json文件， 同时会触发页面的window.reload()功能重新加载页面发起mtop请求，因此此时接口返回的数据已经是切换后的状态数据，因此页面也会呈现对应状态的视图。</p>
<h2 data-id="heading-8">业务应用</h2>
<p>当将以上所述的整套方案串联完成后，业务侧开发只需要定义好属于自己订单详情的状态枚举数据结构，并将视图层组件和mock层插件引入项目工程，即可接入mock的能力，实现所选即所得的订单状态变更。 目前该方案已经在闲鱼验货宝、奢侈品寄卖等交易链路场景下接入, 从真实使用过程中，能够有效提升开发联调的效率，单次状态的切换时间成本从分钟级别下降到秒级， 并能帮助测试和视觉同学快速回归业务场景，定位线上问题，简单的视觉问题不再依赖于后端接口的状态切换，约能节省30%以上的联调沟通成本。 另外带来的彩蛋是该方案的切换语义特点， 在项目开发人员出现流动时，新承接人能够通过这一mock方式快速地理解业务，上手开发。上手快，所见即所得，算是针对此类页面维护开发的一门利器。​</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a47c39b282c4ef89df3297be1886213~tplv-k3u1fbpfcp-zoom-1.image" alt title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">总结与展望</h2>
<p>本章节主要介绍了闲鱼在前端开发典型交易场景-订单详情页时，面对多状态模式切换页面的一种开发体验提升的一种尝试，通过上述的方案设计基本实现了开篇所定义的业务mock的4个目标：**调试方便、业务语义、代码解耦、mock数据精简，**不仅提升了在开发/测试同学的体验，通过语义化的方式也能帮助项目更好地进行维护升级。 伴随着业务系统的复杂度提升和功能迭代，如何能如何更低成本地去维护mock项目给我们提出了更高的要求，能否在比如状态码伴随业务升级，变更，增减的功能迭代过程中，联动式地快速变更枚举状态值配置，减少业务侧开发的维护成本是我们继续升级迭代该方案的方向。 目前页面只针对单页面mock, 如何去覆盖整体交易链路的mock，比如一个完整订单链路的状态一致性，也是值得探索的方向。</p>
<p>[</p>
<p>]()</p>
<p>​</p>
<p>​</p>
<p>​</p>
<p>​</p>
<p>​</p></div>  
</div>
            