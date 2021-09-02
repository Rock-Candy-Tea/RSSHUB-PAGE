
---
title: 'VIte + Vue3 + ElementPlus仿写掘金抽奖'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a0791d867ec49849c672c2d4225fe3a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 05:27:49 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a0791d867ec49849c672c2d4225fe3a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>字节跳动前端青训营大作业</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchanglin2569%2FByteDanceTask" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/changlin2569/ByteDanceTask" ref="nofollow noopener noreferrer">Github项目地址</a></p>
<p>使用vite + vue3 来初始化项目</p>
<p>为什么选择vite呢</p>
<ol>
<li>快速启动，<code>Vite</code> 会在本地启动一个开发服务器，来管理开发环境的资源请求</li>
<li>无需打包，热更新更快</li>
<li>原生ES module 需要什么就引入什么</li>
</ol>
<pre><code class="hljs language-node copyable" lang="node">$ npm init vite-app <project-name> 
$ cd <project-name> //进入项目目录 
$ npm install //安装项目所需依赖 
$ npm run dev //启动项目
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的项目目录</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a0791d867ec49849c672c2d4225fe3a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们进入src的components目录下创建组件</p>
<h3 data-id="heading-0">Home组件</h3>
<p><strong>Home组件主要负责页面的框架与初始展示</strong></p>
<h3 data-id="heading-1">LuckDraw组件</h3>
<p><strong>LuckDraw组件主要展示抽奖与中将列表组件</strong></p>
<p>具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>掘金幸运抽奖<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left_box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left_header"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"count"</span>></span>
            当前矿石数：<span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; money &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123; sign: true, signed: isSign &#125;"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"signHandle"</span>></span>
            &#123;&#123; isSign ? "已签到" : "签到" &#125;&#125;
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"panel"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Lotterypanel</span>
            <span class="hljs-attr">:money</span>=<span class="hljs-string">"money"</span>
            @<span class="hljs-attr">updateMoney</span>=<span class="hljs-string">"updateMoney"</span>
            @<span class="hljs-attr">getPrizeHandle</span>=<span class="hljs-string">"getPrizeHandle"</span>
          ></span><span class="hljs-tag"></<span class="hljs-name">Lotterypanel</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right_box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Prizes</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"wonPrizes"</span>></span><span class="hljs-tag"></<span class="hljs-name">Prizes</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; reactive, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> Lotterypanel <span class="hljs-keyword">from</span> <span class="hljs-string">"./../Lotterypanel/Lotterypanel.vue"</span>;
