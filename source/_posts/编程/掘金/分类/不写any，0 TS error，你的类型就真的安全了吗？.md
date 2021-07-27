
---
title: '不写any，0 TS error，你的类型就真的安全了吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4349'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 04:46:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=4349'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>TS能起到错误前置的作用，但是不正确地使用TS就不能保证，比如初学者经常会写any甚至会放任一些TS error，这不在讨论范围内。我们要讨论的是即使你能做到不写any，没有任何TS error，看上去很安全的代码，真的就能起到TS的错误前置，避免运行时报错导致的组件挂掉甚至页面白屏的作用吗？<br>
答案当然是否定的，我们下面看看经典的不正确使用TS的案例。</p>
<h2 data-id="heading-1">1.objArr[index].key</h2>
<pre><code class="copyable">// 危险的
interface IName &#123;
    name: string;
&#125;

let names: IName[] | undefined;

// 这样是不会标红的，但是实际运行时很可能会报错，因为显然obj?.[2]可能是undefined类型。
names?.[2].name;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这其实是很危险的，因为一旦报错页面白屏是不可接受的。</p>
<p>那么如何避免呢？就是对象数组在下标取值后用一个变量表示而不是直接取值。</p>
<pre><code class="copyable">// 安全的
interface IName &#123;
    name: string;
&#125;

let names: IName[] | undefined;

const thirdName = names?.[2];

// 这样会标红，并且正常选name字段VSCode会帮你自动补上?
thirdName.name
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2.obj.key.grandsonKey操作时，key的类型声明信任了外界传入的值是在key list范围内导致的问题</h2>
<pre><code class="copyable">const object = &#123;
    a: &#123;
        c: 'c'
    &#125;,
    b: &#123;
        c: 'c'
    &#125;,
&#125;;

// key是外界传来的参数，我们错误地信任了key只可能是'a'或'b'
function foo(key: keyof typeof object) &#123;
    const d = object[key].c;
&#125;

// @ts-ignore
// 然后调用方却传了个'c'，于是在foo函数第一行就gg了整个作用域内的代码挂掉，而且如果没有catch住错误，整个页面都会白调。
foo('c');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过，仅仅指出了问题是不够的，这种情况如何避免呢？这个方案仅供参考，并不是最优解。</p>
<pre><code class="copyable">interface IC &#123;
    c: string;
&#125;

const object: Record<string, IC | undefined> = &#123;
    a: &#123;
        c: 'c'
    &#125;,
    b: &#123;
        c: 'c'
    &#125;,
&#125;;

// key是外界传来的参数, 我们不信任它, 从类型上就兼容undefined或其他情况
function foo(key?: string) &#123;
    const d = key ? object[key]?.c : 'default';
&#125;

foo('c');
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3.obj.key.grandsonKey操作时，key信任了外界必传导致的问题</h2>
<pre><code class="copyable">interface Iter &#123;
    key: &#123;
       grandsonKey: string;
    &#125;;
&#125;

// object是外界传进来的参数，我们错误地信任了key是必传参数
function foo(object: Iter) &#123;
    const a = object.key.grandsonKey;
&#125;

// 实际传的数据, 造成
const object = &#123;&#125; as Iter;
foo(object);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">进一步思考</h2>
<p>在例子2中，我这的解决方案是把类型定的范围更大来让我们的代码没有处理这么大范围时会标红，这样确实能解决很关键问题，即运行时报错。</p>
<p>要知道运行时报错是很严重的问题，如果你没有捕获错误，或者用errorBoundary设置错误边界就会导致页面白屏，如果影响面大这就是P0事故了（即使上游异常数据的制造者的锅会大一些）。</p>
<p>即使有errorBoundary，但是如果说一个组件直接展示了组件出错了这种default文案，也并不能说是精细的错误处理，最理想的错误处理我们要考虑这个异常数据是不是可以兼容的，比如给个默认值，保证整个程序正常运作。</p>
<p>而话说回来，我们用一个更大范围的类型定义<code>'a' | 'b' → string | undefined</code> 确实可以让TS对未兼容代码提出错误，从而促使我们把异常数据转为正常数据，保证程序正常运转而不是抛出错误。</p>
<p>但是这个方案却被大佬否了，因为这样做在解决问题的同时又带来了另一个问题就是调用者不知道我该传什么了。</p>
<p>比如例子2中的<code>foo</code>函数我们暴露给业务方使用，业务方本来知道他应该传<code>'a' | 'b'</code>类型的参数，但是在我们因为不信任参数改为<code>string | undefined</code> 类型后，调用者只知道要传string，甚至似乎不传也行，但是实际上呢，不传仅仅是兼容了，能跑，但是绝对不会得到预期的结果的。</p>
<p>所以我的最新思路是这种要暴露给外界使用的场景，要搞一个接入层，接入层的功能是提供正常的接口定义，让调用者可以知道函数的设计意图。</p>
<p>在接入层并不定义处理函数，而是引入并调用兼容层的函数，并且参数直接透传原数据。</p>
<p>在兼容层我们的函数参数采用完全不信任的策略，如每条属性都设为非必传的、不枚举，都设为字符串等。这样能保证我们在使用时会做充分的兼容。</p>
<p>在消费层我们真正定义处理函数，接受的参数和接入层一致，因为异常数据都已经被兼容层处理了，所以可以放心使用。</p>
<p>当然这只是一个初步设想，还没有真正落地，欢迎大家指出自己的看法或者给出更好的解决方案。</p></div>  
</div>
            