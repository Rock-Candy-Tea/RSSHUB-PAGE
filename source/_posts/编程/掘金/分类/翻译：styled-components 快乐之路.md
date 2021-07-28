
---
title: '翻译：styled-components 快乐之路'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5465148476104ccbae4a9be8b8a466e2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 19:51:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5465148476104ccbae4a9be8b8a466e2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原作地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.joshwcomeau.com%2Fcss%2Fstyled-components%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.joshwcomeau.com/css/styled-components/" ref="nofollow noopener noreferrer">www.joshwcomeau.com/css/styled-…</a> <br>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.joshwcomeau.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.joshwcomeau.com/" ref="nofollow noopener noreferrer">Josh Comeau</a> <br>译：大力智能前端团队 粽粽</p>
</blockquote>
<p>几年来，在 React 应用里管理 CSS 的工具中， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fstyled-components.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://styled-components.com/" ref="nofollow noopener noreferrer">💅 styled-components</a> 一直是我最喜欢的。</p>
<p>styled-components 非常优秀，它在许多方面改变了我对 CSS 架构的看法，并帮助我保持代码仓库的干净整洁、模块清晰——这点像极了 React。</p>
<p>styled-components 与 React 还有一个共同点：一开始，很多人难以接受它们的理念 😅 。“每种样式都是一个组件” 的思路可能让人难以接受，就像“你的视图现在是用 XML/JS 混合编写的”。</p>
<p>也许正因如此，我发现许多开发人员从未认真接受 styled-components。开发者们虽然把在项目中引入它，但没有更新自己关于样式的思维模型<sup>[1]</sup>。浅入浅出的心态使他们与工具的最佳实践失之交臂。</p>
<p>如果你使用 styled-components，或者类似的工具，比如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Femotion.sh%2Fdocs%2Fintroduction" target="_blank" rel="nofollow noopener noreferrer" title="https://emotion.sh/docs/introduction" ref="nofollow noopener noreferrer">Emotion</a>，我希望这篇文章能帮助你充分利用它们。我已经将多年的实验和实践提炼成一些实用的技巧和技术。如果你将这些经验应用得当，相信我，你一定能更快乐地编写 css✨。</p>
<p><strong>目标读者</strong></p>
<p>本文主要面向已经在使用 styled-components 或其他 CSS-in-JS 解决方案（如 Emotion）的、不论是刚入门还是经验丰富的 React 开发人员。</p>
<p>本文不打算作为 styled-components 的介绍，也不打算将其与其他工具进行比较或对比。</p>
<h1 data-id="heading-0">CSS 变量</h1>
<p>让我们从一个有趣的例子开始。</p>
<p>假设我们有一个背景组件，它具有透明度和颜色属性：</p>
<pre><code class="copyable">function Backdrop(&#123; opacity, color, children &#125;) &#123;
  return (
    <Wrapper>
      &#123;children&#125;
    </Wrapper>
  )
&#125;

const Wrapper = styled.div`
  /* 省略 */
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何将这些属性应用于 <code>Wrapper</code>？</p>
<p>一种方法是使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstyled-components.com%2Fdocs%2Fbasics%23adapting-based-on-props" target="_blank" rel="nofollow noopener noreferrer" title="https://styled-components.com/docs/basics#adapting-based-on-props" ref="nofollow noopener noreferrer">插值函数</a>：</p>
<pre><code class="copyable">function Backdrop(&#123; opacity, color, children &#125;) &#123;
  return (
    <Wrapper opacity=&#123;opacity&#125; color=&#123;color&#125;>
      &#123;children&#125;
    </Wrapper>
  )
&#125;

const Wrapper = styled.div`
  opacity: $&#123;p => p.opacity&#125;;
  background-color: $&#123;p => p.color&#125;;
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的代码可以起作用，但有一些小问题。该段代码运行过程中，每当属性的值改变时，styled-components 会生成新的类名，并将其重新注入文档的 <code><head></code> 。这样做，有时候存在性能问题（例如：执行 JS 动画）。</p>
<p>要解决这个问题，还有另一种方法 —— 使用 CSS 变量：</p>
<pre><code class="copyable">function Backdrop(&#123; opacity, color, children &#125;) &#123;
  return (
    <Wrapper
      style=&#123;&#123;
        '--color': color,
        '--opacity': opacity,
      &#125;&#125;
    >
      &#123;children&#125;
    </Wrapper>
  )
&#125;

const Wrapper = styled.div`
  opacity: var(--opacity);
  background-color: var(--color);
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS 变量能不断挖掘出新玩法。如果你不确定这里发生了什么，我的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.joshwcomeau.com%2Fcss%2Fcss-variables-for-react-devs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.joshwcomeau.com/css/css-variables-for-react-devs/" ref="nofollow noopener noreferrer">React 开发中的 CSS 变量</a> 会帮助你理解它（同时你还会学到一些其他的技巧！）。</p>
<p>我们还可以使用 CSS 变量来指定默认值：</p>
<pre><code class="copyable">function Backdrop(&#123; opacity, color, children &#125;) &#123;
  return (
    <Wrapper
      style=&#123;&#123;
        '--color': color,
        '--opacity': opacity,
      &#125;&#125;
    >
      &#123;children&#125;
    </Wrapper>
  )
&#125;

const Wrapper = styled.div`
  opacity: var(--opacity, 0.75);
  background-color: var(--color, var(--color-gray-900));
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们使用 <code><Backdrop></code> 时没有指定透明度或颜色，将使用 75% 透明度，以及主题颜色中的深灰色作为默认值。</p>
<p>这种指定属性值的方式感觉很好。它并没有改变游戏规则，却给我带来了一些乐趣。</p>
<p>而这仅仅是个开始，让我们看一些更有意义的东西。</p>
<h1 data-id="heading-1">样式的单一来源</h1>
<p>如果通过本文只能让你学会一个技巧，那一定是这条。这才是一个真正的宝藏。</p>
<p>在这篇文章中，我有一个 <code>TextLink</code> 组件。它看起来是这样的：</p>
<pre><code class="copyable">const TextLink = styled.a`
  color: var(--color-primary);
  font-weight: var(--font-weight-medium);
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是用于文章正文内链接的组件。下面是原博客文章中的一个例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5465148476104ccbae4a9be8b8a466e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在我的博客上，我有一个用于提供额外信息的 <code>Aside</code> 组件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba10aebf988e4d48b6efcaa6d485be7b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这个 <code>Aside</code> 中，“an included link”是用 <code>TextLink</code> 呈现的，它与正文中的 <code>TextLink</code> 是非常相似的组件。不过，我想应用一些不同的样式——我不喜欢蓝色背景上的蓝色文字。</p>
<p>这就是所谓的“上下文样式”的概念：相同的组件根据其上下文更改外观。当你在 <code>Aside</code> 中使用 <code>TextLink</code> 时，会添加/替换一些样式。</p>
<p>针对这种场景，你会怎么解决这个问题呢？我经常看到这样的代码：</p>
<pre><code class="copyable">// Aside.js
const Aside = (&#123; children &#125;) => &#123;
  return (
    <Wrapper>
      &#123;children&#125;
    </Wrapper>
  );
&#125;

const Wrapper = styled.aside`
  /* 基础样式 */
  a &#123;
    color: var(--color-text);
    font-weight: var(--font-weight-bold);
  &#125;
`;

export default Aside;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在我看来，这是非常不可取的写法。这使得样式回溯在我们的应用中变得非常困难 —— 如何才能知道 <code>TextLink</code> 被设置了哪些样式呢？对 <code>TextLink</code> 进行项目范围内的搜索并不可行，你得用 <code>grep</code> 搜索 <code>a</code> 才行，祝你好运。如果我们不知道 <code>Aside</code> 应用了这些样式，我们将永远无法预测 <code>TextLink</code> 的表现。</p>
<p>那么，正确的方法是什么?也许你已经考虑过使用 <code>TextLink</code> 代替 <code>a</code> 来指定这些样式：</p>
<pre><code class="copyable">// Aside.js
import TextLink from '../TextLink'

const Aside = (&#123; children &#125;) => &#123; /* 省略 */ &#125;
const Wrapper = styled.aside`
  /* 基础样式 */
  
  $&#123;TextLink&#125; &#123;
    color: var(--color-text);
    font-weight: var(--font-weight-bold);
  &#125;
`;

export default Aside;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>styled-components 允许我们像这样将一个组件“嵌入”到另一个组件中。当组件被呈现时，它会产生相应的选择器，一个匹配 <code>TextLink</code> 组件的类名。</p>
<p>这个肯定更好，但我还不够满意。我们还没有解决最大的问题，我们只是让它更容易解决。</p>
<p>让我们回过头来谈谈封装。</p>
<p>我之所以喜欢 React，是因为它可以将逻辑（状态、副作用）和 UI （JSX） 封装到可重用盒子中。很多人关注的是“可重用性”，但在我看来，更酷的地方在于它是一个“盒子”。</p>
<p>React 组件在其周边设置了严格的边界。当你在一个组件中编写 JSX 时，你可以相信 HTML 只会在该组件中被修改；你不必担心应用其他地方的组件“侵入”并篡改 HTML。</p>
<p>再看一下 <code>TextLink</code> 解决方案。<code>Aside</code> 在侵入并干预 <code>TextLink</code> 的样式！如果任何组件可以覆盖任何其他组件的样式，那么我们实际上根本就没有封装。</p>
<p>想象一下，如果你完全自信地确认给定元素的所有样式都定义在 styled-component 本身中，那该有多好?</p>
<p>事实证明，我们可以这么做<sup>[2]</sup>。方法如下：</p>
<pre><code class="copyable">// Aside 组件使用
import Aside from '@components/Aside';
import TextLink from '@components/TextLink';

const Section = () => &#123;
    return (
        <Aside>
这是一个 Aside 组件的例子，包含一个
            <TextLink>an included link.</TextLink>
        </Aside>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// Aside.js
const Aside = (&#123; children &#125;) => &#123;
    return (
        <Wrapper>
          &#123;children&#125;
        </Wrapper>
    )
&#125;

// 导出这个 Wrapper
export const Wrapper = styled.aside`
  /* 样式 */
`;

export default Aside;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// TextLink.js
import &#123; Wrapper as AsideWrapper &#125; from '../Aside'

const TextLink = styled.a`
  color: var(--color-primary);
  font-weight: var(--font-weight-medium);

  $&#123;AsideWrapper&#125; & &#123;
    color: var(--color-text);
    font-weight: var(--font-weight-bold);
  &#125;
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你不熟悉 & 字符，它是最终生成的类名的占位符。当 styles-components 为该组件创建一个<code>.textlink-abc123</code> 类时，它也会用该选择器替换任何 & 字符。这是最终生成的 CSS：</p>
<pre><code class="copyable">.TextLink-abc123 &#123;
  color: var(--color-primary);
  font-weight: var(--font-weight-medium);
&#125;

.Aside-Wrapper-def789 .TextLink-abc123 &#123;
  color: var(--color-text);
  font-weight: var(--font-weight-bold);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这个小技巧，我们把控制反转了。我们说“这是我的基础 <code>TextLink</code> 样式，这是我在<code>AsideWrapper</code> 中包装的 <code>TextLink</code> 样式”，这两种样式的声明都在同一个地方。</p>
<p>强大的 <code>TextLink</code> 将再次掌控自己的命运。我们的样式有单一的来源。</p>
<p>这样做真的好得多，下次你遇到这种情况，不妨试一试。</p>
<h2 data-id="heading-2">为场景选择合适的工具</h2>
<p>当我们有像 <code>Aside</code> 和 <code>TextLink</code> 这样的两个通用组件时，这种形式的“控制反转”使事情变得如此美好和可控，但这适合所有的场景吗?</p>
<p>假设我们有一个组件，<code>HalloweenSale.js</code>。这是一个使用我们标准组件的营销页面，但添加了一个可怕的字体和橙色主题。</p>
<p>我们是否应该更新所有标准组件以支持此变体？当然不是。😅</p>
<p>首先，将 <code>HalloweenSale</code> 导入到 <code>TextLink</code> 中会增加我们的 JavaScript 包的体积：无论用户何时访问我们网站上的任何页面，他们都必须下载万圣节销售页面的所有标记和代码，即使是在 3 月中旬！</p>
<p>这么做还会使我们的 <code>TextLink.js</code> 文件变得杂乱，被一次性的变量塞满了，这些 99% 的时间都无关紧要的样式反而会挤掉了更相关的上下文样式。</p>
<p>还有一种替代方法 —— 组合 API：</p>
<pre><code class="copyable">// HalloweenPage.js
import TextLink from '../TextLink';

const HalloweenTextLink = styled(TextLink)`
  font-family: 'Spooky Font', cursive;
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两种情况之间的区别有点微妙，但却非常重要！</p>
<p>在万圣节的情景下，我会使用一个通用的标准组件，并将其组合成一个新组件——一个具有更专门用途的组件，以便以特定的方式使用。<code>HalloweenTextLink</code> 重用的方式与 <code>TextLink</code> 不一样。</p>
<p>我们能在 Aside/TextLink 的场景中做同样的事情，创建一个 <code>AsideTextLink</code> 包装器吗？当然可以，但我觉得不应该这么做：</p>
<ol>
<li>与 <code>HalloweenTextLink</code> 不同，我在各处使用 <code>Aside</code> 组件！当我使用 <code>TextLink</code> 时，了解这些样式是有益的，因为这是应用的核心部分。</li>
<li>我想要上下文样式被自动应用。我不希望开发人员在使用 <code>Aside</code> 时，还要记得必须使用 <code>AsideTextLink</code>：</li>
</ol>
<pre><code class="copyable"><Aside>
  你真觉得开发者会记得使用
  <AsideTextLink href="">
    这个组件变体吗
  </AsideTextLink>?
</Aside>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我非常了解我自己，最多有 75% 的时间我会记得这么做。剩下的 25% 的时候，可能会导致一个相当不一致的 UI！</p>
<p>现在，我们要权衡一下了：对于 <code>HalloweenTextLink</code> 这个组件，其实我们失去了一些可见性。理论上，我可能会在更改 <code>TextLink</code> 的时候悄悄地破坏了 <code>HalloweenTextLink</code>，甚至不知道该组件的存在！</p>
<p>这很难办，没什么完美的解决方案，但是通过明确区分“核心变体”和“一次性变体”，我们可以确保优先处理最重要的内容，并把它们管理好（在 <code>TextLink.js</code> 中定义 30 个一次性变体真的有帮助吗？）。</p>
<h2 data-id="heading-3">继承的 CSS 属性</h2>
<p>有时候还会有一些出乎意料的情况发生：组件边界永远不会是完全密封的，因为某些 CSS 属性是可继承的。</p>
<p>但在我看来，这不是什么大事。</p>
<p>首先，为了解释我到底在说什么，请考虑以下内容：</p>
<pre><code class="copyable">function App() &#123;
  return (
    <div style=&#123;&#123; color: 'red' &#125;&#125;>
      <Kid />
    </div>
  )
&#125;

function Kid() &#123;
  return <p>Hello world</p>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Kid</code> 组件没有设置样式，但它最终显示为红色的文本。这是因为颜色是一个继承的属性，所有后代元素将默认为红色文本。</p>
<p>技术上讲，这是一种泄漏，但它是一个相当无害的泄漏，原因如下：</p>
<ol>
<li>我设置的任何样式都会推翻继承的样式，继承的样式永远不会赢得优先级之战。我确信显式设置的所有样式都会生效。组件样式还是组件自己说了算！</li>
<li>只有少数 CSS 属性是可继承的，而且它们基本上都是排版相关的。而布局属性如 <code>padding</code> 或 <code>border</code> 不会被继承。一般来说，排版样式应该被继承；如果需要将当前的字体颜色重新应用到段落中的每个 <code><strong></code> 或 <code><em></code>， 将非常烦人。</li>
<li>在 devtools 中，生效的组件样式来源非常清晰，我们很就能搞清楚样式是在哪里设置的。</li>
</ol>
<p>全局样式也是如此，在我的大多数项目中，都引入了一个 CSS reset 和一些常规的标准样式（normalize）。它们都是作用于标签（例如 p，h1）上，以尽可能降低优先级。人生苦短，如果可以直接用 <code>p</code> 标签时，何苦要个入一个 <code>Paragraph</code> 组件呢？</p>
<h1 data-id="heading-4">单独谈谈 CSS</h1>
<p>好了，我还有一个好东西要分享。</p>
<p>设想一下，如果我们想让 <code>Aside</code> 组件周围有一些空间，这样它就不会被卡在同级段落和标题之间。</p>
<p>这里有一种方法：</p>
<pre><code class="copyable">// Aside.js
const Aside = (&#123; children &#125;) => &#123;
  return (
    <Wrapper>
      &#123;children&#125;
    </Wrapper>
  );
&#125;

const Wrapper = styled.aside`
  margin-top: 32px;
  margin-bottom: 48px;
`;

export default Aside;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这可以解决我们的问题，但我觉得太重了。如果采用这样的思路，我们容易陷入困局 —— 比如当我们需要在另一种有不同间距要求的情况下使用这个组件时，我们要怎么办？</p>
<p>以这种方式使用 margin 与设计可重用的通用组件的思想是对立的。</p>
<p>Heydon Pickering 对此有句名言：</p>
<blockquote>
<p>“margin 就像在你决定要把东西粘在什么上，或者是否应该粘在什么东西上之前，先给东西粘上胶水。”</p>
</blockquote>
<p>还有一个问题是 margin 很奇怪，它可能一种出人意料的、违反直觉的方式坍塌，这时可能会打破封装。例如，我们把 <code><Aside></code> 放到 <code><MainContent></code> 中，顶部的边距就会把整个组往下推，<em>就像</em> <code>MainContent</code><em>有边距一样</em>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ed8ab3a51a24755bdd092a04591effa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我最近写了一篇关于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.joshwcomeau.com%2Fcss%2Frules-of-margin-collapse%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.joshwcomeau.com/css/rules-of-margin-collapse/" ref="nofollow noopener noreferrer"> Margin 塌陷规则</a>的文章。如果你对 margin 的这种表现感到惊讶，这篇文章对你非常有用！</p>
<p>越来越多的开发者<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmxstbr.com%2Fthoughts%2Fmargin" target="_blank" rel="nofollow noopener noreferrer" title="https://mxstbr.com/thoughts/margin" ref="nofollow noopener noreferrer">选择不使用 margin</a>，我还没有完全放弃这个习惯，但我认为避免像这样的“margin 泄漏”是一个很好的折中和起点。</p>
<p>我们怎么不使用 margin 进行布局？有几个选择！</p>
<ul>
<li>如果它在一个 CSS 网格中，你可以使用 <code>grid-gap</code> 来分隔每个元素</li>
<li>如果它在一个 Flex 容器中，全新的 <code>gap</code> 属性会非常有效（尽管你可能希望等到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2Fflexbox-gap" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/flexbox-gap" ref="nofollow noopener noreferrer">Safari 添加支持</a>后再使用）</li>
<li>你可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.joshwcomeau.com%2Freact%2Fmodern-spacer-gif%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.joshwcomeau.com/react/modern-spacer-gif/" ref="nofollow noopener noreferrer">使用 </a><code>Spacer</code><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.joshwcomeau.com%2Freact%2Fmodern-spacer-gif%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.joshwcomeau.com/react/modern-spacer-gif/" ref="nofollow noopener noreferrer"> 组件</a>，这是一个有争议但意外好用的选择</li>
<li>你可以使用专用的布局组件，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fseek-oss.github.io%2Fbraid-design-system%2Fcomponents%2FStack%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://seek-oss.github.io/braid-design-system/components/Stack/" ref="nofollow noopener noreferrer">比如 Braid 设计系统中的 Stack</a></li>
</ul>
<p>最终的目标是避免把自己逼入绝境。我相信，只要我们是有意识地，并且理解这种权衡关系，偶尔用用 margin 解决实际问题也挺好的。</p>
<p>最后，我们再谈谈层叠上下文。</p>
<p>仔细看看下面的代码：</p>
<pre><code class="copyable">// Flourish.js
const Flourish = styled.div`
  position: relative;
  z-index: 2;
  /* 忽略了一些样式 */
`;

export default Flourish;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发现问题了吗？和之前一样，我们预先给组件设置了一个 <code>z-index</code> 属性，我们希望将来所有情况下 2 都是正确的层级！</p>
<p>这个问题还可能更严重，看看下面的代码：</p>
<pre><code class="copyable">// Flourish.js
const Flourish = (&#123; children &#125;) => &#123;
  return (
    <Wrapper>
      <DecorativeBit />
      <DecorativeBackground />
    </Wrapper>
  );
&#125;

const Wrapper = styled.div`
  position: relative;
`;

const DecorativeBit = styled.div`
  position: absolute;
  z-index: 3;
`;

const DecorativeBackground = styled.div`
  position: absolute;
  z-index: 1;
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顶层样式组件 <code>Wrapper</code> 没有设置 <code>z-index</code>……当然，这肯定是没问题的吧?</p>
<p>但愿如此。实际上，这会导致一个非常混乱的问题。</p>
<p>如果我们的 <code>Flourish</code> 组件有一个 z-index 值在中间的兄弟组件，那么这个组件会和 <code>Flourish</code> 的背景产生“交错”：</p>
<pre><code class="copyable"><div>
  <!-- Malcom 组件会被夹在中间! --> 
  <Malcolm
    style=&#123;&#123; position: 'relative', zIndex: 2&#125;&#125;
  />
  <Flourish />
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过使用 <code>isolation</code> 属性显式创建一个层叠上下文来解决这个问题：</p>
<pre><code class="copyable">const Flourish = (&#123; children &#125;) => &#123;
  return (
    <Wrapper>
      <DecorativeBit />
      <DecorativeBackground />
    </Wrapper>
  );
&#125;

const Wrapper = styled.div`
  position: relative;
  isolation: isolate;
`;

// 剩余部分没有变化
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这确保了任何兄弟元素将高于或低于这个元素。额外的好处是，新的层叠上下文没有 z-index，所以我们可以完全依赖于 DOM 顺序，也可以在必要时传递一个特定的值。</p>
<p>这个东西很复杂，超出了本文的范围。层叠上下文将在我即将到来的 CSS 课程中深入讨论，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-for-js.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-for-js.dev/" ref="nofollow noopener noreferrer">JavaScript 开发人员的 CSS 课</a>。</p>
<h1 data-id="heading-5">提示和技巧</h1>
<p>唷！我想要分享的高级“好东西”都讲完了，但是在结束之前，我还有几个自认为值得分享的小细节。我们来看看。</p>
<h2 data-id="heading-6">as 属性</h2>
<p>React 开发人员以不懂 HTML 的语义而闻名，他们使用 <code><div></code> 处理所有情况。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f6818697d2b412c9c7c1b72f4f6114b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对 styled-components 的一项公正批评是，它在 JSX 和生成的 HTML 标记之间添加了一层间接层。只有意识到这个事实，我才能讲明白下面的内容！</p>
<p>你创建的每个 styled-component 组件都接受一个属性，它会改变使用的是哪个 HTML 元素。这对于标题来说非常方便，因为具体的标题级别取决于场景：</p>
<pre><code class="copyable">// `level` 是一个取值为 1-6 的数字，可以映射为 h1-h6
function Heading(&#123; level, children &#125;) &#123;
  const tag = `h$&#123;level&#125;`;
  return (
    <Wrapper as=&#123;tag&#125;>
      &#123;children&#125;
    </Wrapper>
  );
&#125;

// 下面的 h2 并不重要，因为它总是被覆盖的
const Wrapper = styled.h2`
  /* 样式内容 */
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它也可以方便地根据环境把组件渲染为 <code>button</code> 或 <code>link</code>：</p>
<pre><code class="copyable">function LinkButton(&#123; href, children, ...delegated &#125;) &#123;
  const tag = typeof href === 'string'
    ? 'a'
    : 'button';

  return (
    <Wrapper as=&#123;tag&#125; href=&#123;href&#125; &#123;...delegated&#125;>
      &#123;children&#125;
    </Wrapper>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>HTML 语义化非常重要，所有使用 styled-components 的开发人员都应该了解 <code>as</code> 属性，这个至关重要的知识。</p>
<h2 data-id="heading-7">增加优先级</h2>
<p>在大多数 CSS 方法论中，你偶尔都会遇到这样的情况：由于另一种样式覆盖，你编写的声明没有效果。这被称为优先级问题，因为不想要的样式优先级更高。</p>
<p>在大多数情况下，如果你遵循本文列出的方法，我保证你不会遇到优先级问题，除了在处理第三方 CSS 时。这个博客有大约 1000 个样式组件，我从来没有遇到过优先级的问题。</p>
<p>我很犹豫要不要分享这个技巧，因为这是一个应该避免的情况的逃生口……但我也想现实一点。我们总是在并不理想的代码仓库中工作，并且在你的工具箱中额外增加一个工具永远不会有坏处。</p>
<p>像这样：</p>
<pre><code class="copyable">const Wrapper = styled.div`
  p &#123;
    color: blue;
  &#125;
`

const Paragraph = styled.p`
  color: red;
  && &#123;
    color: green;
  &#125;
`;

// 使用:
<Wrapper>
  <Paragraph>I'm green!</Paragraph>
</Wrapper>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，针对同一个段落，我们有三个独立的颜色声明。</p>
<p>在基本级别，我们的段落是使用标准样式组件语法给出的红色文本。不幸的是，<code>Wrapper</code> 使用了后代选择器，并使用蓝色文本覆盖了红色文本。</p>
<p>为了解决这个问题，我们可以使用双 & 符将其转换为绿色文本。正如我们前面看到的，& 字符是生成的类名的占位符。把它放两遍就会重复这个类：不是 <code>.paragraph</code>，而是 <code>.paragraph.paragraph</code>。</p>
<p>通过双倍强调这个类名，它的优先级增加了。 <code>.paragraph.paragraph</code> 比 <code>.wrapper p</code> 优先级更高。</p>
<p>这个技巧可以在不动用核武器 <code>!important</code> 的情况下提高优先级，这很重要。但这也是一个潘多拉魔盒：一旦你开始沿着这个技巧的道路走下去，你就走上了一条注定毁灭的道路。</p>
<h2 data-id="heading-8">babel 插件</h2>
<p>在生产环境中，styled-components 将为你创建的每个样式组件生成唯一的散列值，比如 <code>.hnn0ug</code> 或 <code>.gajjhs</code>。这些简洁的名称是有益的，因为它们不会在服务端渲染的 HTML 中占用太多空间，但对于开发人员来说，它们是完全不透明的。</p>
<p>幸运的是，存在一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstyled-components%2Fbabel-plugin-styled-components" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/styled-components/babel-plugin-styled-components" ref="nofollow noopener noreferrer">babel 插件</a>！在开发过程中，它使用语义类名，帮助我们追踪元素/样式的来源:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3330f7e645f446d189e182ff0d0bd5aa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你使用 <code>create-react-app</code>，你可以从这个插件中受益，而不需要通过改变所有的导入来使用：<code>import styled from 'styled-components/macro';</code></p>
<p>在你的项目中快速查找和替换将极大地改善你的开发体验！</p>
<p>对于其他类型的项目，你可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstyled-components%2Fbabel-plugin-styled-components" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/styled-components/babel-plugin-styled-components" ref="nofollow noopener noreferrer">遵循官方文档</a>。</p>
<h3 data-id="heading-9">后代选择器</h3>
<p>前文我们讨论了为何使用后代选择器使你的应用难以跟踪样式。但如果我们可以使用 babel 插件跟踪样式，可以消除这个顾虑吗?</p>
<p>很遗憾，并不能。完全不能。</p>
<p>再重复一次，以下是我希望你避免的一种模式：</p>
<pre><code class="copyable">// Aside.js
const Aside = (&#123; children &#125;) => &#123;
  return (
    <Wrapper>
      &#123;children&#125;
    </Wrapper>
  );
&#125;

const Wrapper = styled.aside`
  /* 基础样式 */
  a &#123;
    color: #F00;
  &#125;
`;

export default Aside;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们在 devtools 中查看它，我们会发现 babel 插件并不能真正处理这种愚蠢的事情：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32525f93c67647f8a955941857933a7e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>即使可以，我还是建议不要使用这种模式。我们不应该只有在代码实时渲染后才能够理解哪些样式生效了；而是最好只通过阅读源文件时就能做出这个判断，理想情况下只需查看一段代码。</p>
<p>这是否意味着每当我需要应用一个样式的时候，都要创建一个新的 <code>styled.whatever</code>？好吧，我可以降低一点要求，只要确保我使用后代选择器时，总是针对的是组件特有的元素：</p>
<pre><code class="copyable">// Whatever.js
const Whatever = () => &#123;
  return (
    <Wrapper>
      这是一个 <em>小例子</em>.
    </Wrapper>
  );
&#125;

const Wrapper = styled.div`
  & > em &#123;
    color: #F00;
  &#125;
`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要你不“侵入”修改另一个组件下的元素样式，这种模式还不算太糟。老实说，这仍然不理想，但我知道一直创建新的样式组件是很乏味的，这是一个合理的、务实的妥协。</p>
<h1 data-id="heading-10">思维模型</h1>
<p>在本文中，我们讨论了一些 styled-component 的特定 API，但是我希望传达的思想比任何特定的工具或库都要重要。</p>
<p>当我们将组件思维扩展到 CSS 时，我们获得了各种新的超能力：</p>
<ul>
<li>能够明确地知道是否可以安全地删除 CSS 声明（不会影响应用的其他模块！）</li>
<li>脱离优先级问题，不再试图寻找提高优先级的技巧</li>
<li>一套整洁明了的思维模型，它适合你的大脑，并帮助你准确地理解你的页面是什么样子，而不需要做一堆手动测试</li>
</ul>
<p>styled-components 本身没什么倾向性，所以有很多不同的使用方式……但是我必须承认，当我看到开发人员把它当作一个花哨的类名生成器或“Sass 2.0”时，我有点难过。如果你认同样式化组件就是组件的理念，那么你一定能从该工具中收获更多。</p>
<p>当然，这些只是我的观点，但我很高兴知道它们符合推荐的实践。我将这篇文章的初稿发给了 styled-components 的创造者 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftwitter.com%2Fmxstbr" target="_blank" rel="nofollow noopener noreferrer" title="https://twitter.com/mxstbr" ref="nofollow noopener noreferrer">Max Stoiber</a>，以下是他的回应：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec66b34f67ea409ba34344507a9ff755~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在我看来，许多类似的工具已经淡出视野。只有经过几年的实验，“如何在 React 中管理 CSS”的思路才变得清晰。我希望这篇文章能为你节省一些时间和精力。</p>
<br>
<blockquote>
<h3 data-id="heading-11">译者注</h3>
<p>[1]. 思维模型：原文是“Mental models”。大概可以理解为：解決问题时，人内在的思考和运作方式。 <br></p>
<p>[2]. 示例代码：该写法比较容易产生循环引用。在项目中运用时需要规范代码结构、引入循环依赖的检测机制。</p>
</blockquote></div>  
</div>
            