<span class="hljs-keyword">import</span> Prizes <span class="hljs-keyword">from</span> <span class="hljs-string">"./../Prizes/Prizes.vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> money = ref(<span class="hljs-number">400</span>);
    <span class="hljs-keyword">const</span> isSign = ref(<span class="hljs-literal">false</span>);
    <span class="hljs-comment">// 触发签到事件</span>
    <span class="hljs-keyword">const</span> signHandle = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (isSign.value) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      money.value += <span class="hljs-number">200</span>;
      isSign.value = <span class="hljs-literal">true</span>;
    &#125;;

    <span class="hljs-keyword">const</span> updateMoney = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      money.value -= <span class="hljs-number">200</span>;
    &#125;;

    <span class="hljs-comment">// 抽中的奖品</span>
    <span class="hljs-keyword">const</span> wonPrizes = reactive([]);
    <span class="hljs-keyword">const</span> getPrizeHandle = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">prize</span>) </span>&#123;
      <span class="hljs-keyword">const</span> [date] = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().toLocaleString().split(<span class="hljs-string">" "</span>);
      wonPrizes.push(&#123;
        ...prize,
        date,
      &#125;);
    &#125;;
    <span class="hljs-keyword">return</span> &#123;
      money,
      isSign,
      signHandle,
      updateMoney,
      wonPrizes,
      getPrizeHandle,
    &#125;;
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
    Lotterypanel,
    Prizes,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span>
 .......省略
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，分别定义money与isSign来百事初始矿石数量与是否签到，初始矿石数量400，默认没有签到；在签到按钮上绑定签到事件，签到后money值增加200且isSign为true。
<strong>wonPrizes</strong>表示抽中的奖品列表，引入Prizes组件展示奖品列表，将wonPrizes作为props传递给Prizes子组件进行展示</p>
<p><strong>将money传递给Lotterypanel组件（完成具体抽奖逻辑）用于判断剩余矿石数是否可以抽奖，自定义事件updateMoney与getPrizeHandle分别用于获取抽奖后的最新矿石数和获得的奖品</strong></p>
<p>下面来到重头戏，<strong>Lotterypanel组件</strong></p>
<h3 data-id="heading-2">Lotterypanel组件（抽奖逻辑实现）</h3>
<p>先上代码</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item-box"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;
          item,
          btn: item.id === 8 || count === item.id,
        &#125;"</span>
        <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in prizeList"</span>
        <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.id"</span>
      ></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.id !== 8"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"item.img"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"luckDrawHandle"</span> <span class="hljs-attr">v-else</span>></span>抽奖<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; item.price ? `$&#123;item.price&#125;/次` : item.name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- <Toast></Toast> --></span>
    <span class="hljs-tag"><<span class="hljs-name">el-dialog</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"恭喜您中将了！"</span>
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"prizeDialogVisible"</span>
      <span class="hljs-attr">width</span>=<span class="hljs-string">"30%"</span>
      @<span class="hljs-attr">close</span>=<span class="hljs-string">"count = -1"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"own-prize"</span>></span>
        <span class="hljs-comment"><!-- <div class="img-box">
          <img :src="ownPrize.img" alt="" />
        </div> --></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"prize-name"</span>></span>&#123;&#123; ownPrizeName &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">footer</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dialog-footer"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"prizeDialogVisible = false"</span>></span>取 消<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"prizeDialogVisible = false"</span>
            ></span>确 定</el-button
          >
        <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-dialog</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> &#123; prizeList &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../utils/prizeList"</span>;
<span class="hljs-comment">// import Toast from "./../common/Toast/Toast.vue";</span>
<span class="hljs-keyword">import</span> &#123; ElDialog, ElButton, ElMessage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"element-plus"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">money</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
    &#125;,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; emit &#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> count = ref(-<span class="hljs-number">1</span>);
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">money</span>: curMoney &#125; = toRefs(props);
    <span class="hljs-keyword">const</span> ownPrizeName = ref(<span class="hljs-string">""</span>); <span class="hljs-comment">// 获得奖品的名字</span>
    <span class="hljs-keyword">const</span> prizeDialogVisible = ref(<span class="hljs-literal">false</span>);

    <span class="hljs-comment">// 抽中的奖品</span>
    <span class="hljs-keyword">const</span> getPrize = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">id</span>) </span>&#123;
      <span class="hljs-keyword">const</span> [prize] = prizeList.filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.id == id);
      <span class="hljs-keyword">return</span> prize;
    &#125;;

    <span class="hljs-comment">// 中奖后</span>
    <span class="hljs-keyword">const</span> winPrize = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">val</span>) </span>&#123;
      <span class="hljs-keyword">const</span> ownPrize = getPrize(val);
      emit(<span class="hljs-string">"getPrizeHandle"</span>, ownPrize);
      ownPrizeName.value = ownPrize.name;
      prizeDialogVisible.value = !prizeDialogVisible.value;
    &#125;;
    <span class="hljs-comment">// 触发抽奖</span>
    <span class="hljs-keyword">const</span> luckDrawHandle = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (curMoney.value < <span class="hljs-number">200</span>) &#123;
        ElMessage(&#123;
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">"矿石不足，签到领取200矿石哦~"</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">"error"</span>,
        &#125;);
        <span class="hljs-keyword">return</span>;
      &#125;
      emit(<span class="hljs-string">"updateMoney"</span>);
      <span class="hljs-keyword">const</span> random = <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">100</span>;
      <span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>;
      <span class="hljs-keyword">let</span> timer;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_handle</span>(<span class="hljs-params"></span>) </span>&#123;
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          count.value += <span class="hljs-number">1</span>;
          <span class="hljs-keyword">if</span> (count.value > <span class="hljs-number">8</span>) &#123;
            count.value = <span class="hljs-number">0</span>;
          &#125;
          i++;
          <span class="hljs-keyword">if</span> (i > <span class="hljs-number">25</span> && prizeList[count.value].probability >= random) &#123;
            <span class="hljs-built_in">clearTimeout</span>(timer);
            winPrize(count.value);
          &#125; <span class="hljs-keyword">else</span> &#123;
            _handle();
          &#125;
        &#125;, i * <span class="hljs-number">10</span>);
      &#125;
      _handle();
    &#125;;
    <span class="hljs-keyword">return</span> &#123;
      count,
      prizeList,
      luckDrawHandle,
      prizeDialogVisible,
      ownPrizeName,
    &#125;;
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-comment">// Toast,</span>
    ElDialog,
    ElButton,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span>
 .......略
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>prizeList表示奖品池，支持自定义，目前写在前端，后期会进行更新到后端数据库中</strong></p>
<p>我们来看最重要的抽奖逻辑</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 触发抽奖</span>
    <span class="hljs-keyword">const</span> luckDrawHandle = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (curMoney.value < <span class="hljs-number">200</span>) &#123;
        ElMessage(&#123;
          <span class="hljs-attr">showClose</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">"矿石不足，签到领取200矿石哦~"</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">"error"</span>,
        &#125;);
        <span class="hljs-keyword">return</span>;
      &#125;
      emit(<span class="hljs-string">"updateMoney"</span>);
      <span class="hljs-keyword">const</span> random = <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">100</span>;
      <span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>;
      <span class="hljs-keyword">let</span> timer;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_handle</span>(<span class="hljs-params"></span>) </span>&#123;
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          count.value += <span class="hljs-number">1</span>;
          <span class="hljs-keyword">if</span> (count.value > <span class="hljs-number">8</span>) &#123;
            count.value = <span class="hljs-number">0</span>;
          &#125;
          i++;
          <span class="hljs-keyword">if</span> (i > <span class="hljs-number">25</span> && prizeList[count.value].probability >= random) &#123;
            <span class="hljs-built_in">clearTimeout</span>(timer);
            winPrize(count.value);
          &#125; <span class="hljs-keyword">else</span> &#123;
            _handle();
          &#125;
        &#125;, i * <span class="hljs-number">10</span>);
      &#125;
      _handle();
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>当点击抽奖按钮时，首先会检查当前拥有的矿石数，少于200则警告矿石数量不足，无法进行抽奖；当抽奖开始时，会先通知父组件更新最新的矿石数量，然后获取0-99的随机数，因为每个奖品有一个对应的probability属性（0-100的数）代表具有百分之多少的概率会被抽到，然后定义i（用于计数）与timer（用于最后暂停setTimeout）。count表示最终抽到的奖品id，在循环时回进行递增匹配不同的奖品（每次递增都对应着奖品id)</strong></p>
<p><strong>i每次约会进行递增1，每次延迟的时间 i * 100 这样速度便会越来越慢，最后的停止条件为i > 25且目前的奖品的抽中概率大于产生的随机数；这样就实现了随机抽奖且奖品抽中概率可控</strong></p>
<p>停止后，清除定时器并调用抽取成功的方法 winPrize 传入目前的count值，winPrize方法接受count值并获得对应的奖品通过自定义事件传递给父组件，并随后进行弹窗展示</p>
<p>父组件拿到抽中的奖品后传递给奖品展示组件进行展示</p>
<h3 data-id="heading-3">奖池</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> prizeList = reactive([
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'66矿石'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32ed6a7619934144882d841761b63d3c~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">100</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'随机限量徽章'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71c68de6368548bd9bd6c8888542f911~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">20</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'掘金新款T恤'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bf91038a6384fc3927dee294a38006b~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">20</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">7</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'BUG'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a4ce25d48b8405cbf5444b6195928d4~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">20</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">8</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'抽奖'</span>,
        <span class="hljs-attr">price</span>: <span class="hljs-number">200</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'乐高海洋巨轮'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aabe49b0d5c741fa8d92ff94cd17cb90~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">20</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">6</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'掘金马克杯'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab31c183950541d4a0731c0b8765b173~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">20</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">5</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'YoYo抱枕'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33f4d465a6a9462f9b1b19b3104c8f91~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">20</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">4</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'switch'</span>,
        <span class="hljs-attr">img</span>: <span class="hljs-string">'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4decbd721b2b48098a1ecf879cfca677~tplv-k3u1fbpfcp-no-mark:0:0:0:0.awebp'</span>,
        <span class="hljs-attr">probability</span>: <span class="hljs-number">20</span>
    &#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">手工设置奖池与中奖概率</h4>
<p><strong>直接替换数组中元素即可，需要注意的是 id 不要修改，中将概率为probability属性（0-100内的数字）代表百分之多少中奖概率</strong></p></div>  
</div>
            