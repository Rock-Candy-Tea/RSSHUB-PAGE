
---
title: '一个闯关游戏相关的算法总结：js判断一个数是否在一个区间内或者是否等于它'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f331565bd84775a582002689a452c6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 03:04:56 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f331565bd84775a582002689a452c6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">业务场景</h2>
<p>此算法源于项目中要实现一个下单闯关业务，根据用户累计的下单金额，判断用户目前处于哪一关，解锁对应的福利</p>
<p>游戏的步骤与金额都配置在前端，每一关对应一个累计金额，总共4关（多少关都无所谓，主要是思路哈哈）</p>
<h3 data-id="heading-1">思路</h3>
<p>用数组数据结构存储用户每关的累计金额数，根据用户当前的累计金额总数判断用户所处的关卡</p>
<p>let step=[1000, 2500, 5000, 7000, 10000, 12500, 15000, 20000]</p>
<p>比如：：</p>
<p>当用户累计是100元，100<1000，关卡未解锁，在第一关处提醒用户所差的金额；</p>
<p>当累计1000元，1000==1000,此时第一关已处于解锁状态，需要在第二关处提醒用户离解锁第二关所差的金额；</p>
<p>当累计2600时，2600>2500，第二关卡已解锁，需在第三关处提醒用户，离解锁第三关所差的金额数；</p>
<p>以此类推......</p>
<h3 data-id="heading-2">效果图</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f331565bd84775a582002689a452c6~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210521182644.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由此可见，还缺少一个标识，记录用户此关是否已通过。设置一个isOver属性，如果金额大于等于此关的金额数，则此关为通过状态，isOver=true</p>
<h3 data-id="heading-3">继续思路整理</h3>
<p>一开始觉得要用用户的累计金额在数组每个元素的前后作个判断，后来发现只要做一个过滤即可，过滤出小于等于累计金额的数组元素，求其数组的长度就是用户所处的关卡数，然后根据用户是否已通过所处的关卡，设置下一关的提示。</p>
<h3 data-id="heading-4">实现代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//根据累积金额算出所处的关卡</span>
<span class="hljs-function"><span class="hljs-title">_onStep</span>(<span class="hljs-params">num</span>)</span> &#123;
        <span class="hljs-keyword">let</span> stepData = [<span class="hljs-number">1000</span>, <span class="hljs-number">2500</span>, <span class="hljs-number">5000</span>, <span class="hljs-number">7000</span>, <span class="hljs-number">10000</span>, <span class="hljs-number">12500</span>, <span class="hljs-number">15000</span>, <span class="hljs-number">20000</span>]
        <span class="hljs-keyword">let</span> step = stepData.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item <= num).length
        <span class="hljs-keyword">return</span> step || <span class="hljs-number">1</span> <span class="hljs-comment">//当小于第一关的金额1000元时，符合条件的元素为空，长度是0，手动设置处于第一关卡的位置</span>
    &#125;,


