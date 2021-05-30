
---
title: 'StepsGuide：一个像跟屁虫一样的组件 - DevUI'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 20:21:30 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image" alt="Kagol.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">引言</h1>
<p>近期对 ProjectMan 业务的工作项搜索/过滤功能做了优化，用 DevUI 组件库新推出的 <a href="https://devui.design/components/zh-cn/category-search/" target="_blank" rel="nofollow noopener noreferrer">CategorySearch</a> 组件替换了之前复杂繁琐的交互方式，实现了搜索、过滤、过滤条件显示3个功能的整合，能够有效提升用户的操作效率和体验。</p>
<p>以下是新旧过滤器的效果对比：</p>
<p>旧版过滤器</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d99174850d04582990b2727616ca241~tplv-k3u1fbpfcp-watermark.image" alt="before-search-module.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新版过滤器</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afa23663c0dd46c19392189f2f7bc683~tplv-k3u1fbpfcp-watermark.image" alt="after-category-search2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从新旧过滤器的对比可以看出，两者相差很大，这个旧版的过滤器已经在线上运行多年，用户已经习惯了这种交互方式，如果贸然上一个几乎是全新的东西，势必会挑战用户的使用习惯，即使新版过滤器拥有简单易用、操作效率高、体验好等众多优点。</p>
<p>由于要改变用户习惯，前期很可能还是会受到部分用户的排斥和抵触，为了尽可能让用户平滑过渡到新版过滤器，需要增加一个简单的用户指引，让用户通过几个简单的步骤，快速了解新版过滤器的使用方式。</p>
<h1 data-id="heading-1">1 单步骤用户指引</h1>
<p>用户指引应该是一个比较通用的场景，先到组件库里找下有没有可以直接用的组件。</p>
<h2 data-id="heading-2">1.1 寻找合适的组件</h2>
<p>打开DevUI官网的组件总览页面：</p>
<p><a href="https://devui.design/components/zh-cn/overview" target="_blank" rel="nofollow noopener noreferrer">devui.design/components/…</a></p>
<p>先尝试搜索🔍关键字<code>指引</code>，找到一个操作指引组件：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/875fcb1ea9ff41debfc5892767877e7a~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击进入<code>StepsGuide</code>组件的详情页面：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4213d2bc5f5549129a41ea99029bf863~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>何时使用</code>里写了该组件的使用场景：</p>
<blockquote>
<p>业务推出新特性，或复杂的业务逻辑需要指引用户时使用。</p>
</blockquote>
<p>和我们的场景是一样的，直接拿来用吧。</p>
<h2 data-id="heading-3">1.2 看组件Demo，了解组件基本用法</h2>
<p>先看下第一个基本用法的Demo：</p>
<pre><code class="copyable"><d-button
  bsStyle="common"
  dStepsGuide
  [pageName]="'step-basic-demo'"
  [steps]="steps"
  [stepIndex]="0"
  [dStepsGuidePosition]="'top'"
  (operateChange)="operateChange($event)"
  (click)="reset(0)"
>
  Step 1
