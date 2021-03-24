
---
title: '写TypeScript代码的10种坏习惯'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/bVbJA9m'
author: segmentfault
comments: false
date: 2021-03-24 03:23:37
thumbnail: 'https://segmentfault.com/img/bVbJA9m'
---

<div>   
<blockquote>作者：Daniel Bartholomae<p>翻译：疯狂的技术宅</p><p>原文：<a href="https://startup-cto.net/10-bad-typescript-habits-to-break-this-year/" rel="nofollow">https://startup-cto.net/10-ba...</a></p></blockquote><p>近几年 TypeScript 和 JavaScript 一直在稳步发展。我们在过去写代码时养成了一些习惯，而有些习惯却没有什么意义。以下是我们都应该改正的 10 个坏习惯。</p><h2>1.不使用 <code>strict</code> 模式</h2><h4>这种习惯看起来是什么样的</h4><p>没有用严格模式编写 <code>tsconfig.json</code>。</p><pre><code class="json">&#123;
  "compilerOptions": &#123;
    "target": "ES2015",
    "module": "commonjs"
  &#125;
&#125;</code></pre><h4>应该怎样</h4><p>只需启用 <code>strict</code> 模式即可：</p><pre><code class="json">&#123;
  "compilerOptions": &#123;
    "target": "ES2015",
    "module": "commonjs",
    "strict": true
  &#125;
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>在现有代码库中引入更严格的规则需要花费时间。</p><h3>为什么不该这样做</h3><p>更严格的规则使将来维护代码时更加容易，使你节省大量的时间。</p><h2>2. 用 <code>||</code> 定义默认值</h2><h4>这种习惯看起来是什么样的</h4><p>使用旧的  <code>||</code>  处理后备的默认值：</p><pre><code class="ts">function createBlogPost (text: string, author: string, date?: Date) &#123;
  return &#123;
    text: text,
    author: author,
    date: date || new Date()
  &#125;
&#125;</code></pre><h4>应该怎样</h4><p>使用新的 <code>??</code> 运算符，或者在参数重定义默认值。</p><pre><code class="ts">function createBlogPost (text: string, author: string, date: Date = new Date())
  return &#123;
    text: text,
    author: author,
    date: date
  &#125;
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p><code>??</code> 运算符是去年才引入的，当在长函数中使用值时，可能很难将其设置为参数默认值。</p><h4>为什么不该这样做</h4><p><code>??</code> 与 <code>||</code> 不同，<code>??</code> 仅针对 <code>null</code> 或 <code>undefined</code>，并不适用于所有虚值。</p><h2>3. 随意使用 <code>any</code> 类型</h2><h4>这种习惯看起来是什么样的</h4><p>当你不确定结构时，可以用 <code>any</code> 类型。</p><pre><code class="ts">async function loadProducts(): Promise<Product[]> &#123;
  const response = await fetch('https://api.mysite.com/products')
  const products: any = await response.json()
  return products
&#125;</code></pre><h4>应该怎样</h4><p>把你代码中任何一个使用 <code>any</code> 的地方都改为 <code>unknown</code></p><pre><code class="ts">async function loadProducts(): Promise<Product[]> &#123;
  const response = await fetch('https://api.mysite.com/products')
  const products: unknown = await response.json()
  return products as Product[]
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p><code>any</code> 是很方便的，因为它基本上禁用了所有的类型检查。通常，甚至在官方提供的类型中都使用了 <code>any</code>。例如，TypeScript 团队将上面例子中的 <code>response.json()</code> 的类型设置为 <code>Promise <any></code>。</p><h4>为什么不该这样做</h4><p>它基本上禁用所有类型检查。任何通过 <code>any</code> 进来的东西将完全放弃所有类型检查。这将会使错误很难被捕获到。</p><h2>4. <code>val as SomeType</code></h2><h4>这种习惯看起来是什么样的</h4><p>强行告诉编译器无法推断的类型。</p><pre><code class="ts">async function loadProducts(): Promise<Product[]> &#123;
  const response = await fetch('https://api.mysite.com/products')
  const products: unknown = await response.json()
  return products as Product[]
