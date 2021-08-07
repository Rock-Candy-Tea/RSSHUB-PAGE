
---
title: '手把手教你实现vue数据双向绑定（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6924d862906b45c0b5f38302288b8a5b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 09:06:56 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6924d862906b45c0b5f38302288b8a5b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第N天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>（已经更文2天）</p>
<h2 data-id="heading-0">前言</h2>
<p><code>vue</code>是现在前端最炙手可热的框架之一，平时工作中或者出去面试，都少不了问一些<code>vue</code>的问题。而<code>vue</code>是怎么实现数据绑定的，又是问的频率最高的几个问题之一，今天就分享一下个人实现的一个简易的<code>vue</code>。这个项目实现了简单的<code>模板编译</code>、<code>数据双向绑定</code>。</p>
<p>源码发布在了个人github上，感兴趣的小伙伴请移步：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKryst4ljy%2Fsimple-vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Kryst4ljy/simple-vue" ref="nofollow noopener noreferrer">vue数据双向绑定源码地址</a></p>
<h2 data-id="heading-1">项目初始化</h2>
<p>首先，实现这个简易的<code>vue</code>，一个好的工程化工具是必不可少的，对于这个项目来说，使用<code>webpack</code>有点太过笨重了，这里使用了<code>parcel-bundler</code>这个工具（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.parceljs.org%2Fgetting_started.html" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.parceljs.org/getting_started.html" ref="nofollow noopener noreferrer">官方文档</a>）。</p>
<blockquote>
<p>Parcel 是 Web 应用打包工具，适用于经验不同的开发者。它利用多核处理提供了极快的速度，并且不需要任何配置。</p>
</blockquote>
<p>我们只需要先创建一个项目，并且安装这个依赖即可。</p>
<pre><code class="copyable">mkdir simple-vue && cd simple-vue
npm init -y
npm install -D parcel-bundler
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装好了这个依赖之后，我们在根目录下创建一个模板文件<code>index.html</code>，并且创建一个<code>src</code>文件夹，并且在此文件夹下创建一个<code>main.js</code>文件作为我们项目的入口文件。</p>
<p><strong>index.html</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>

<head>
  <title>简易vue</title>
  <meta charset="UTF-8">
</head>

<body>
  <div id="app">
    <input type="text" id="ceshi">
  </div>

  <script src="./src/main.js"></script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再在<code>package.json</code>中新增一条脚本指令：</p>
<pre><code class="copyable">"dev": "parcel index.html"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们启动项目<code>npm run dev</code>：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6924d862906b45c0b5f38302288b8a5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到现在，我们的项目就初步搭建好了。</p>
<h2 data-id="heading-2">数据双向绑定</h2>
<p>什么是数据双向绑定呢？写过<code>vue</code>的小伙伴一定知道，在一个<code>vue实例</code>中，通过定义一个<code>data</code>函数返回一个对象，这个对象里面的所有属性经过了一系列的处理就实现了双向绑定。在<code>template</code>中使用<code>v-bind</code>或者<code>&#123;&#123;&#125;&#125;</code>双括号语法，当这些属性改变时，<code>v-bind</code>和<code>&#123;&#123;&#125;&#125;</code>绑定的文本节点就会自动赋值。</p>
<h3 data-id="heading-3">原理概述</h3>
<p>我们先看一张图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5db0dd19efcf416f92be0a9be8d0617f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文项目的实现基本思路就是根据上述这张图，而数据双向绑定的原理在于<code>发布-订阅</code>模式。</p>
<p>我们先抛开代码不谈，发挥一下想象：把<code>data</code>对象里的每一个属性比作一个<code>youtube</code>账号，它有一个<code>订阅者列表</code>，也就是观众列表。当它发布了一个视频，就会自动通知每个列表里的观众去更新他们的主页（<code>update</code>），推送这个视频。而在哪里用到了这个属性（<code>v-bind</code>，<code>&#123;&#123;&#125;&#125;</code>等），那么就把那里设置成一个<code>watcher</code>，也就是一个观众，点击了<code>订阅</code>。</p>
<p>好好理解一下上面的这段话，我们就基于此进入具体实现中了。</p>
<h2 data-id="heading-4">具体实现</h2>
<h3 data-id="heading-5">创建一个vue</h3>
<p>首先，我们照葫芦画瓢，先创建一个<code>vue</code>构造函数。真正的<code>vue</code>怎么写，我们就怎么写，不过我们这个是<code>青春版</code>的，嘻嘻。</p>
<p>先在我们的项目中，创建一个<code>core</code>文件夹，用来存放我们定义好的各种类。再在此文件夹下面创建一个<code>Vue.js</code>文件，用来存放我们的<code>Vue构造函数</code>。首先，我们在<code>main.js</code>中，先定义一个<code>Vue实例</code>，再去根据这个写我们的构造函数：</p>
<p><strong>main.js</strong></p>
<pre><code class="copyable">import Vue from './core/Vue';