</d-button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这个Demo，我们大致可以一窥其使用方式：</p>
<ul>
<li>以指令（<code>dStepsGuide</code>）的方式使用</li>
<li>指令放在哪个元素上，就在它上面展示一个指引框</li>
<li><code>dStepsGuidePosition</code>属性应该是控制指引框的位置</li>
<li><code>steps</code>应该是配置指引步骤数据源</li>
<li><code>stepIndex</code>应该是表示当前的元素是第几个步骤</li>
<li><code>pageName</code>暂时还不知道有什么用</li>
<li><code>operateChange</code>是一个事件，还不知道有什么用</li>
</ul>
<p>看完HTML文件，再看下TS文件：</p>
<pre><code class="copyable">export class BasicComponent implements OnInit &#123;
  ...
  steps = [
      &#123;
        title: 'Step 1',
        content: 'Guide Content',
      &#125;,
      &#123;
        title: 'Step 2',
        content: 'Guide Content',
      &#125;,
      &#123;
        title: 'Step 3',
        content: 'Guide Content',
      &#125;,
  ];
  constructor(private stepService: StepsGuideService) &#123;&#125;

  ngOnInit() &#123;
    this.stepService.currentIndex.subscribe((index) => (this.currentStep = index));
    /* 由于整个demo是在一个页面内显示多个操作指引序列，因此需要在初始化时重置显示状态 */
    localStorage.setItem('devui_guide_step-position-demo', '0');
    localStorage.setItem('devui_guide_step-custom-demo', '0'); /* 设置第二个序列为不显示状态 */
    localStorage.removeItem('devui_guide_step-basic-demo'); /* 设置第一个序列为显示状态 */
    this.stepService.setSteps(this.steps); /* 将步骤数据设置为第一个序列的内容 */
    this.stepService.setCurrentIndex(0); /* 设置当前序列显示步骤为第一个步骤 */
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从TS文件里可以看到steps步骤数据源的结构，steps是一个对象数组，每一个数组项表示一个指引步骤，里面包含该步骤的标题和内容。</p>
<p>组件初始化事件里面写了一些逻辑，有点复杂，我们先不看。</p>
<p>根据现有的知识，应该能先用起来。</p>
<h2 data-id="heading-4">1.3 先用起来再说</h2>
<p>比如我想给下面的搜索框元素加一个指引：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66a6b4dee16a4b18a1e120aa1997aac0~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大致效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce6bc5b9f9b94f2bac383142faf34ee2~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">1.3.1 第一步是先引入组件模块</h3>
<pre><code class="copyable">import &#123; StepsGuideModule &#125; from 'ng-devui';