<span class="hljs-comment">//处理数据，用作页面结果渲染</span>
<span class="hljs-function"><span class="hljs-title">_initStep</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">let</span> &#123; payMoney=<span class="hljs-number">0</span>&#125;=<span class="hljs-built_in">this</span>.$route.query  <span class="hljs-comment">//用户累计金额</span>
  <span class="hljs-comment">//用对象数据结构，方便读取并设置每一关的值，对象存储比数组存储更节省内存，虽然也没多少数据哈哈</span>
      <span class="hljs-keyword">let</span> stepData= stepData: &#123;
        <span class="hljs-number">1</span>:&#123;<span class="hljs-comment">//第一关</span>
          <span class="hljs-attr">step</span>:<span class="hljs-string">'one'</span>,  <span class="hljs-comment">//为设置每一关图标所处的不同位置class类</span>
          <span class="hljs-attr">num</span>:<span class="hljs-number">1000</span>,    <span class="hljs-comment">//每关的关卡金额数</span>
          <span class="hljs-attr">tip</span>:<span class="hljs-string">''</span>,      <span class="hljs-comment">//关卡提示</span>
          <span class="hljs-attr">isOver</span>:<span class="hljs-literal">false</span> <span class="hljs-comment">//是否已通过本关</span>
        &#125;,
        <span class="hljs-number">2</span>:&#123;<span class="hljs-comment">//第二关</span>
          <span class="hljs-attr">step</span>:<span class="hljs-string">'two'</span>,
          <span class="hljs-attr">num</span>:<span class="hljs-number">2500</span>,
          <span class="hljs-attr">tip</span>:<span class="hljs-string">''</span>,
          <span class="hljs-attr">isOver</span>:<span class="hljs-literal">false</span>
        &#125;,
       <span class="hljs-number">3</span>: &#123;<span class="hljs-comment">//第三关</span>
          <span class="hljs-attr">step</span>:<span class="hljs-string">'three'</span>,
          <span class="hljs-attr">num</span>:<span class="hljs-number">5000</span>,
          <span class="hljs-attr">tip</span>:<span class="hljs-string">''</span>,    
          <span class="hljs-attr">isOver</span>:<span class="hljs-literal">false</span>
        &#125;,
        <span class="hljs-number">4</span>: &#123;<span class="hljs-comment">//第四关</span>
          <span class="hljs-attr">step</span>:<span class="hljs-string">'four'</span>,
          <span class="hljs-attr">num</span>:<span class="hljs-number">7000</span>,
          <span class="hljs-attr">tip</span>:<span class="hljs-string">''</span>,         
          <span class="hljs-attr">isOver</span>:<span class="hljs-literal">false</span>
        &#125;]
      payMoney=<span class="hljs-built_in">parseFloat</span>(payMoney)
      <span class="hljs-keyword">let</span> step=<span class="hljs-built_in">this</span>._onStep(payMoney)
      step=<span class="hljs-built_in">Number</span>(step)
      
      <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> stepData)&#123;
        <span class="hljs-keyword">if</span>(key<=step)&#123;
          <span class="hljs-keyword">let</span> flag=payMoney>=stepData[key].num
          stepData[key].isOver=flag
          stepData[key].tip=flag?<span class="hljs-string">''</span>:<span class="hljs-string">`距离奖励仍差：¥ <span class="hljs-subst">$&#123; <span class="hljs-built_in">this</span>._handleFloat(stepData[key].num-payMoney)&#125;</span>元`</span>
        &#125;
      &#125;
      <span class="hljs-comment">//当用户通过当前关卡时，设置好下一关卡的提示信息</span>
      <span class="hljs-keyword">if</span>(step<<span class="hljs-number">8</span>&&stepData[step].isOver)&#123;
        <span class="hljs-keyword">let</span> next=<span class="hljs-built_in">Number</span>(step)+<span class="hljs-number">1</span>
        stepData[next].tip= <span class="hljs-string">`距离奖励仍差：¥ <span class="hljs-subst">$&#123; <span class="hljs-built_in">this</span>._handleFloat(stepData[next].num-payMoney) &#125;</span>元`</span>
      &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">_handleFloat</span>(<span class="hljs-params">number</span>)</span>&#123;
      <span class="hljs-keyword">if</span>(!number) <span class="hljs-keyword">return</span> 
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">parseFloat</span>(number).toFixed(<span class="hljs-number">2</span>)
    &#125;,


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">总结</h3>
<p>前端会在本次存储用户下单的累计金额（是调用后台接口后存储在本地storage中），下次进入页面时获取后台最新的累计金额跟前端本地的作比较，后台>本地 时，提醒用户所处的关卡数
挺好玩的一种业务类型，用到了一个数组算法，已知一个数值，判断在数组中所处的位置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">_onStep</span>(<span class="hljs-params">num</span>)</span> &#123;
            <span class="hljs-keyword">let</span> stepData = [<span class="hljs-number">1000</span>, <span class="hljs-number">2500</span>, <span class="hljs-number">5000</span>, <span class="hljs-number">7000</span>, <span class="hljs-number">10000</span>, <span class="hljs-number">12500</span>, <span class="hljs-number">15000</span>, <span class="hljs-number">20000</span>]
            <span class="hljs-keyword">let</span> step = stepData.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item <= num).length
            <span class="hljs-keyword">return</span> step || <span class="hljs-number">1</span> 
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最近公司比较忙，趁着稍有空闲，积累下所做的，有所学，有所得，每天都进步~~~ 加油！</p></div>  
</div>
            