&#125;</code></pre><h3>应该怎样</h3><p>这正是 <code>Type Guard</code> 的用武之地。</p><pre><code class="ts">function isArrayOfProducts (obj: unknown): obj is Product[] &#123;
  return Array.isArray(obj) && obj.every(isProduct)
&#125;

function isProduct (obj: unknown): obj is Product &#123;
  return obj != null
    && typeof (obj as Product).id === 'string'
&#125;

async function loadProducts(): Promise<Product[]> &#123;
  const response = await fetch('https://api.mysite.com/products')
  const products: unknown = await response.json()
  if (!isArrayOfProducts(products)) &#123;
    throw new TypeError('Received malformed products API response')
  &#125;
  return products
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>从 JavaScript 转到 TypeScript 时，现有的代码库通常会对 TypeScript 编译器无法自动推断出的类型进行假设。在这时，通过 <code>as SomeOtherType</code> 可以加快转换速度，而不必修改 <code>tsconfig</code> 中的设置。</p><h4>为什么不该这样做</h4><p><code>Type Guard</code> 会确保所有检查都是明确的。</p><h2>5. 测试中的 <code>as any</code></h2><h4>这种习惯看起来是什么样的</h4><p>编写测试时创建不完整的用例。</p><pre><code class="ts">interface User &#123;
  id: string
  firstName: string
  lastName: string
  email: string
&#125;