@NgModule(&#123;
  ...
  imports: [
    ...
    StepsGuideModule,
  ],
  ...
&#125;)
export class MainContentHeadModule &#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">1.3.2 然后加上dStepsGuide指令和相应的属性</h3>
<p>先只加一个steps试试看：</p>
<pre><code class="copyable"><d-search 
  dStepsGuide
  [steps]="steps"
></d-search>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">steps = [
  &#123;
    title: '新功能介绍：搜索框',
    content: `
      <p>1、过滤功能迁移至搜索框中啦</p>
      <p>2、在搜索框中，您可输入关键词或添加筛选条件查询所需要的工作项</p>
    `,
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现什么效果都没有。</p>
<h3 data-id="heading-7">1.3.3 调整参数，达到我们想要的效果</h3>
<p>回过头来看组件Demo，组件初始化时做了一些事情：</p>
<pre><code class="copyable">  ngOnInit() &#123;
    this.stepService.currentIndex.subscribe((index) => (this.currentStep = index));
    /* 由于整个demo是在一个页面内显示多个操作指引序列，因此需要在初始化时重置显示状态 */
    localStorage.setItem('devui_guide_step-position-demo', '0');
    localStorage.setItem('devui_guide_step-custom-demo', '0'); /* 设置第二个序列为不显示状态 */
    localStorage.removeItem('devui_guide_step-basic-demo'); /* 设置第一个序列为显示状态 */
    this.stepService.setSteps(this.steps); /* 将步骤数据设置为第一个序列的内容 */
    this.stepService.setCurrentIndex(0); /* 设置当前序列显示步骤为第一个步骤 */
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一行代码似乎是用来控制显示哪一个步骤指引的：</p>
<pre><code class="copyable">this.stepService.setCurrentIndex(0); /* 设置当前序列显示步骤为第一个步骤 */
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们加上这一行试试看。</p>
<pre><code class="copyable">import &#123; StepsGuideService &#125; from 'ng-devui';

constructor(
  private stepService: StepsGuideService,
) &#123;&#125;

ngOnInit(): void &#123;
  this.stepService.setCurrentIndex(0); /* 设置当前序列显示步骤为第一个步骤 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现还是没效果。</p>
<p>再加上调用setSteps方法那一行试试：</p>
<pre><code class="copyable">ngOnInit(): void &#123;
  this.stepService.setSteps(this.steps); /* 将步骤数据设置为第一个序列的内容 */
  this.stepService.setCurrentIndex(0); /* 设置当前序列显示步骤为第一个步骤 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是不行，再试试加上stepIndex属性：</p>
<pre><code class="copyable">    <d-search 
      dStepsGuide
      [steps]="steps"
      [stepIndex]="0" // 新增的
    ></d-search>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>终于有效果了：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/208f99da6f2d407c9eb7b87e818e5673~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过默认位置显示在元素上方，被挡住了，可以设置下dStepsGuidePosition属性，调整下指引的位置：</p>
<pre><code class="copyable">    <d-search 
      dStepsGuide
      [steps]="steps"
      [stepIndex]="0"
      dStepsGuidePosition="bottom" // 新增的
    ></d-search>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这回正常了。</p>
<p>效果和我们想要的一模一样：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7431285d2ca44124a07e1b089b9e881c~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">1.3.4 小结</h3>
<p>回顾一下，为了实现单步骤用户指引，我们使用了<code>dStepsGuide</code>指令的三个参数：</p>
<ul>
<li>steps 步骤数组，是一个对象数组，里面包含步骤的标题（title）和内容（content）</li>
<li>stepIndex 显示第几个步骤</li>
<li>dStepsGuidePosition 显示位置（一共有8个方位）</li>
</ul>
<p>为了设置当前步骤为第一个步骤，我们调用了stepService的两个方法：</p>
<ul>
<li>setSteps(this.steps) 将步骤数据设置为第一个序列的内容</li>
<li>setCurrentIndex(0) 设置当前步骤为第一个步骤</li>
</ul>
<p>这就是实现单步骤用户指引所需要知道的全部知识。</p>
<h1 data-id="heading-9">2 多步骤指引</h1>
<p>这时产品说一个步骤不够，要加一个，主要有两个要求：</p>
<ul>
<li>第一个步骤里面点击下一步，可以跳到下一个步骤</li>
<li>第二个步骤有一个返回上一步的按钮</li>
</ul>
<p>为了实现多步骤指引，我们不需要学习任何多余的API，只需要简单地在steps中增加一个步骤，并设置第二个步骤的stepIndex为1即可。</p>
<pre><code class="copyable"><d-search 
  dStepsGuide
  dStepsGuidePosition="bottom"
  [steps]="steps"
  [stepIndex]="0"
></d-search>
<!--新增的步骤-->
<d-button
  dStepsGuide
  dStepsGuidePosition="bottom"
  [steps]="steps"
  [stepIndex]="1"
>新建项目</d-button>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">steps = [
  &#123;
    title: '新功能介绍：搜索框',
    content: `
      <p>1、过滤功能迁移至搜索框中啦</p>
      <p>2、在搜索框中，您可输入关键词或添加筛选条件查询所需要的工作项</p>
    `,
  &#125;,
  // 新增的步骤
  &#123;
    title: '新功能介绍：新建项目',
    content: `
      <p>点击“新建项目”按钮，即可跳转到新建项目页面</p>
    `,
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/321de82b64224eb1955c24cd36f42e29~tplv-k3u1fbpfcp-watermark.image" alt="多步骤用户指引.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是非常简单？</p>
<h1 data-id="heading-10">3 跟随效果</h1>
<p>以上实现会有一个问题：</p>
<blockquote>
<p>如果步骤的目标元素是动态变化的，比如它的位置变了，宽高变了，指引不会跟着变。</p>
</blockquote>
<p>效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89614834bb0d4047974c6f4dabd197cd~tplv-k3u1fbpfcp-watermark.image" alt="不跟随的情况.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时需要用到StepsGuide组件的另一个API：<code>observerDom</code></p>
<p>这个API会让指引步骤秒变跟屁虫：</p>
<blockquote>
<p>目标元素在哪儿，指引步骤就跟到哪儿。</p>
</blockquote>
<p>API文档用了大段文字来描述这个<code>observerDom</code>的用途，其实就是把指引步骤的浮框变成“跟屁虫”😄</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac9bfbe4b2c14ca68adc5140719e9009~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><d-search 
  dStepsGuide
  dStepsGuidePosition="bottom"
  [steps]="steps"
  [stepIndex]="0"
  [observerDom]="observerDom" // 新增的
></d-search>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">observerDom;

ngOnInit(): void &#123;
  // 新增的，把搜索框的外层元素设置成observerDom，这样只要它里面的任何元素发生变化，导致了搜索框位置发生变化，步骤指引的浮框都会跟着变化
  this.observerDom = document.querySelector('.main-content');
  
  this.stepService.setSteps(this.steps);
  this.stepService.setCurrentIndex(0);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26ce78b9a09243ec8962e5837649bce7~tplv-k3u1fbpfcp-watermark.image" alt="跟随的情况.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不仅仅是搜索框宽度变化，其他变化导致的搜索框位置的变化也会触发步骤指引的跟随：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be33878dc4064b8d94b1908fad4f136c~tplv-k3u1fbpfcp-watermark.image" alt="响应其他变化.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是非常有意思？</p>
<p>接下来我们就来看看这个简单却很有意思的“跟屁虫”组件还有哪些能力。</p>
<h1 data-id="heading-11">4 StepsGuide组件的其他API</h1>
<p>关注StepsGuide组件的介绍，没有比它的<a href="https://devui.design/components/zh-cn/steps-guide/api" target="_blank" rel="nofollow noopener noreferrer">API文档</a>写得更清楚的了。</p>
<p>它一共有12个属性API，一个事件API。</p>
<p>属性API：</p>
<ul>
<li>steps 步骤数组</li>
<li>stepIndex 当前步骤索引</li>
<li>dStepsGuidePosition 指引步骤的位置</li>
<li>observerDom 跟随效果</li>
<li>pageName 用来标识操作指引，跨页面（或路由）时会用到</li>
<li>leftFix 位置修复</li>
<li>topFix 位置修复</li>
<li>zIndex 指引步骤的层级</li>
<li>targetElement 指定目标元素，当需要为动态生成的元素添加指引时会用到</li>
<li>scrollElement 指引信息跟随滚动定位的容器元素</li>
<li>scrollToTargetSwitch 是否自动滚动页面至指引信息显示的位置</li>
<li>extraConfig 扩展配置，用于隐藏上一步按钮和步骤圆点图标</li>
</ul>
<p>事件API：</p>
<ul>
<li>operateChange 指引步骤中的按钮事件，需要自定义下一步的动作时会用到</li>
</ul>
<p>这些API的具体用法详见StepsGuide组件的Demo：</p>
<p><a href="https://devui.design/components/zh-cn/steps-guide/demo" target="_blank" rel="nofollow noopener noreferrer">devui.design/components/…</a></p>
<p>如果你的业务中也有新特性要发布，需要增加用户指引，不妨试试这个有趣的跟屁虫组件吧😜！</p>
<p>也欢迎使用DevUI新发布的<a href="https://devui.design/admin/" target="_blank" rel="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-12">加入我们</h1>
<p>我们是DevUI团队，欢迎来这里和我们一起打造优雅高效的人机设计/研发体系。招聘邮箱：<a href="mailto:muyang2@huawei.com">muyang2@huawei.com</a>。</p>
<p>文/DevUI Kagol</p>
<p>往期文章推荐</p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank">《Quill富文本编辑器的实践》</a></p>
<p><a href="https://juejin.cn/post/6959700988882059271" target="_blank">《如何解决异步接口请求快慢不均导致的数据错误问题？》</a></p>
<p><a href="https://juejin.cn/post/6956155033410863134" target="_blank">《号外号外！DevUI Admin V1.0 发布啦！》</a></p>
<p><a href="https://juejin.cn/post/6956612556710477860" target="_blank">《CategorySearch分类搜索组件初体验》</a></p>
<p><a href="https://juejin.cn/post/6956988395016945701" target="_blank">《让我们一起建设 Vue DevUI 项目吧！》</a></p></div>  
</div>
            