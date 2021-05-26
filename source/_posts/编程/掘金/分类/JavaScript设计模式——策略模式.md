
---
title: 'JavaScript设计模式——策略模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9385'
author: 掘金
comments: false
date: Tue, 25 May 2021 03:11:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=9385'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>策略模式：封装一系列算法策略，并使他们之间可以相互替换</p>
</blockquote>
<p>在说策略模式之前，我们先简述一下两个基本概念：</p>
<ul>
<li>环境类（Context）：负责接收用户请求，并派发给策略算法执行</li>
<li>策略类（Strategy）：策略算法具体实现，接收环境类派发的计算请求，并返回计算结果</li>
</ul>
<h3 data-id="heading-0">Question</h3>
<p>根据员工绩效等级，实现一个员工奖金计算算法</p>
<pre><code class="copyable">S => 4 * 月薪
A => 3 * 月薪
B => 2 * 月薪
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">直观实现</h3>
<p>当我们拿到上面的问题，直观想法当然是逻辑判断。如</p>
<pre><code class="copyable">const calculateBonus = (performanceLevel, salary) => &#123;
  if (performanceLevel === 'S') &#123;
    return salary * 4
  &#125;
  if (performanceLevel === 'A') &#123;
    return salary * 3
  &#125;
  if (performanceLevel === 'B') &#123;
    return salary * 2
  &#125;
  return salary
&#125;

calculateBonus('S', 10000)
calculateBonus('A', 5000)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，这样写很直观，也很好理解。但是拓展性不强，假如策略变了，新增一个'C'绩效，那就不得不修改计算函数了</p>
<h3 data-id="heading-2">策略模式实现</h3>
<p>在JavaScript中实现策略模式再简单不过了，可能我们实际开发中已经多次使用，只是没特别留意。如</p>
<pre><code class="copyable">const Strategy = &#123;
  S: (salary) => salary * 4,
  A: (salary) => salary * 3,
  B: (salary) => salary * 2,
&#125;

const calculateBonus = (performanceLevel, salary) => &#123;
  return Strategy[performanceLevel](salary)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>calculateBonus：环境类，策略模式中不变的部分；</li>
<li>Strategy：策略类，算法具体实现过程；</li>
</ul>
<p>当然，我们也可以采用class实现</p>
<pre><code class="copyable">class StrategyS &#123;
  constructor(salary) &#123;
    this.salary = salary
  &#125;
  calculate() &#123;
    return this.salary * 4
  &#125;
&#125;

class StrategyA &#123;
  constructor(salary) &#123;
    this.salary = salary
  &#125;
  calculate() &#123;
    return this.salary * 3
  &#125;
&#125;

class StrategyB &#123;
  constructor(salary) &#123;
    this.salary = salary
  &#125;
  calculate() &#123;
    return this.salary * 2
  &#125;
&#125;

class Bonus &#123;
  strategy = null
  setStrategy(strategy) &#123;
    this.strategy = strategy
  &#125;
  getBonus() &#123;
    return this.strategy.calculate()
  &#125;
&#125;

const bonus = new Bonus()
bonus.setStrategy(new StrategyS(10000))
bonus.getBonus()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>策略模式就是把不变的部分（策略派发）和算法部分抽离开，方便策略新增和替换，增强代码弹性</p>
<h3 data-id="heading-3">总结</h3>
<h5 data-id="heading-4">优点</h5>
<ul>
<li>利用代码组合，有效避免多重条件判断；</li>
<li>代码可服用，易拓展易组合；</li>
</ul>
<h5 data-id="heading-5">缺点</h5>
<ul>
<li>相比直接编写业务逻辑，策略模式会适当增加代码量，主要集中在策略算法；</li>
<li>需要很清晰业务逻辑和策略算法，并准确抽离算法实现过程</li>
</ul></div>  
</div>
            