test('createEmailText returns text that greats the user by first name', () => &#123;
  const user: User = &#123;
    firstName: 'John'
  &#125; as any
  
  expect(createEmailText(user)).toContain(user.firstName)
&#125;</code></pre><h4>应该怎样</h4><p>如果你需要模拟测试数据，请将模拟逻辑移到要模拟的对象旁边，并使其可重用。</p><pre><code class="ts">interface User &#123;
  id: string
  firstName: string
  lastName: string
  email: string
&#125;

class MockUser implements User &#123;
  id = 'id'
  firstName = 'John'
  lastName = 'Doe'
  email = 'john@doe.com'
&#125;

test('createEmailText returns text that greats the user by first name', () => &#123;
  const user = new MockUser()

  expect(createEmailText(user)).toContain(user.firstName)
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>在给尚不具备广泛测试覆盖条件的代码编写测试时，通常会存在复杂的大数据结构，但要测试的特定功能仅需要其中的一部分。短期内不必关心其他属性。</p><h4>为什么不该这样做</h4><p>在某些情况下，被测代码依赖于我们之前认为不重要的属性，然后需要更新针对该功能的所有测试。</p><h2>6. 可选属性</h2><h4>这种习惯看起来是什么样的</h4><p>将属性标记为可选属性，即便这些属性有时不存在。</p><pre><code class="ts">interface Product &#123;
  id: string
  type: 'digital' | 'physical'
  weightInKg?: number
  sizeInMb?: number
&#125;</code></pre><h4>应该怎样</h4><p>明确哪些组合存在，哪些不存在。</p><pre><code class="ts">interface Product &#123;
  id: string
  type: 'digital' | 'physical'
&#125;

interface DigitalProduct extends Product &#123;
  type: 'digital'
  sizeInMb: number
&#125;

interface PhysicalProduct extends Product &#123;
  type: 'physical'
  weightInKg: number
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>将属性标记为可选而不是拆分类型更容易，并且产生的代码更少。它还需要对正在构建的产品有更深入的了解，并且如果对产品的设计有所修改，可能会限制代码的使用。</p><h4>为什么不该这样做</h4><p>类型系统的最大好处是可以用编译时检查代替运行时检查。通过更显式的类型，能够对可能不被注意的错误进行编译时检查，例如确保每个 <code>DigitalProduct</code> 都有一个 <code>sizeInMb</code>。</p><h2>7. 用一个字母通行天下</h2><h4>这种习惯看起来是什么样的</h4><p>用一个字母命名泛型</p><pre><code class="ts">function head<T> (arr: T[]): T | undefined &#123;
  return arr[0]
&#125;</code></pre><h4>应该怎样</h4><p>提供完整的描述性类型名称。</p><pre><code class="ts">function head<Element> (arr: Element[]): Element | undefined &#123;
  return arr[0]
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>这种写法最早来源于C++的范型库，即使是 TS 的官方文档也在用一个字母的名称。它也可以更快地输入，只需要简单的敲下一个字母 <code>T</code> 就可以代替写全名。</p><h4>为什么不该这样做</h4><p>通用类型变量也是变量，就像其他变量一样。当 IDE 开始向我们展示变量的类型细节时，我们已经慢慢放弃了用它们的名称描述来变量类型的想法。例如我们现在写代码用 <code>const name ='Daniel'</code>，而不是 <code>const strName ='Daniel'</code>。同样，一个字母的变量名通常会令人费解，因为不看声明就很难理解它们的含义。</p><h2>8. 对非布尔类型的值进行布尔检查</h2><h4>这种习惯看起来是什么样的</h4><p>通过直接将值传给 <code>if</code> 语句来检查是否定义了值。</p><pre><code class="ts">function createNewMessagesResponse (countOfNewMessages?: number) &#123;
  if (countOfNewMessages) &#123;
    return `You have $&#123;countOfNewMessages&#125; new messages`
  &#125;
  return 'Error: Could not retrieve number of new messages'
&#125;</code></pre><h4>应该怎样</h4><p>明确检查我们所关心的状况。</p><pre><code class="ts">function createNewMessagesResponse (countOfNewMessages?: number) &#123;
  if (countOfNewMessages !== undefined) &#123;
    return `You have $&#123;countOfNewMessages&#125; new messages`
  &#125;
  return 'Error: Could not retrieve number of new messages'
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>编写简短的检测代码看起来更加简洁，使我们能够避免思考实际想要检测的内容。</p><h4>为什么不该这样做</h4><p>也许我们应该考虑一下实际要检查的内容。例如上面的例子以不同的方式处理 <code>countOfNewMessages</code> 为 <code>0</code> 的情况。</p><h2>9. ”棒棒“运算符</h2><h4>这种习惯看起来是什么样的</h4><p>将非布尔值转换为布尔值。</p><pre><code class="ts">function createNewMessagesResponse (countOfNewMessages?: number) &#123;
  if (!!countOfNewMessages) &#123;
    return `You have $&#123;countOfNewMessages&#125; new messages`
  &#125;
  return 'Error: Could not retrieve number of new messages'
&#125;</code></pre><h4>应该怎样</h4><p>明确检查我们所关心的状况。</p><pre><code class="ts">function createNewMessagesResponse (countOfNewMessages?: number) &#123;
  if (countOfNewMessages !== undefined) &#123;
    return `You have $&#123;countOfNewMessages&#125; new messages`
  &#125;
  return 'Error: Could not retrieve number of new messages'
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>对某些人而言，理解 <code>!!</code> 就像是进入  JavaScript 世界的入门仪式。它看起来简短而简洁，如果你对它已经非常习惯了，就会知道它的含义。这是将任意值转换为布尔值的便捷方式。尤其是在如果虚值之间没有明确的语义界限时，例如 <code>null</code>、<code>undefined</code> 和 <code>''</code>。</p><h4>为什么不该这样做</h4><p>与很多编码时的便捷方式一样，使用 <code>!!</code> 实际上是混淆了代码的真实含义。这使得新开发人员很难理解代码，无论是对一般开发人员来说还是对 JavaScript 来说都是新手。也很容易引入细微的错误。在对“非布尔类型的值”进行布尔检查时 <code>countOfNewMessages</code> 为 <code>0</code> 的问题在使用 <code>!!</code> 时仍然会存在。</p><h2>10. <code>!= null</code></h2><h4>这种习惯看起来是什么样的</h4><p>棒棒运算符的小弟 <code>! = null</code>使我们能同时检查 <code>null</code> 和 <code>undefined</code>。</p><pre><code class="ts">function createNewMessagesResponse (countOfNewMessages?: number) &#123;
  if (countOfNewMessages != null) &#123;
    return `You have $&#123;countOfNewMessages&#125; new messages`
  &#125;
  return 'Error: Could not retrieve number of new messages'
&#125;</code></pre><h4>应该怎样</h4><p>明确检查我们所关心的状况。</p><pre><code class="ts">function createNewMessagesResponse (countOfNewMessages?: number) &#123;
  if (countOfNewMessages !== undefined) &#123;
    return `You have $&#123;countOfNewMessages&#125; new messages`
  &#125;
  return 'Error: Could not retrieve number of new messages'
&#125;</code></pre><h4>为什么会有这种坏习惯</h4><p>如果你的代码在 <code>null</code> 和 <code>undefined</code> 之间没有明显的区别，那么 <code>!= null</code> 有助于简化对这两种可能性的检查。</p><h4>为什么不该这样做</h4><p>尽管 <code>null</code> 在 JavaScript早期很麻烦，但 TypeScript 处于 <code>strict</code> 模式时，它却可以成为这种语言中宝贵的工具。一种常见模式是将 <code>null</code> 值定义为不存在的事物，将 <code>undefined</code> 定义为未知的事物，例如 <code>user.firstName === null</code> 可能意味着用户实际上没有名字，而 <code>user.firstName === undefined</code> 只是意味着我们尚未询问该用户（而 <code>user.firstName ===</code> 的意思是字面意思是 <code>''</code> 。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVbJA9m" alt="173382ede7319973.gif" title="173382ede7319973.gif" referrerpolicy="no-referrer"></span></p><hr><h4>本文首发微信公众号：前端先锋</h4><h4>欢迎扫描二维码关注公众号，每天都给你推送新鲜的前端技术文章</h4><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVRyYe" alt="欢迎扫描二维码关注公众号，每天都给你推送新鲜的前端技术文章" title="欢迎扫描二维码关注公众号，每天都给你推送新鲜的前端技术文章" referrerpolicy="no-referrer"></span></p><hr><h3>欢迎继续阅读本专栏其它高赞文章：</h3><ul><li><a href="https://segmentfault.com/a/1190000019115050">深入理解Shadow DOM v1</a></li><li><a href="https://segmentfault.com/a/1190000019135847">一步步教你用 WebVR 实现虚拟现实游戏</a></li><li><a href="https://segmentfault.com/a/1190000019154021">13个帮你提高开发效率的现代CSS框架</a></li><li><a href="https://segmentfault.com/a/1190000019085935">快速上手BootstrapVue</a></li><li><a href="https://segmentfault.com/a/1190000019205065">JavaScript引擎是如何工作的？从调用栈到Promise你需要知道的一切</a></li><li><a href="https://segmentfault.com/a/1190000019216390">WebSocket实战：在 Node 和 React 之间进行实时通信</a></li><li><a href="https://segmentfault.com/a/1190000019315509">关于 Git 的 20 个面试题</a></li><li><a href="https://segmentfault.com/a/1190000019302858">深入解析 Node.js 的 console.log</a></li><li><a href="https://segmentfault.com/a/1190000019283751">Node.js 究竟是什么？</a></li><li><a href="https://segmentfault.com/a/1190000019268920">30分钟用Node.js构建一个API服务器</a></li><li><a href="https://segmentfault.com/a/1190000018903274">Javascript的对象拷贝</a></li><li><a href="https://segmentfault.com/a/1190000018224157">程序员30岁前月薪达不到30K，该何去何从</a></li><li><a href="https://segmentfault.com/a/1190000018646425">14个最好的 JavaScript 数据可视化库</a></li><li><a href="https://segmentfault.com/a/1190000018439250">8 个给前端的顶级 VS Code 扩展插件</a></li><li><a href="https://segmentfault.com/a/1190000018660861">Node.js 多线程完全指南</a></li><li><a href="https://segmentfault.com/a/1190000018701596">把HTML转成PDF的4个方案及实现</a></li></ul><hr><ul><li><a href="http://blog.yidengxuetang.com/" rel="nofollow">更多文章...</a></li></ul>  
</div>
            