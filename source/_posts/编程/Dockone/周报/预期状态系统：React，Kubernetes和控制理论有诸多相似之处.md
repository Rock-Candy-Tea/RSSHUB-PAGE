
---
title: '预期状态系统：React，Kubernetes和控制理论有诸多相似之处'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/3b47ad5981de45f6d8c601daee810095.png'
author: Dockone
comments: false
date: 2022-02-04 07:07:05
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/3b47ad5981de45f6d8c601daee810095.png'
---

<div>   
<br>在2021年12月份，我在<a href="https://ndcoslo.com/agenda/desired-state-how-react-kubernetes-and-control-theory-have-lots-in-common-0ded/0llw0hsd6pk">NDC Oslo 2021会议</a>上演讲了《预期状态：React，Kubernetes和控制理论有诸多相似之处》，本文是这次演讲的文字版。<br>
<br>我想分享这些年学习了多个技术栈之后遇到的一种特定类型的抽象。这是一种在计算机的多个领域一次次出现的模型，从UI工程到基础架构管理，数据库，编程语言理论等等。<br>
<br>因为缺少更好的术语，我称这种抽象为<em>预期状态</em>，但是这个名称只能描述这种抽象的一部分。我会介绍看待这种抽象的多种方式，并且展示一些使用到它的示例。希望最终你不仅仅能够在各种工具和API里能认出这种抽象，而且能够评估在你自己的项目中是否值得使用它。<br>
<h3>总概</h3>我会从一些通用的目的开始，然后介绍简单的例子，展示如何看待即使在我们知识边界之外的系统中的这种抽象。这会让我们了解构成这个模型基础的一些通用原则。然后我会展示一些看待这个抽象的不同视角，用常用的工具，比如React，Kubernetes和Terraform来举例。最后会提到应用这种抽象时应该思考的一些事情。<br>
<h4>Mental模型</h4><a href="https://en.wikipedia.org/wiki/All_models_are_wrong">所有模型都是错误的，但其中有一些是有用的</a>。在软件领域，我们总是在和模型打交道，描述事情是如何工作的mental模型，它在不同的领域，行业里都挺有用的，并且试图发现它们概念上的联系并找到共同之处。有时你会发现看似不相关的东西却彼此相通。<br>
<br>你的模型永远不会是完美的，但这并不重要。当学习新事物时，可以更容易地映射到已有的mental模型。就像学习语言的时候——你懂了更多门语言，你就更容易学习新的（无论是人类的语言还是编程语言）。语法有所变化，但是底层的模型通常并不怎么变。这让大家能够更清楚地思考。<br>
<h4>抽象还是接口？</h4>我想要描述的预期状态系统在前端Web开发，后端开发，数据库，基础架构，GUI等领域常用的工具和库函数里都有其踪迹。这是一种抽象的模型，但是它和接口紧密相关，因为抽象根本性地改变了开发人员或者用户或其他系统和某个系统交互的方式。<br>
<br>抽象到底是什么？《<a href="https://mitpress.mit.edu/books/concepts-techniques-and-models-computer-programming">计算编程的理念，技术和模型</a>》一书的作者将其定义为解决某个特定问题的工具或者设备。<br>
<br>这个定义非常笼统和正确，但是我尤其喜欢<a href="https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions">Joel Spolsky的定义</a>，他认为抽象就是伪装。他说：“string库是什么？它是计算机假装自己可以像操作数字一样操作string的方式。什么是文件系统？它是假装硬盘其实不是一堆能够在特定位置存储比特的旋转磁盘，而是包含单个文件的文件夹嵌套文件夹的层级系统，这些单个文件则包含一个或者多个比特的string。”<br>
<br>抽象是我们工作的核心。我发现最有价值的工作不是编写程序，而是设计这些抽象层。计算机编程主要就是设计和使用抽象来实现新的目标。当可以构建出一些将底层复杂性隐藏掉的系统，并为使用此系统的人或其他系统提供更为简单的接口时，这是令人兴奋的。<br>
<br>这就是抽象，让我们看一个每天都会遇到的例子。<br>
<h3>电梯</h3>想象一个普通的电梯。<br>
<br>你来到电梯前，看到指上和指下的按钮。我不知道你是如何想的，但是在我小时候，我的大脑总会将上下的箭头解释为“我要让电梯上去”和“我要让电梯下去”，而不是“我要上去”和“我要下去”。也就是说，我想直接控制它。直到今天，有时我仍然需要花一点脑细胞才能记住电梯的实际规则。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/3b47ad5981de45f6d8c601daee810095.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/3b47ad5981de45f6d8c601daee810095.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对于来到电梯前的人来说，这些按钮意味着什么？它们就是电梯的<em>接口</em>。允许用户使用这个设备和系统交互。我们可以把用户看成另外一个系统，它遇到了一个通用定义的接口，这里允许两个系统发生交互。现在，我的困惑就是这个指向哪里的箭头可能意味着“我想要去那里”以及“我想要这个东西去那里”。当然并不是很多人都有这个困惑。让我们忽略解释用户界面的问题，并比较这两种方案，就当它们都是有效的。<br>
<br>我们可以称这两种方案为什么呢？<br>
<br>在我小时候的方案里，我想要告诉机器它需要做什么。也就是说，如何实现我想要它完成的事情。我想给他<em>指示</em>。懂拉丁文的人可能会建议我们称之为<em>命令式</em>方案。<br>
<br>在另一种方案里，我们只是告诉机器我们需要做什么，让它自己判断它需要如何去做。我们<em>声明</em>我们想要的。因此可以称之为<em>声明式</em>方案。<br>
<br>使用命令式方案，我们告诉机器怎么去做我们想要的——如何到达我的楼层。使用声明式方案，我们告诉它我们想要什么。<br>
<br>然后它运行一小段逻辑来决定实际如何移动电梯。这段逻辑需要考虑一些事情，比如：电梯在哪里，调用者在哪一层等等。如果电梯在我们上面，它需要下来。如果它在我们下面，它需要上去。<br>
<br>使用命令式接口，实际需要我们来负责判断这些。因此，我们需要获得电梯在哪里这些信息，可能可以通过屏幕展示出来。（显然这不是生活中的实际场景，这也很快地证伪了我小时候的理解）只有掌握了这些<em>状态</em>，我们才能够决定发给机器的具体指令。<br>
<br>在声明式方案里，我们不需要知道电梯状态。<br>
<h4>观察1：声明式接口是无状态的</h4>注意在这个例子里，使用声明式接口时，我们实际提供给电梯两类信息：我们想要上电梯（不管它现在在什么位置），以及我们想要上去或者下去。<br>
<br>简化下示例，分开两种概念并且仅关注于第一种——我们想要上电梯。在这个场景里我们仅仅需要一个按钮，对吧？这样简单的电梯是存在的。<br>
<br>我们将两个按钮简化成了一个。这意味着什么呢？<br>
<h4>观察2：声明式接口让控制减少</h4>与之对比，命令式方案给了你更多控制权——你可以让电梯上或者下，不管你站在哪里（还是两个按钮），虽然在实际日常生活的电梯里没啥意义，但是你确实可以这么做。声明式方案让你有更少的控制权——电梯总是来到我们的地方（一个按钮）。<br>
<br>但是，你很可能注意到这不是全部。<br>
<br>我小时候没有想到的是电梯可以<em>服务多层</em>。电梯接口不仅仅是你所在楼层的按钮，而是所有楼层都有按钮，还有电梯内部的按钮。<br>
<br>当你考虑到这所有的情况，就会发现命令式方案根本无法工作。怎么处理相同时间多人并发控制呢？如果你不是足够的快，在你看到屏幕上电梯当前位置的瞬间就按下按钮，电梯可能已经呼啸而过，而你则把它送到更远的地方，这该怎么办？如果不同楼层的两个人一直在做相反的输入，使电梯在原地振荡，又怎么办？<br>
<br>虽然声明式方案拿走了部分控制权，但是它解决了这些问题。比如，我们可以基于按下按钮的时间，简单地根据先来先服务的机制处理不同楼层的人。<br>
<h4>观察3：声明式接口简化了并发处理</h4>但这效率不高——如果多个楼层的人想要去同一个方向，我们需要在中途停止。好吧，如果用户事先告诉我们他们想去哪里呢？<br>
<br>那么我们可以优化电梯的运行，在电梯下行或上行的时候带上更多的人。可以称这样的信息为域特定参数。最后，这就是为什么需要两个按钮，为什么它们代表我们想去那里，而不是直接表示我们想要电梯去哪里。<br>
<br>在一些非常高的建筑里，甚至可以在上电梯之前就选择想要到达的楼层，这就让系统可以做进一步的优化。<br>
<h4>观察4：声明式接口有助于优化</h4>重点是抛开命令式控制，并且加入域特定参数，我们能够进一步优化操作。发送到引擎的指令可以排列，重新排序等等，这让我们能够让电梯并发支持多个楼层的多人操作。让我们能够构建更好的优化，并且彻底隐藏底层系统的机制。<br>
<h4>观察5：声明式接口提供了封装</h4>注意，电梯也在做同样的事情。上下，停在这层楼或那层楼。因此，电梯里得有什么东西能够直接对电梯发出命令式控制，否则我们想去哪里就不重要了，它不会移动。我喜欢这么认为，声明性接口封装了命令式接口。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/ccfd0e6cfaad520204226fedf45ac588.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/ccfd0e6cfaad520204226fedf45ac588.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这样的封装也就是抽象。这是一种到处可见的抽象。我们可以称这种抽象为预期状态。我们告诉系统预期状态——需要电梯到我们的楼层——让系统处理如何将电梯的实际状态改变为预期状态。为了实现这个目标，电梯必须能够查询底层系统的当前状态，将其和实际状态做对比，并且相应地发出命令，更新实际状态。为了区分这些概念，我使用动词“应用（apply）”来表示告诉系统预期状态的操作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/6c4c7cd1ba77d9cad48878df893c215e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/6c4c7cd1ba77d9cad48878df893c215e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
让我们概括一下这些原则。<br>
<h3>预期状态系统</h3>预期状态系统封装了命令式可变接口的底层 API 或系统，并允许其用户为此底层系统指定所需状态。然后，封装器负责找出底层系统的实际状态，将其与用户提供给它的预期状态进行比较，并应用必要的更改以使实际状态与预期状态保持一致。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/c97a817831c2527a6d3e63659e45b552.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/c97a817831c2527a6d3e63659e45b552.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
中间的部分，它循环式地观察底层系统，将其实际状态与预期状态进行比较，并相应地采取行动，这个过程称之为reconciliation。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/9ffb81a40fc9196b3a5e1142301a703c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/9ffb81a40fc9196b3a5e1142301a703c.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
正如示例中所提到的，我们可以用几种不同的方式来思考这种抽象。<br>
<h4>1. 声明式 vs. 命令式</h4>首先，作为封装在命令式接口上的声明式接口。只提供接口，让用户只需声明他们想要做什么，这会更简单。通过限制API并将用户引导到所需的使用模式中，这也是有益的。许多工具还利用了预期状态可以进行版本控制的特性，来提高可测试性和可审计性。<br>
<h4>2. 有状态 vs. 无状态</h4>也可以将其视为封装在有状态接口上的无状态接口。为什么要尽量减少跟踪状态的必要性？因为这样，系统才更易于理解，而且更容易测试。API变得更简单，就更易于维护，这也就意味着它更加可靠。能够推断变更对特定系统的影响非常重要，尤其是在处理并发性时。<br>
<h4>3. 不可变 vs. 可变</h4>另一种看待它的方式是，我们用可变语义的API封装了一个不可变语义的API。在某些情况下，这种抽象允许我们将底层系统视为无法更改的不可变对象。如果某些东西发生了变化，可以将其视为一个新对象。这再次有助于推理变更所造成的影响。<br>
<br>这些只是我们可以用来分析预期状态系统的众多可能角度中的三个，这对理解之后的示例是有用的。<br>
<br>让我们首先看一下React，它使用了预期状态系统的简化版本。<br>
<h3>React</h3>React是一种流行的构建用户界面的JavaScript库。它让用户定义想要的应用程序的外观和行为，都是用JavaScript实现的。<br>
<br>将应用定义为可组合组件的树型结构，这些组件是React的输入。树型结构定义了应用程序的结构，而外观由应用于这些树组件的各种属性控制，行为由各种回调函数控制，这些函数在用户输入或组件生命周期的某个阶段触发。树型结构的叶子表示要显示的实际HTML元素。<br>
<br>这棵树本质上是React的<code class="prettyprint">createElement</code>函数的一个巨大的嵌套调用。此函数的第一个参数是要使用的节点的类型，这可以是我们自己定义的组件，也可以是具有特定HTML元素的叶子节点。第二个参数是要发送到此组件的属性，第三个参数指定树中组件节点的子级。这个接口让组件非常容易组合，因为可以非常动态地传递数据，回调甚至其他组件（树中的父组件到子组件）。这使得React可以表达许多有用的设计模式。<br>
<br>为了节省手动输入并使语法更符合实际的HTML，许多人使用称为JSX的语法糖，这使得函数调用更加紧凑。<br>
<br>React 围绕浏览器文档对象模型或DOM进行包装，DOM是一种所有Web浏览器中都存在的重要的API。此API允许我们以编程的方式更改页面的内容。它将HTML页表示为具有属性、参数、事件处理程序的节点树，并提供用于查询、创建新元素、在树中追加新子级等的方法。React的组件树也有类似的结构。<br>
<h4>React作为预期状态系统</h4>让我们通过期望状态的镜头来看看React。当页面加载时，一些初始预期状态作为组件树的形式给到React。在内部，React在内存中保留此树的表示形式，每当预期状态发生变更时——基于用户输入或其他触发器——它都会将旧状态与新状态进行比较。这种内部表示形式过去被称为虚拟DOM，现在这个名称已经用的不多了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/f285459f8630a65397f782a8bee02ae7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/f285459f8630a65397f782a8bee02ae7.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
状态的比较生成了一系列需要在实际 DOM 上执行的操作。用于生成将一个树转换为另一个树所需的最小操作数的通用算法具有O(n^3)级的复杂性，其中n是树中的组件数。然而，React必须非常快速地做到这一点，因此它使用一系列启发式方法来计算所需的最少操作数。<br>
<br>这将时间复杂度降低到O(n)。这些启发式方法在很大程度上依赖于两个假设：首先，两个不同类型的元素将产生不同的树；其次，开发人员可以使用称为key的特殊属性来提示哪些子元素在渲染中可能无需更改。对于列表和其他顺序很重要的地方，这是必需的。React还依赖于传递给子级的属性是不可变的事实——它假设当对象的内容发生变化时，对该对象的引用也会发生变化。然后，React可以执行简单的引用比较，而无需执行深度比较，并在组件属性更改时重新渲染组件。这让UI保持可响应。<br>
<br>我之所以强调这一点，是因为状态的结构以及比较它的两个版本时如何改变它的难度，可能是构建理想的预期状态系统的关键部分之一。<br>
<br>React计算所需最少操作的原因是，DOM上的操作非常慢。但是，整个比较机制是实现的细节，如果它是高性能的，React可以选择每次都从头开始重建整个树。<br>
<br>现在我想说，根据我们正在使用的模型，React是一个简化的预期状态系统。让我离题介绍一下控制理论的基础知识。<br>
<h4>控制理论：闭环系统 vs 开环系统</h4>闭环系统是在一个循环中相互连接的系统。如果系统1向系统2发送信号，则系统2的输出在某种程度上又是系统1输入的一部分。这称为<em>反馈</em>。反馈的一个关键特征是为不确定性提供了鲁棒性。闭环系统通过将所需的输出条件与实际条件进行比较，自动实现并保持预期的输出条件。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/b12aec75998d0686ce529e601b449b5e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/b12aec75998d0686ce529e601b449b5e.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<a href="https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers">虽然反馈有很多优点，但它也带来了一系列缺点。如果设计不当，系统可能会表现不稳定。这可能是正反馈的形式，例如当麦克风的放大器在房间中调得太高时。此外，反馈本质上也耦合了系统的不同部分</a>。<br>
<br>另一方面，在开环系统中，这种互连被切断。<br>
<h4>React是开环系统</h4>虽然React是模型中的预期状态系统，但它实际上是一个开环系统。React不会不断重新检查浏览器DOM的当前状态，以确定它是否正确。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/32ffda9870a30543e888ece223d05ef9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/32ffda9870a30543e888ece223d05ef9.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
首先，这可能会非常慢。它其实也不需要这么做。与许多其他预期状态系统不同，React的运行假设是，<em>只有它能够操作目标域</em>。它通常假设没有其他库函数或人绕过它去修改页面。你可以使用浏览器中的开发工具自行测试。如果修改了由React控制的HTML元素，则库函数不会尝试覆盖你的修改，除非发生变更的元素的父元素被重新渲染并替换了整个子树。<br>
<br>React的一个好处是它是以模块化的方式构建的。与DOM通信的部分是一个名为ReactDOM的单独模块，可以替换为不同的渲染目标，React称之为主机（host）。例如，在移动应用程序框架React Native中使用了不同的主机。在编写React Native时，你仍然将应用的用户界面指定为组件树。然而，React不是与DOM对话，而是与移动操作系统的原生API交互。使用自定义的渲染目标来扩展 React 也相对容易。<br>
<br>React的API最近添加了Hooks。这是一种有趣的设计模式，允许开发人员以声明性的方式管理组件中的状态和副作用。建议大家阅读Dan Abramov的博客文章《<a href="https://overreacted.io/making-setinterval-declarative-with-react-hooks">使用 React Hooks 让setInterval 变成声明式</a>》，他在其中用声明式的hook包装了一个固有的命令式API，即浏览器的setInterval方法。<br>
<br>让我们进一步研究些别的。<br>
<h3>Terraform</h3>Terraform是一个开源的基础架构即代码的工具，其目标是提供一个工作流来配置所有的基础架构。它允许用户指定基础架构的各个部分，最常见的是云提供商中不同类型和实例的资源，以及它们的配置，用Terraform的原生语言HCL编写的文本文件。<br>
<br>使用这些配置文件，你可以执行所谓的terraform计划，通过该计划，可以在预配或更改实际基础结构之前检查配置的执行计划是否符合预期。<br>
<br>首次运行Terraform时，它会创建一个名为tfstate的文件，用于存储资源的当前状态。<br>
<br>每次想要对其进行更改时，它都会去获取实际资源的当前状态，并报告新计划将造成的变更。然后就可以检查变更是否正确并应用它们。<br>
<h4>Terraform作为预期状态系统</h4>在生成的差异中，你可以看到新计划将进行哪些更改，还可以查看实际状态是否已偏离保存的tfstate。换句话说，与React不同，Terraform是一个闭环系统。本质上，这是因为它正在优化以解决不同的问题——虽然React需要快速更新并且可以假设没有其他人接触其目标域，但Terraform则可以花费更多的时间（并且确实）弄清楚与实际状态的差异。至关重要的是，它不能假设它所管理的资源保持不变。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/e62c7e923a40e65df00ac1b42ca25da7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/e62c7e923a40e65df00ac1b42ca25da7.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
就像你可以用不同的主机扩展React一样，Terraform有一个称为提供者（provider）的插件集合。provider负责理解API与某种服务的交互，并基于该API将资源公开。当然，也可以创建自己的provider。与React不同，Terraform在如何定义资源及其配置上增加了复杂性。可以将配置指定为自己的资源，也可以仅将其指定为父资源的一部分。这里因provider而异，许多资源类型都同时支持这两者。Terraform最困难的部分之一是如何管理这种耦合。<br>
<br>与Chef或SaltStack等配置管理工具相比，Terraform遵循不可变部署的原则。更改计划时，将重新创建资源并应用正确的状态。这意味着操作本质上可能具有破坏性。在VM上进行配置的更改可能意味着销毁原来的VM并预配新的VM。哪些操作是破坏性的，哪些不是破坏性的，是由每个provider定义的。另一方面，使用可变部署的话，更有可能陷入实际状态偏离预期状态的情况。换句话说，对Terraform状态的更改是幂等的——如果持续重新创建10个VM的相同状态，则最终结果始终只有10个VM。这是预期状态系统的关键属性。<br>
<br>让我们从预配转向容器编排。<br>
<h3>Kubernetes</h3>你们可能都听说过Kubernetes。这是一个由Google创建的开源系统，用于自动化容器化应用程序的部署，扩展和管理。为了实现其目标，它很有争议地将预期状态系统作为其最高层的设计理念。<br>
<br>Kubernetes管理机器集群内的容器化的工作流，这些机器称为节点（node）。可以是物理机或虚拟机。最小的工作单元称为Pod，可以安排它们在节点上运行。最终，带有我们代码的特定容器将在这个Pod中运行。Pod以多种资源进行组织，最常见的是部署（deployment）。可以用另一种资源（称为服务，service）来定义网络。还有许多其他类型的资源，并且可以创建自定义资源。<br>
<br>Kubernetes本身作为一系列服务，运行在这些节点上，称为控制平面。控制平面负责为API提供服务，持续跟踪资源和其他所需的任务，来保持系统的运行。<br>
<br>集群可以用 命令行工具<em>kubectl</em>来控制，该工具是Kubernetes的接口。<br>
<br>虽然它还提供了一种类似命令式的API，但其用法的核心是用<code class="prettyprint">yaml</code>配置文件完成的，将其作为预期状态应用到集群里。<br>
<h4>Kubernetes作为预期状态系统</h4>我们也可以通过模型的镜头来看待Kubernetes。与Terraform类似，你向系统提供集群中特定资源的预期状态，这次是以yaml文件的形式。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/c24840ac1280df988a06ae49f22769c9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/c24840ac1280df988a06ae49f22769c9.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes中称为控制器（controller）的组件负责保证给定资源的实际状态与预期状态保持一致。与Terraform不同，这种情况是持续发生的。如果你尝试删除有3个预期副本的部署中的某个Pod副本，Kubernetes将立即启动一个新副本。同样，如果一个Pod不断崩溃，将继续尝试运行它，因为它试图保持实际状态与预期状态一致。Kubernetes是一个闭环系统。<br>
<br>控制理论中另一个有趣的概念，出现在持续的对预期状态reconciliation的系统中，即滞后（hysteresis）。<br>
<h4>控制理论：滞后（hysteresis）</h4>滞后表示这个系统的行为不仅取决于它在时间t处的输入，还取决于该输入的历史记录。您也可以将其视为向系统添加了人为滞后。一个广泛使用的例子是恒温器。假设我们将恒温器的温度设置为20度。没有滞后的话，一旦温度达到预期状态，加热就会关闭。但这意味着很快温度就会下降到20度以下，然后需要重新打开暖气。恒温器系统就会开始振荡，快速地打开和关闭加热。当我们添加滞后时，恒温器会等到温度高于22度，然后再关闭加热。同样，恒温器将等到温度低于18度时才重新打开加热。这确保了系统更平稳、更可靠的运行。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/e768a1cee8e84973cf37b8fd4895df16.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/e768a1cee8e84973cf37b8fd4895df16.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Kuberntes控制器</h4>在Kubernetes中，当它必须决定是否将一些工作负载从计算资源正在减少的Node中移走时，这个概念就会发挥作用，这就是所谓的Pod逐出。可以指定软宽限期，这意味着Kubernetes将等待一段时间，然后再将Pod从节点调度出去，因为资源约束可能是暂时的情况。这确保了调度的更可预测性和更顺畅的操作。<br>
<br>Kubernetes实际上是由许多控制器组成的，它们协同工作，以使实际状态接近预期状态。每个控制器可以对一种或多种资源类型执行操作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/59c0e020ad234700d5e5105270ae4e70.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/59c0e020ad234700d5e5105270ae4e70.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这些控制器实际通常是嵌套的——特定的控制循环（控制器）使用一种资源作为其预期状态，并且控制另一种资源，设法达到预期状态。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/db1773d6f7f7079facf236da356465f4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/db1773d6f7f7079facf236da356465f4.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
允许我再次转向控制理论的基础，这个概念来自电路板设计和CPU中断。<br>
<h4>控制理论：边沿- vs 电平触发逻辑</h4>当一个系统需要通过电路向另一个系统提供信息时，有两种选择。第一种称为边沿触发逻辑——系统1通过短暂的高压尖峰脉冲来传递电信号。这种方法的问题在于，如果系统2当时不在侦听，它可能就会错过信号。<br>
<br>第二种选择是我们所说的电平触发逻辑。在这种情况下，系统 1 将电压调高并保持在那里，直到确定它已被系统 2 接收。这种方法更可靠，因为系统2可以随时检查电线的状态。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220126/5c6bc391b4ed1246b761deabb8ba947c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220126/5c6bc391b4ed1246b761deabb8ba947c.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
你可能会看到这与事件驱动的通信与轮询更改之间的一些相似之处。<br>
<br>但是让我们回到Kubernetes控制器。React需要优化以便能够快速更新浏览器DOM，而Kubernetes需要优化reconciliation循环的观察部分。这是因为在任何时候，大量的控制器都可能需要询问特定资源的状态。大规模范围内持续轮询这些信息是低效的。因此，大多数控制器在边沿和电平触发逻辑之间选择了混合方法，称为列表-监视模式。<br>
<br>在此模式中，控制器首先请求当前状态，然后对其进行缓存，并保持事件流处于打开状态，以便立即更新到其缓存。与纯事件流不同，该系统是健壮的，可以应对崩溃和网络问题，因为控制器可以随时重新断言状态。<br>
<br>让我们再看一下另一种描述预期状态模型的方法。<br>
<h3>值 vs 引用语义</h3>我们可以将其视为用值语义封装了引用语义。当我们将对象视为值时，假设它们无法更改，它们是不可变的（在这种情况下，对象通常意味着使用的东西，一些数据）。在编程时，我们不必担心整数5和整数4之后加了1这两者之间的差异。五等于五。换句话说，是对象的内容提供了对象标识，而不是我们对它的引用。<br>
<br>预期状态只是我们想要其存在于世界上的各种值的集合。与其像React一样跟踪浏览器DOM节点的引用，或者Kubernetes中的容器，或者Terraform中的虚拟机，我们可以简单地将它们视为值。值不能改变，如果我们需要另一个值，必须创建一个新的。底层系统负责处理下面的所有可变逻辑。在某种程度上，你最喜欢的编程语言中的不可变字符串可以视为一个预期状态系统，编译器或解释器确保以高性能的方式协调值语义与底层内存的引用。对复杂对象执行此操作并不容易，而且通常也不可能。<br>
<br>不过，我发现思考一下如何将网络套接字，数据库或其他固有的有状态对象视为值，是非常有趣的。<br>
<h3>思考</h3>最后，让我们列出在设计这样的系统时必须记住的一些注意事项。<br>
<h4>1. 增加这样的复杂度是否值得？</h4>首先，你必须问自己一个问题，即它是否必要。它是否解决了真正的问题。添加抽象总是会导致更多的复杂性，重要的是要对这额外的复杂性是否值得进行成本效益分析。对于使用它的人来说，封装了命令式API后的声明式API似乎要简单得多，但其实它的内部复杂性总是更高的。<br>
<h4>2. 限制API</h4>思考怎么限制用户使用我们的接口，让他们可以做什么和不能做什么，这是很有用的。确定要给用户更少的控制权吗？是否确切地知道我们想要如何引导API？<br>
<h4>3. 闭环还是开环系统</h4>我们需要的是闭环还是开环系统？也就是说，我们是使用沙盒的唯一用户嘛？是否确定我们是唯一可以控制底层API的人，没有别人需要这些？<br>
<h4>4. 并发</h4>我们是否需要解决来自多个用户的对接口的并发更新？来自同一用户的多个更新怎么处理？如何协调多个相互冲突的预期状态？<br>
<h4>5. 优化</h4>无状态的接口以及限制API的使用面是否能够有助于系统的优化？<br>
<h4>6. 时间</h4>如何处理需要一定时间才能完成的事情。虽然API可能会将某些对象或资源视为值，但在系统内部，可能需要等待才能顺序地创建，销毁，更新它们。如何将这些传达给用户，又是否需要传达呢？<br>
<br>必须考虑时间是有状态和无状态系统之间的关键区别。当尝试将优雅的数学模型映射到现实世界时，时间是系统复杂性的主要来源之一。<br>
<h4>7. 比较差异的性能</h4>你的状态的结构是什么，如何能够迅速地比较它们。这可能是，也可能不是瓶颈，取决于结构和底层API的情况。<br>
<h4>8. 观察并且更新的性能</h4>底层API有多快，是否是观察或者更新的一部分。通常来说，预期状态系统比直接操作底层API更慢。您将始终需要权衡性能影响与使用此类抽象的好处。<br>
<h4>9. 持续跟踪资源</h4>如何跟踪底层API控制的资源。这在像Kubernetes这样的分布式系统中尤其重要，因为同时运行着许多控制循环。<br>
<h4>10. Escape hatches</h4>我们是否需要在接口里添加escape hatches，以便用户可以在需要时切入到命令式接口？这可能是出于性能的考虑，也可能是为了在真正需要时为用户提供更大的灵活性。React允许在需要时直接与浏览器DOM对话。尽管不鼓励这样做，但偶尔也是有必要的。同样地，Kubernetes允许用户在必要时可以直接进入Pod中运行的应用程序的shell命令行。<br>
<h3>结论</h3>本文介绍了什么是预期状态系统及其中心原则，向大家展示了一些使用到它的例子，并提出了在使用这种抽象时，应该记住的一些重要的考虑因素。<br>
<br>我在这里提出的想法并不是什么新鲜事，大多数人可能已经思考过这个问题。我希望通过结构化的方式思考它们，希望现在你的脑海中有一个更清晰的画面或mental模型，从而有助于工作。<br>
<br>在当今时代，我们周围的世界不是数学的，而是天生可变和有状态的。限制我们的事实是，在所有程序的底层都有一台冯·诺伊曼计算机，它有中央处理单元，数据存储和可以在CPU和存储之间传输单词的连接通道。它是固有的可变的和命令式接口。<br>
<br>但是，由于抽象，有时在有限的范围内，我们可以假装情况并非如此，并简化我们的接口。<br>
<br><strong>原文链接：<a href="https://branislavjenco.github.io/desired-state-systems/">Desired state systems</a>（翻译：崔婧雯）</strong> <br>
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝<br>
译者介绍<br>
崔婧雯，现就职于IBM，高级软件工程师，负责IBM WebSphere业务流程管理软件的系统测试工作。曾就职于VMware从事桌面虚拟化产品的质量保证工作。对虚拟化，中间件技术，业务流程管理有浓厚的兴趣。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            