const app = new Vue(&#123;
  el: '#app',
  data() &#123;
    return &#123;
      val: '初始化val',
      info: &#123; text: '123' &#125;,
    &#125;;
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是还挺像那么回事的，这里我们往<code>Vue</code>的构造函数中，传入了一个对象，<code>el</code>为绑定的根节点，我们所有的<code>DOM</code>操作都是以此为根节点来的。<code>data</code>则是我们要实现数据双向绑定的那个对象。</p>
<p>我们再回到<code>Vue.js</code>中去：</p>
<p><strong>Vue.js</strong></p>
<pre><code class="copyable">export default class Vue &#123;
  constructor(option) &#123;
    this._init(option);
  &#125;
&#125;

Vue.prototype._init = function (option) &#123;
  const vm = this;

  vm.$el = document.querySelector(option.el); // 项目根节点
  vm.$data = option.data(); // data对象
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们新建好了一个<code>Vue</code>，但是它与数据双向绑定毫无关系。别着急，现在考考你：<strong>数据双向绑定的原理是什么？</strong> 你可能会回答：因为<code>vue</code>通过<code>Object.defineProperty</code>劫持了<code>data</code>对象（vue3.x是通过proxy），当对象属性被读取时，收集依赖；当对象属性设置时，发布订阅。非常好，既然知道了原理，那我们现在就动手实现吧。</p>
<h3 data-id="heading-6">劫持data对象</h3>
<p>我们再往<code>Vue构造函数</code>的原型中加东西，加入劫持对象的方法：</p>
<pre><code class="copyable">// 监听对象属性变化方法，自动订阅以及发布订阅
Vue.prototype.defineReactive = function (obj) &#123;
  if (!(obj instanceof Object)) return;
  // 遍历对象
  for (let key in obj) &#123;
    let val = obj[key]; // 取data对象的每一个属性的值
    Object.defineProperty(obj, key, &#123;
      enumerable: true, // 是否可枚举
      configurable: true, // 是否可配置
      get() &#123;
        console.log(`get：$&#123;key&#125; - $&#123;val&#125;`);
        return val;
      &#125;,
      set(newVal) &#123;
        if (newVal === val) return;
        console.log(`set：$&#123;key&#125; - $&#123;newVal&#125;`);
        val = newVal;
      &#125;,
    &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再在<code>_init</code>方法中，调用此方法劫持<code>data</code>对象，并且写一个测试方法来试试是否已经成功的劫持了<code>data</code>对象：</p>
<pre><code class="copyable">Vue.prototype._init = function (option) &#123;
  const vm = this;

  vm.$el = document.querySelector(option.el); // 项目根节点
  vm.$data = option.data(); // data对象

  // 劫持data对象
  vm.defineReactive(vm.$data);
  
  // 测试方法 - 监听input输入
  const input = document.getElementById("ceshi");
  vm.$data.val; // 试着读取一下值
  input.addEventListener(
    "input",
    (e) => &#123;
      vm.$data.val = e.target.value; // 赋值操作
    &#125;,
    false
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们打开控制台，并向输入框中输入一些文本，发现打印了一些信息：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc9b9b965808401886d45866df7e1e2d~tplv-k3u1fbpfcp-watermark.image" alt="qwe2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里，我们成功的劫持了<code>data</code>对象。</p>
<p>我们再来思考下<code>原理概述</code>那里的那段话，<code>data</code>对象里的每一个属性比作一个<code>youtube</code>账号，我们现在劫持了<code>data</code>，就相当于给每个属性都创建了一个<code>频道</code>。而一个<code>频道</code>要有什么呢，当然是<code>订阅者列表</code>，我们要给我们的粉丝一个家（也希望看文章的小伙伴点点赞点点关注，给我一个温暖的家~）。那么这个订阅者列表是什么呢？我们就来创建一个。</p>
<h3 data-id="heading-7">创建订阅者列表 - Dep</h3>
<p>我们在<code>core</code>文件夹下新建一个<code>Dep.js</code>文件，用来存放我们的<code>Dep</code>构造函数：</p>
<p><strong>Dep.js</strong></p>
<pre><code class="copyable">// Dep类为每个频道的订阅者列表，提供一个subs数组来维护此频道的订阅者
export default class Dep &#123;
  static target = null;

  constructor() &#123;
    this.subs = []; // 订阅者列表
  &#125;

  // 添加订阅
  addSub(sub) &#123;
    this.subs.push(sub);
  &#125;

  // 删除订阅
  removeSub(sub) &#123;&#125;

  // 自动订阅
  depend() &#123;
    if (Dep.target) &#123;
      this.addSub(Dep.target);
    &#125;
  &#125;

  // 发布订阅
  notify() &#123;
    this.subs.forEach((m) => &#123;
      m.update();
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，<code>subs</code>为我们的订阅者列表，有<code>添加订阅</code>、<code>删除订阅</code>、<code>自动订阅</code>和<code>发布订阅</code>这几个方法。我掐指一算，小伙伴们最疑惑的就是<code>target</code>这个静态变量了。别急，我们先在这里埋下一个伏笔，到后面再来解释这个<code>target</code>究竟是何方神圣。我们还是回到劫持对象的那个方法中，为我们创建的每一个<code>频道</code>来创建一个<code>订阅者列表</code>：</p>
<p><strong>Vue.js</strong></p>
<pre><code class="copyable">import Dep from "./Dep";

export default class Vue &#123;
  constructor(option) &#123;
    this._init(option);
  &#125;
&#125;

Vue.prototype._init = function (option) &#123;
  const vm = this;

  vm.$el = document.querySelector(option.el); // 项目根节点
  vm.$data = option.data(); // data对象

  // 劫持data对象
  vm.defineReactive(vm.$data);

  // 测试方法 - 监听input输入
  const input = document.getElementById("ceshi");
  vm.$data.val; // 试着读取一下值
  input.addEventListener(
    "input",
    (e) => &#123;
      vm.$data.val = e.target.value; // 赋值操作
    &#125;,
    false
  );
&#125;;

Vue.prototype.defineReactive = function (obj) &#123;
  if (!(obj instanceof Object)) return;
  // 遍历对象
  for (let key in obj) &#123;
    let val = obj[key]; // 赋值
    const dep = new Dep();
    Object.defineProperty(obj, key, &#123;
      enumerable: true, // 是否可枚举
      configurable: true, // 是否可配置
      get() &#123;
        console.log(`get：$&#123;key&#125; - $&#123;val&#125;`);
        dep.depend(); // 订阅
        return val;
      &#125;,
      set(newVal) &#123;
        if (newVal === val) return;
        console.log(`set：$&#123;key&#125; - $&#123;newVal&#125;`);
        val = newVal;
        dep.notify(); // 发布
      &#125;,
    &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>既然<code>频道</code>已经创建好了，那么我们是时候要创建<code>观众</code>了。</p>
<h3 data-id="heading-8">创建观众 - Watcher</h3>
<p>我们在<code>core</code>文件夹下创建一个<code>Watcher.js</code>的文件，用来存放我们的<code>Watcher</code>构造函数。</p>
<p><strong>Watcher.js</strong></p>
<pre><code class="copyable">import Dep from './Dep';

export default class Watcher &#123;
  constructor(obj, key, cb) &#123;
    this._data = obj; // data对象
    this.key = key; // 频道
    this.cb = cb; // 副作用函数
    this.get();
  &#125;

  // 订阅频道
  get() &#123;
    Dep.target = this;
    this._data[this.key]; // 触发data的get方法，进行自动订阅
    Dep.target = null;
  &#125;

  // 更新订阅
  update() &#123;
    const newVal = this._data[this.key];
    this.cb(newVal);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看了上面的代码，仔细的小伙伴就看到了一个东西，我们的老朋友<code>target</code>。分析一下<code>Watcher</code>这个构造函数，初始化的时候把<code>频道</code>传入：<code>data</code>对象以及具体的属性<code>key</code>，<code>data[key]</code>就是我们具体的<code>频道</code>了。而<code>cb</code>则是我们的副作用函数，用来在<code>频道</code>发布内容后，调用这个函数去更新我们的主页（主页长啥样子只有自己知道，所以<code>cb</code>由每个订阅者提供）。接着，自己调用了一下<code>get</code>方法。</p>
<p>我们来详细解剖一下这个<code>get</code>方法的逻辑，首先，它把<code>Dep</code>构造函数的静态变量<code>target</code>赋值为了自己，也就是自己这个<code>观众</code>，赋值过去的意义是什么呢？</p>
<p>我们回到<code>Dep</code>函数，发现<code>target</code>只被用在了<code>depend</code>方法里。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75394e58fb314ed4bc3485c107eb2779~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么<code>depend</code>又是何时被调用的呢？我们回到<code>Vue.js</code>中，在劫持<code>data</code>对象的方法里，找到了<code>depend</code>的调用时机，在执行每个<code>频道</code>的<code>get</code>方法时被调用的：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a6616d1dffa423397117085575a7cd0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哦，到这里链路都通了，我们再回过头来捋一下<strong>Watcher里自执行的get函数</strong>的逻辑：</p>
<ol>
<li>
<p><strong>Dep.target = this</strong>：当创建一个<code>观众</code>（new 一个 Watcher）时，它会内部自行调用一个订阅频道的方法，这个方法先把自己（this）存放到<code>Dep.target</code>里。</p>
</li>
<li>
<p><strong>this._data[this.key]</strong>：而紧接着调用了一下该<code>频道</code>（也就是<code>this._data[this.key]</code>），又因为<code>频道</code>被劫持了，调用的时候会自动触发<code>Object.defineProperty 的 get方法</code>，而去通知<code>订阅者列表</code>去执行自动订阅。又因为此时<code>Dep.target</code>已经存在了这个<code>观众</code>，它就真正的被<code>addSubs</code>进了<code>订阅者列表</code>中了。</p>
</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75394e58fb314ed4bc3485c107eb2779~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li><strong>Dep.target = null</strong>：到最后初始化<code>Dep.target</code>。</li>
</ol>
<p>到现在为止，<code>发布-订阅</code>的类都已经创建完毕了，链路也都已经打通了，那么我们写个列子来验证一下。</p>
<h3 data-id="heading-9">验证一下</h3>
<p>我们先在<code>index.html</code>中创建一个<code>p标签</code>，把它当成一个<code>watcher - 观众</code>。</p>
<p><strong>index.html</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>

<head>
  <title>简易vue</title>
  <meta charset="UTF-8">
</head>

<body>
  <div id="app">
    <input type="text" id="ceshi">
    <p id="watcher"></p>
  </div>

  <script src="./src/main.js"></script>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再完善一下<code>Vue.js</code>里的测试方法：</p>
<p><strong>Vue.js</strong></p>
<pre><code class="copyable">import Dep from "./Dep";
import Watcher from "./Watcher";

export default class Vue &#123;
  constructor(option) &#123;
    this._init(option);
  &#125;
&#125;

Vue.prototype._init = function (option) &#123;
  const vm = this;

  vm.$el = document.querySelector(option.el); // 项目根节点
  vm.$data = option.data(); // data对象

  // 劫持data对象
  vm.defineReactive(vm.$data);

  // 测试方法 - 监听input输入
  const input = document.getElementById("ceshi");
  input.addEventListener(
    "input",
    (e) => &#123;
      vm.$data.val = e.target.value; // 赋值操作
    &#125;,
    false
  );
  // 获取观众
  const watcher = document.getElementById("watcher");
  // 新建观众
  // 这里订阅的是 val 这个频道
  new Watcher(vm.$data, "val", (newVal) => &#123;
    watcher.innerHTML = newVal;
  &#125;);
&#125;;

Vue.prototype.defineReactive = function (obj) &#123;
  if (!(obj instanceof Object)) return;
  // 遍历对象
  for (let key in obj) &#123;
    let val = obj[key]; // 赋值
    const dep = new Dep();
    Object.defineProperty(obj, key, &#123;
      enumerable: true, // 是否可枚举
      configurable: true, // 是否可配置
      get() &#123;
        console.log(`get：$&#123;key&#125; - $&#123;val&#125;`);
        dep.depend(); // 订阅
        return val;
      &#125;,
      set(newVal) &#123;
        if (newVal === val) return;
        console.log(`set：$&#123;key&#125; - $&#123;newVal&#125;`);
        val = newVal;
        dep.notify(); // 发布
      &#125;,
    &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok，到这里我们来试一下最终的效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44eecea624804485ad9c3edd523ebc11~tplv-k3u1fbpfcp-watermark.image" alt="qwe.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">结语</h2>
<p>到现在为止，我们实现了一个简单的<code>数据双向绑定</code>，它通过<code>发布-订阅</code>模式来实现。但是，我们再想想，他是不是缺少了点什么东西。一开始说好的<code>v-bind</code>、<code>&#123;&#123;&#125;&#125;双括号</code>呢？别急，这里我们先实现一个<code>青春阳光版本</code>，下一篇文章再来实现<code>v-bind</code>、<code>&#123;&#123;&#125;&#125;双括号</code>的模板编译以及监听属性为对象时的变化。希望看到这里有收获的小伙伴能点个赞点个关注，感谢小伙伴们的支持~</p></div>  
</div>
            