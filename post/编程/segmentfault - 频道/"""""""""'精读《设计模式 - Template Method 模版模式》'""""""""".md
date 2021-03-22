
---
title: """""""""'精读《设计模式 - Template Method 模版模式》'"""""""""
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-22 04:44:36
thumbnail: 'https://segmentfault.com/img/remote/1460000039683667'
---

<div>   
<h1>Template Method（模版模式）</h1><p>Template Method（模版模式）属于行为型模式。</p><p><strong>意图：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。TemplateMethod 使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。</strong></p><h2>举例子</h2><p>如果看不懂上面的意图介绍，没有关系，设计模式需要在日常工作里用起来，结合例子可以加深你的理解，下面我准备了三个例子，让你体会什么场景下会用到这种设计模式。</p><h3>模版文件</h3><p>我们办事打印的文件就是模版文件，只需要写上个人基本信息再签字就可以了，我们不需要做太多的重复劳动，因为某些场景下大部分内容是可以固化下来的。比如买卖房屋，那大部分甲方乙方的条款是固定的，最大的变化是甲方与乙方的不同，我们在模版上签字时，就是利用了模版模式减少了大量写条款的时间。</p><h3>实例化</h3><p>实例化也可以认为是模版模式的某种表现形式，因为对于工厂方法，我们传入不同的初始值可能给出不同结果，那么实际上就是用很少的代码撬动了很大一块功能，起到了抽象作用。</p><h3>Vue 模版</h3><p>Vue 模版更符合我们对模版直觉的理解。这个场景中，模版指的是 HTML 模版，我们只需要在模版中以 <code>&#123;&#125;</code> 形式描述一些变量，就可以生成一块只有局部变量变化的模版 DOM，非常方便。</p><h2>意图解释</h2><p><strong>意图：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。TemplateMethod 使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。</strong></p><p>这个设计模式初衷是用于面向对象的，所以考虑的是如何在类中运用模版模式。首先定义一个父类，实现了一些算法，再将需要被子类重载的方法提出来，子类重载这些部分方法后，即可利用父类实现好的算法做一些功能。</p><p>比如说父类方法 <code>function a() &#123; b() + c() &#125;</code>，此时子类只需要重定义 b 与 c 方法，即可复用 a 的算法（b 与 c 相加）。当然这个例子比较简单，当算法较为复杂时，模版模式的好处将凸显出来。</p><h2>结构图</h2><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039683667" alt title referrerpolicy="no-referrer"></span></p><ul><li>ConcreteClass: 具体的父类。可以看到父类中实现了 TemplateMethod，其调用了 primitiveOperation1 与 primitiveOperation2, 所以子类只需要重载这两个方法，即可享用 TemplateMethod 提供的算法。</li></ul><p>假设 TemplateMethod 是 <code>OpenDocument</code> 打开文档的作用，那么 primitiveOperation1 可能是 <code>CanOpen</code> 校验，<code>primitiveOperation2</code> 可能是 <code>ReadDocument</code> 读取文档方法。</p><p>我们只要专心实现具体的细节方法，而不需要关心他们之间是如何相互作用的，父级会帮我们实现它。之后我们就可以调用子类的 <code>OpenDocument</code> 实现打开文档了。</p><h2>代码例子</h2><p>下面例子使用 typescript 编写。</p><pre><code class="typescript">class View &#123;
  doDisplay()&#123;&#125;

  display() &#123;
    this.setFocus()
    this.doDisplay()
    this.resetFocus()
  &#125;
&#125;

class MyView extends View &#123;
  doDisplay()&#123;
    console.log('myDisplay')
  &#125;
&#125;

const myView = new MyView()
myView.display()</code></pre><p>这个例子中，<code>doDisplay</code> 表示父类希望子类重载的方法，一般以 <code>do</code> 约定打头。</p><h2>弊端</h2><p>模版模式用在类中，本质上是固定不可变的结构，进一步缩小重写方法的范围，重写的范围越小，代码可复用度就越高，所以一定要在具有通用算法可提取的情况下使用，而不要为了节省代码行数而过度使用。</p><p>另外前端开发中，HTML 本身就很契合模版模式，因为 HTML 中有大量标签描述千变万化的 UI 结构，可复用的地方实在太多太多，所以非常适合模版模式，所以不要认为模版模式仅能在类中使用，模版模式还能在脚手架使用呢，比如填入一些表单自动生成代码。</p><p>学习这个设计模式时，注意不要固化思维在其定义的类这个框子中，因为设计模式写于 1994 年，其中提到的模式已经被大量迁移运用，能否识别并做适当的知识迁移，是 20 多年后的今天学习设计模式的关键。</p><h2>总结</h2><p>模版模式与策略模式有一定相似处，模版模式是改变算法的一部分，而策略模式是将策略完全提取出来，所以可以改变算法的全部。</p><blockquote>讨论地址是：<a href="https://github.com/dt-fe/weekly/issues/3045" rel="nofollow">精读《设计模式 - Template Method 模版模式》· Issue #305 · dt-fe/weekly</a></blockquote><p><strong>如果你想参与讨论，请 <a href="https://github.com/dt-fe/weekly" rel="nofollow">点击这里</a>，每周都有新的主题，周末或周一发布。前端精读 - 帮你筛选靠谱的内容。</strong></p><blockquote>关注 <strong>前端精读微信公众号</strong></blockquote><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000018549678" alt title referrerpolicy="no-referrer"></span></p><blockquote>版权声明：自由转载-非商用-非衍生-保持署名（<a href="https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh" rel="nofollow">创意共享 3.0 许可证</a>）</blockquote>  
</div>
            