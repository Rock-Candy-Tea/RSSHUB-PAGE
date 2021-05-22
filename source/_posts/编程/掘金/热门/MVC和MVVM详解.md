
---
title: 'MVC和MVVM详解'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47695929a9764f9ab366846f8fd886ab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 19:30:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47695929a9764f9ab366846f8fd886ab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>请预留足够的时间，您将看到大量的文字描述。但是相信我，您绝对值得花时间在这些文字描述上面。我已经尽了我最大所能来阐述关于MVC和MVVM如此这般设计的原因以及我们应该如何思考一些相关的问题</p>
<h1 data-id="heading-1">让我们从MVC开始</h1>
<p>说起MVC，必须拿斯坦福大学公开课上的这幅图来说明，这可以说是最经典和最规范的MVC标准</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47695929a9764f9ab366846f8fd886ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
所以看懂这张图，你就应该明白MVC在iOS中的实现思路了。</p>
<h2 data-id="heading-2">你一直在使用MVC的思想只是你可能没有察觉到</h2>
<p>在我们着手探究MVC之前，有些东西是你应该了解的，虽然你可能已经了解了，但是这里还是要拿出来说一下，因为这些内容对于你理解MVC是如何运作的有很大的帮助。
几乎所有的App都只干这么一件事：将数据展示给用户看，并处理用户对界面的操作。
写过iOS App开发的开发者都知道我们大量的操作都是在controller中写布局代码再把数据显示到视图上面，然后实现一些专门处理用户操作的逻辑（比如按钮点击事件的实现）。
这里实际上你已经无形之中使用了MVC的思想了：一句话描述就是Controller负责将Model的数据用View显示出来，换句话说就是在Controller里面把Model的数据赋值给View，比如在controller中写self.label.text = self.data[@”title”]，只是还没有刻意建一个Model类出来而已。</p>
<h2 data-id="heading-3">MVC是如何进行工作的</h2>
<p>M：Model，数据模型，比如我们人类有一双手，一双眼睛，一个脑袋，没有尾巴，这就是模型，Model定义了这个模块的数据模型。在代码中体现为数据管理者，Model负责对数据进行获取及存放。数据不可能凭空生成的，要么是从服务器上面获取到的数据，要么是本地数据库中的数据，也有可能是用户在UI上填写的表单即将上传到服务器上面存放，所以需要有数据来源。既然Model是数据管理者，则自然由它来负责获取数据。Controller不需要关心Model是如何拿到数据的，只管调用就行了。数据存放的地方是在Model，而使用数据的地方是在Controller，所以Model应该提供接口供controller访问其存放的数据（通常通过.h里面的只读属性）。</p>
<p>V：View，视图，简单来说，就是我们在界面上看见的一切。大多数情况都是继承自UIView的类的对象，而有时候则不是直接继承自UIView，有时候会直接用CoreAnimation甚至CoreGraphics来绘制内容，但这些东西统统都归结为MVC中的View。它们有一部分是我们UI定死的，也就是不会根据数据来更新显示的，比如一些Logo图片啊，这里有个按钮啊，那里有个输入框啊，一些显示特定内容的label啊等等；有一部分是会根据数据来显示内容的，比如tableView来显示好友列表啊，这个tableView的显示内容肯定是根据数据来显示的。我们使用MVC解决问题的时候，通常是解决这些根据数据来显示内容的视图。这里要提个醒：MVC虽然看似把模块分为了三部分，但是并不是说一个模块就要一定建三个类出来，比如联系人列表（ContactsList）模块，一定会有的肯定是ContactsListViewController，然后我们使用MVC来作为内部的框架，则需要创建ContactsListModel类，接下来会有少年继续创建ContactsListView，他认为这才是MVC，有三个类分别是XXXModel、XXXController、XXXView，这就大错特错了，你们在Controller中使用的UILabel、UITableView等等就是MVC中的View了，不要再专门建一个XXXXView出来，完全是没事找事多此一举。</p>
<p>C：Controller，最熟悉却又最抽象的一个东西。之所以熟悉，我们在使用UIKit进行开发中我敢说是你打交道最多的类：UIViewController。UIKit框架离不开UIViewController，当然你完全可以使用UIView来完成所有本该由Controller完成的事情，这是大逆不道的，因为这样做将会使你的整个项目代码一团糟，并且完美的违背了面向对象的思想：各司其职。这里大家一定要知道UIViewController究竟应该做些什么事，实际上就是API提供出来的接口：self.view用来作为所有视图的容器；管理自己的生命周期；controller之间的转场；controller容器。这是Controller的本职工作，然而它往往还需要承担起MVC中的数据和视图的协调者，也就是在Controller里面把Model的数据赋值给View来显示（或者是View接收用户输入的数据然后由Controller把这些数据传给Model来保存到本地或者上传到服务器）</p>
<h2 data-id="heading-4">小结</h2>
<p>综合以上内容，实际上你应该可以通过面向对象的基本思想来推导出controller出现的原因：我们所有的App都是界面和数据的交互，所以需要类来进行界面的绘制，于是出现了View，需要类来管理数据于是出现了Model。我们设计的View应该能显示任意的内容比如UILabel显示的文字应该是任意的而不只是某个特定Model的内容，所以我们不应该在View的实现中去写和Model相关的任何代码，如果这样做了，那么View的可扩展性就相当低了。而Model只是负责处理数据的，它根本不知道数据到时候会拿去干啥，可能拿去作为算法噼里啪啦去了，可能拿去显示给用户了，它既然无法接收用户的交互，它就不应该去管和视图相关的任何信息，所以Model中不应该写任何View相关代码。然而我们的数据和界面应该同步，也就是一定要有个地方要把Model的数据赋值给View，而Model内部和View的内部都不可能去写这样的代码，所以只能新创造一个类出来了，取名为Controller。它被UIKit逐渐完善成了我们现在使用的UIViewController。</p>
<h2 data-id="heading-5">看图说话</h2>
<p>你要问我以上这么一大堆东西我是怎么知道的？我就完成了一次看图说话而已，我们终于要开始讲解这张图了，为了更好的观看体验，我再次向您呈现出这张图，这样你就不需要往上面翻一大段内容了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31df81f5cc324bf0a6e348bbd168a564~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>废话不多说了，这张图把MVC分为三个独立的区域，并且中间用了一些线来隔开。很有意思的设计，因为这些线似乎出现在了驾校科目一的内容中，你瞧C和V以及C和M之间的白线，一部分是虚线一部分是实线对吧，这就表明了引用关系：C可以直接引用V和M，而V和M不能直接引用C，至少你不能显式的在V和M的代码中去写和C相关的任何代码，而V和M之间则是双黄线，没错，它们俩谁也不能引用谁，你既不能在M里面写V，也不能在V里面写M。哦，上面的描述有点小小的问题，你不是“不能”这样写，而是“不应该”这样写，没人能阻止你在写代码的时候在一个M里面去写V，但是一旦你这样做了，那么你就违背了MVC的规范，你就不是在使用MVC了，所以这算是MVC的一个必要条件：使用MVC –> M里面没有V的代码。所以M里面没有V的代码就是使用MVC的必要条件，如果P->Q，那么~Q->~P，初中还是高中数学讲过吧，如果你在M里面写了V的代码，那么你就不是在使用MVC了。之前我见过什么字典转模型，然后把模型赋值给一个Cell在Cell内部解析模型来显示的，这我只能说你用的不是MVC。</p>
<p>它们三个分别是什么，干什么事，我在一开始就说清楚了。所以现在我们来看看它们如何进行交互，你可以理解为如何传值。</p>
<h2 data-id="heading-6">View和Controller的交互</h2>
<p>iOS中的传值包括了事件的传递，比如按钮点击事件，是View来接收的，但是处理这个事件的应该是Controller，所以View把这个事件传递给了Controller，如何传递的呢，见图，看到View上面的action没有，这就是事件，看到Controller上面的target没有，这就是靶子，View究竟要把事件传递给谁，它被规定了传递给靶子，Controller实际上就是靶子，你们为按钮添加点击事件怎么写的？[按钮 添加靶子：我 事件：xxx …]；只是View只负责传递事件，不负责关心靶子是谁。就像你是一个负责运货的少年，你唯一知道的是你要把货（action）交给上头（开发者）告诉你的那个收货的人（target），至于那个收货的人是警察还是怪兽，你都不需要关心。这是V和C的一种交互方式，叫做target-action。所以你看，这张图简直就是神来之笔，旁边还栩栩如生的画出了V对C的另一种传值：协议-委托。委托有两种：代理和数据源。什么是代理，就是专门处理should、will、did事件的委托，什么是数据源，就是专门处理data、count等等的委托。你们用的最多的，tableView用过吧，没用过还敢说你是做iOS开发的？你们有没有想过为什么tableView需要数据源来实现协议方法而不是直接把数据通过属性传给tableView？如果你来我这面试，恭喜你，你将会有幸被问到这个问题。</p>
<p>tableView并不像简单的视图那样显示简单的内容，它要显示的内容之丰富，它自己都不知道，它被设计为能显示任意多分组、每个分组任意多个单元格、每个单元格上面能显示任意内容、甚至每个单元格的高度都不一样等等，这样苛刻的条件，绝对不是一次简单的属性赋值就能解决的。然而这样类似的东西早在C语言库函数中就有了传说：我们牛X的排序函数。这个排序函数被设计为能为任意类型的数组进行排序，管你是整型数组还是字符串数组，还是你搞的奇奇怪怪的结构体数组，劳资都能排！没错，如果你学习过回调函数，那么你一定接触过这个牛X的排序函数的例子，对任意类型数组进行排序唯一的问题在于：数组中的元素的比较规则。实际上这个问题用代码来描述起来：排序函数S在排序的过程中，需要不停比较数组中某两个元素，S通过比较的结果来进行排序操作。意味着S只需要比较结果，至于如何比较，就由调用方提供的回调函数来决定，你让劳资帮你排序这个数组，你TM还不知道这个数组里面的东西如何比较，那我排个毛？所以问题解决了：S函数需要由调用方提供一个函数指针作为参数，这个函数指针指向的函数接收两个参数并返回这两个参数比较的结果，S只需要在需要比较的时候调用这个函数指针指向的函数，传入S想要比较的两个元素，拿到返回的比较结果就行了。</p>
<p>所以，明白了吧，tableView如何来实现那么苛刻的效果：我（tableView）在绘制的时候需要调用方提供方法给我，我只要结果不要过程！我先通过参数告诉你，我现在在画第1个section啦，你快告诉我这个section下面有多少个单元格？也就是调用[self.dataSource tableView:self numberOfRowsInSection:section]的返回值就是在section下有多少个单元格，tableView只需要不停的调用方法获取结果，绘制和数据处理的逻辑都在调用方（dataSource）。就像一个孩子一样，tableView一直在问问题，dataSource一直在回答tableView的问题，问题问完了，tableView就画出来了。tableView被这样设计出来以后，任意类都可以调用它，但是呢，调用tableView是有条件的，那就是你必须要有能解决我问题的能力，这就是协议的诞生：你要用我是吧，那你得能够回答上我的问题。所谓能回答上tableView的问题，也就是实现了tableView所声明的协议。</p>
<p>dataSource通过回调的形式，让绘制逻辑由dataSource控制（dataSource协议方法的实现）而绘制过程则由V来进行（dataSource协议方法的调用）。调用方V通过参数把值传给实现方dataSource，实现方通过返回值把值回传给调用方，这样V就通过不停的调用dataSource方法获取它所需要的绘制信息，最终绘制出界面。</p>
<p>往往V的dataSource都是一个C，而C在实现dataSource协议的时候是通过M里面的数据来实现的，这样就相当于由C把M间接地赋值给了V。</p>
<p>同样的，delegate协议也是一种回调，它处理的更多是一种事件，看那几个单词：should、will、did，都是一种询问的形式，我该不该怎样怎样，我将要怎样怎样啦，我已经怎样怎样啦… 当这样的询问需求发生了以后（比如scrollView将要被拖动的一瞬间(willBeginDraging…)，scrollView停止减速的一瞬间(didEndDecelarating…)等等），V就会调用delegate相应的方法。比如tableView单元格的点击事件，是由V来直接接收到的（因为用户直接操作的对象都是V），而需要处理这个点击事件的地方应该在C，所以V应该通过某种方式告知C，有个Cell被点击啦（didSelectRowAtIndexPath…），并且还要能告知C，是哪个Cell（indexPath）被点击了，所以当cell被点击的时候 ，V就通过调用delegate实现的协议方法，这样点击事件的处理就相当于交给了delegate来实现了，并通过参数告知delegate这次是哪个cell被点击了。简单来说，就是V和它的delegate之间事前已经约定好了一个协议，一旦V将要、已经怎样怎样的时候，就按照协议实现的内容去做。所谓按照协议实现的内容去做，就是让delegate调用协议方法。这样就相当于，V将要、已经怎样怎样的时候，在delegate里面相应的实现的协议方法就会被调用。</p>
<p>以上就是V向C传值的设计，总结一下，就是主要通过三种方式：action-target用来负责传递特定的事件；dataSource-protocol用来通过回调的形式动态通过数据绘制界面；delegate-protocol提前约定了对一些事件的处理规则，当被规定的事件发生后，就按照协议的规定来进行处理。协议委托可以通过协议方法的参数由V向C传值。比如cell点击事件的协议方法，tableView通过indexPath参数告诉C是哪个cell被点击了。</p>
<h2 data-id="heading-7">Model和Controller的交互</h2>
<p>接下来看看从MVC出生到现在为止争议比较大的，M和C的交互。</p>
<p>我们从M的作用开始说起。</p>
<p>M是干嘛的？上面说了，M就是数据管理者，你可以理解为它直接和数据库打交道。这里的数据库可能是本地的，也可能是服务器上的，M会从数据库获取数据，也可能把数据上传给数据库。M也将提供属性或者接口来供C访问其持有的数据。我们就拿一个简单的需求作为例子，假如我想在一个模块中显示一段文字，这段文字是从网上获取下来的。</p>
<p>那么使用MVC的话，在C中肯定需要一个UILabel（V）作为属性来显示这段文字，而这段文字由谁来获取呢，肯定是由M来获取了。而获取的地方在哪里呢？通常在C的生命周期里面，所以往往是在C的一个生命周期方法比如viewDidLoad里面调用M获取数据的方法来获取数据。现在问题来了，M获取数据的方法是异步的网络请求，网络请求结束后，C才应该用请求下来的数据重新赋值给V，现在的问题是，C如何知道网络请求结束了？</p>
<p>这里我们一定要换一种角度去思考，我们进一步考虑M和V之间的关系：它们应该是一种同步的关系，也就是，不管任何时刻，只要M的值发生改变，V的显示就应该发生改变（显示最新的M的内容）。所以我们可以关注M的值改变，而不用关心M的网络请求是否结束了。实际上C根本不知道M从哪去拿的数据，C的责任是负责把M最新的数据赋值给V。所以C应该关注的事件是：M的值是否发生了变化。</p>
<p>所以我们只需要解决“C如何知道M的值发生了变化”这个问题。</p>
<p>幸运的是在OC中有一种机制恰好就是来解决“一个对象想要关心另一个对象的属性是否发生了变化”的问题，它叫做KVO。（见图）</p>
<p>KVO叫做键值观察，它让一个对象作为观察者去观察另一个对象的由某个键值路径所代表的属性，一旦这个属性发生了变化，那么系统就会调用观察者的一个方法叫做observingValueForKeyPath:…。比如C想要在M的data属性发生改变后刷新界面，那么就只需要向M添加观察者C，观察路径为@”data”，这样就相当于对C来讲，一旦M.data发生了变化，那么C的observingValueForKeyPath方法就会被调用，就可以在这个方法的实现中写self.label.text = self.model.data;这样就实现了M和V的同步。</p>
<p>图上还标明了一个东西叫做Notification也就是通知，比如你想网络请求失败以后应该弹出提示框，或者自动登录打开App请求首页数据失败想要返回到登录页面重新登录，这样的操作肯定应该在C里面进行，所以M的网络请求一旦失败，就可以向C发送一个通知，来告诉C，网络请求失败啦，你自己看着办。</p>
<p>我之所以说这里有争议，是因为block的出现。Block的出现完美的解决了一些回调实现起来很麻烦的问题，block的回调相当方便简单。这里完全可以由C向M传一个block，M在网络请求结束后调用block。但是呢，这样做我个人认为有些违背M的设计思想和面向对象的思想。M在网络请求获取数据后应该只负责更新自己的数据，它不应该去调用某个block，它不知道自己被一个C持有了，所以对它来讲，它不能主动调用任何东西，只能被动地，毫不知情地告诉C我的数据发生变化了。而KVO对于被观察的对象来讲恰好就是被动的：M根本不知道自己被观察了，M还是按部就班地把新数据赋值给自己的属性，而不用再额外做其他它不应该做的事。</p>
<p>这是我个人的理解，当然使用block从代码的实现上来讲会方便的多，效率也比KVO在运行时稍高，毕竟KVO的实现原理是在运行时动态创建类。但是我个人还是倾向于在MVC中使用KVO而不是block，仁者见仁智者见智，能解决问题的方法就是好方法，这里就不再讨论了。</p>
<h2 data-id="heading-8">一言不合上代码</h2>
<p>讲了这么多，还是来一个demo比较实在。我这里将用GCD的延迟方法模拟一次网络请求获取数据，使用MVC来实现一个异步网络请求并在获取数据后刷新一个表视图。</p>
<p>准备工作：
既然使用MVC，那么必不可少的，首先需要一个Model类。类的名字可以根据当前这个模块来定，比如这个模块是一个新闻列表，那么就可以简单的叫做NewsModel，当然类名应该加上自己的前缀这样比较规范比如就叫做DHNewsModel。</p>
<p>我们这个类建出来以后应该开始着手实现它。</p>
<p>如何实现MVC，可以完全按照上面那张图来实现。首先Model是用来负责和数据打交道的，更具体一点，也就是对数据的存和取。取是用方法进行网络请求或者和本地数据库打交道，存则是把取到的数据放进自己的一个属性以供外界访问。所以理所应当的，Model的头文件应该有两个方法：一个只读属性用来存数据、一个实例方法用来取数据：</p>
<pre><code class="copyable">@interface DHNewsModel : NSObject

@property (nonatomic, strong, readonly) id dataList;

- (void)getData;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们通常都不知道获取到的数据究竟是什么鬼，所以这个属性用了id来声明。</p>
<p>而在.m里面则是简单的实现。getData方法就是调用网络请求，你可以使用系统的URL Session，也可以用AFNetworking或者你比较牛逼直接封装CFNetwork。那我这里就简单的模拟一次网络请求，网络请求的效果就是：延迟获取一段数据，所以我的getData方法就这样实现了。</p>
<pre><code class="copyable">@interface DHNewsModel ()

@property (nonatomic, strong) id dataList;

@end


@implementation DHNewsModel

- (void)getData
&#123;
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(3 * NSEC_PER_SEC)), dispatch_get_main_queue(), ^&#123;
        self.dataList = @[@&#123;@"title":@"新闻一",
                            @"date":@"2016-01-25",
                            @"image":@"http://g.hiphotos.baidu.com/image/h%3D300/sign=bd5cccb88b5494ee982209191df4e0e1/c2cec3fdfc039245980aac088094a4c27d1e257d.jpg",
                            @"content":@"blablabla"&#125;,
                          @&#123;@"title":@"新闻二",
                            @"date":@"2016-01-27",
                            @"image":@"http://a.hiphotos.baidu.com/image/h%3D300/sign=8d9d3903900a304e4d22a6fae1c9a7c3/ac4bd11373f082022a2ddc384cfbfbedab641b7d.jpg",
                            @"content":@"ahahaha"&#125;];

    &#125;);
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们的Model就写完了。再次强调，Model只负责对数据进行存和取，我们实现了取数据的方法（getData），也实现了存数据（获取数据后用数据给dataList赋值）。</p>
<p>接下来就是Controller的实现了。</p>
<p>我们的C应该持有M和V，所以理所应当的应该有一个Model的属性。C和M的交互应该是这样的：C观察M的属性，在KVO的回调中刷新界面。而V和M的交互是这样的：在C中，C用M的属性对V的属性进行赋值。</p>
<p>于是我们的C的实现就是这个样子了：</p>
<pre><code class="copyable">#import "ViewController.h"
#import "DHNewsModel.h"

@interface ViewController () <UITableViewDataSource, UITableViewDelegate>

@property (nonatomic, strong) UITableView * tableView;
@property (nonatomic, strong) DHNewsModel * model;

- (void)_registerObeserver;
- (void)_unregisterObserver;

@end

@implementation ViewController

- (void)dealloc
&#123;
    [self _unregisterObserver];
&#125;

- (instancetype)init
&#123;
    self = [super init];
    if (self) &#123;

    &#125;
    return self;
&#125;

- (void)viewDidLoad &#123;
    [super viewDidLoad];
    [self.view addSubview:self.tableView];
    // 1、我想要请求数据
    [self.model getData];
    // 2、数据请求成功后（model的数据更新后）我应该接收回调然后用model最新的数据刷新界面
    // model跟view要在任意时刻保持同步
    // KVO
    [self _registerObeserver];

&#125;

#pragma mark - private methods
- (void)_registerObeserver
&#123;
    [self.model addObserver:self forKeyPath:@"dataList" options:NSKeyValueObservingOptionNew context:nil];
&#125;

- (void)_unregisterObserver
&#123;
    [self.model removeObserver:self forKeyPath:@"dataList"];
&#125;

#pragma mark - callback
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
&#123;
    [self.tableView reloadData];
&#125;

- (UITableView *)tableView
&#123;
    if (!_tableView) &#123;
        _tableView = [[UITableView alloc] initWithFrame:self.view.bounds style:UITableViewStylePlain];
        _tableView.dataSource = self;
        _tableView.delegate = self;
        _tableView.tableFooterView = [[UIView alloc] init];

    &#125;
    return _tableView;
&#125;

#pragma mark - getter
- (DHNewsModel *)model
&#123;
    if (!_model) &#123;
        _model = [[DHNewsModel alloc] init];
    &#125;
    return _model;
&#125;

#pragma mark - UITableViewProtocol
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
&#123;
    return [self.model.dataList count];
&#125;

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
&#123;
    UITableViewCell * cell = [tableView dequeueReusableCellWithIdentifier:@"cellIdf"];
    if (!cell) &#123;
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@"cellIdf"];
    &#125;
    NSDictionary * infoDic = self.model.dataList[indexPath.row];
    cell.textLabel.text = infoDic[@"title"];
    cell.detailTextLabel.text = infoDic[@"date"];
    NSURL * imageUrl = [NSURL URLWithString:infoDic[@"image"]];

    dispatch_async(dispatch_get_global_queue(0, 0), ^&#123;


        NSData * imageData = [NSData dataWithContentsOfURL:imageUrl];
        UIImage * image = [UIImage imageWithData:imageData];

        dispatch_async(dispatch_get_main_queue(), ^&#123;
            cell.imageView.image = image;
        &#125;);

    &#125;);

    return cell;
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们这里使用了KVO来实现V和M的同步，再次说明，你完全可以用block来进行回调，我这里只是认为KVO更符合M的设计而已。</p>
<h1 data-id="heading-9">MVVM</h1>
<h2 data-id="heading-10">什么是MVVM（what）</h2>
<p>MVVM：Model、View、ViewModel。</p>
<p>你会下意识地把它和MVC来对比，你会发现，MVVM多了一个ViewModel而少了Controller。</p>
<p>首先说一下多出来的ViewModel（VM，不是显存）。
VM的意义，和Model一样，在于数据。
Model负责对数据进行取和存，然而我们对数据的操作除了取和存以外，还有一个非常重要的操作：解析。</p>
<h2 data-id="heading-11">MVVM为什么会出现，为什么要用MVVM解决一些问题（why）</h2>
<p>想象一下我们的Model获取的数据是系统的时间，也就是一个NSDate类型的对象，而Controller需要用一个UILabel来显示这个时间，这样的话，由于Model里面存放的是NSDate，所以当Controller给Label赋值的时候需要将NSDate转换为NSString，这一步转换的操作就叫做数据解析。更具体一点的对数据解析的解释：把原始数据转换成View能直接使用的数据。比如一个UILabel直接使用的数据是一个NSString而不是Model里面存放的原始数据NSDate。</p>
<p>更常见的一些例子比如网络请求获取下来一个字典（往往使用JSON格式封装的数据都会以字典的形式获取到），这个字典将作为原始数据存放在Model中。而我们的Controller实际上需要字典中某个key对应的一个数组，然后用这个数组来控制一个UITableView的显示。</p>
<p>以上例子表明了我们往往在不知不觉中把数据解析的操作放到了Controller里面。就像我们之前分析MVC是如何合理分配工作的一样，我们需要数据所以有了M，我们需要界面所以有了V，而我们需要找一个地方把M赋值给V来显示，所以有了C，然而我们忽略了一个很重要的操作：数据解析。在MVC出生的年代，手机APP的数据往往都比较简单，没有现在那么复杂，所以那时的数据解析很可能一步就解决了，所以既然有这样一个问题要处理，而面向对象的思想就是用类和对象来解决问题，显然V和M早就被定义死了，它们都不应该处理“解析数据”的问题，理所应当的，“解析数据”这个问题就交给C来完成了。而现在的手机App功能越来越复杂，数据结构也越来越复杂，所以数据解析也就没那么简单了。如果我们继续按照MVC的设计思路，将数据解析的部分放到了Controller里面，那么Controller就将变得相当臃肿。还有相当重要的一点：Controller被设计出来并不是处理数据解析的。Controller能做的事情在之前已经说过了，我再次说明一下，是根据UIKit框架API对UIViewController头文件的定义：1、self.view用来作为所有视图的容器；2、管理自己的生命周期；3、处理Controller之间的跳转；4、实现Controller容器。这里面根本没有“数据解析”这一项，所以显然，数据解析也不应该由Controller来完成。那么我们的MVC中，M、V、C都不应该处理数据解析，那么由谁来呢？这个问题实际上在面向对象的时候相当好回答：既然目前没有类能够处理这个问题，那么就创建一个新的类出来解决不就好了？所以我们聪明的开发者们就专门为数据解析创建出了一个新的类：ViewModel。这就是MVVM的诞生。</p>
<h2 data-id="heading-12">如何实现MVVM（how）</h2>
<p>搞清楚了MVVM为什么会出现，将对于你理解如何实现MVVM有极大的帮助。在我们开始着手实现MVVM之前，我先简单提一下之前遗留的一个问题：为什么MVVM这个名字里面，没有Controller的出现（为什么不叫MVCVM，C去哪了）。本来这个问题应该在实现后再来解释，但是我们这里是教学，为了让大家更好的明白我们接下来的思想，所以这里要提前解释一下这个结论：Controller的存在感被完全的降低了。我们在待会实现MVVM的时候你就能体会到了，这里请先把这个结论印在脑海当中：Controller的存在感被完全的降低了、Controller的存在感被完全的降低了、Controller的存在感被完全的降低了。</p>
<p>好的，我们终于要开始着手实现MVVM了。如果你已经搞懂了MVC，那么用MVVM实现一个相同的功能将会变得非常简单。你只需要记住两点：1、Controller的存在感被完全的降低了；2、VM的出现就是Controller存在感降低的原因。</p>
<h2 data-id="heading-13">先来点理论性的准备工作</h2>
<p>在MVVM中，Controller不再像MVC那样直接持有Model了。想象Controller是一个Boss，数据是一堆文件（Model），如果现在是MVC，那么数据解析（比如整理文件）需要由Boss亲自完成，然而实际上Boss需要的仅仅是整理好的文件而不是那一堆乱七八糟的整理前的文件。所以Boss招聘了一个秘书，现在Boss就不再需要管理原始数据（整理之前的文件）了，他只需要去找秘书：你帮我把文件整理好后给我。那么这个秘书就首先去拿到文件（原始数据），然后进行整理（数据解析），接下来把整理的结果给Boss。所以秘书就是VM了，并且Controller（Boss）现在只需要直接持有VM而不需要再持有M了。如果再进一步理解C、VM、M之间的关系：因为Controller只需要数据解析的结果而不关心过程，所以就相当于VM把“如何解析Model”给封装起来了，C甚至根本就不需要知道M的存在就能把工作做好，前提它需要持有一个VM。那么我们MVVM中的持有关系就是：C持有VM，VM持有M。这里有一个比较争议的地方：C该不该持有M。我的答案是不该。为什么呢，因为C持有M没有任何意义。就算C直接拿到了M的数据，它还是要去让VM进行数据解析，而数据解析就需要M，那么直接让VM持有M而C直接持有VM就足够了。最后再分享一个我在实现MVVM中的一个技巧，也谈不上是技巧吧，算是一种必要的思想：一旦在实现Controller的过程中遇到任何跟Model（或者数据）相关的问题，就找VM要答案。这个思想待会我们会在实现代码的时候用到。</p>
<h2 data-id="heading-14">一言不合上代码2.0</h2>
<p>弄清了这样的关系后，终于可以开始着手实现了。显然，MVVM也需要Model，并且MVVM中的Model和MVC中的Model完全一致，所以我们上一个MVC的demo中的Model可以一行代码都不动保持原样，然后我们需要新建一个类出来，它叫做DHNewsViewModel。时刻注意，VM就像C的秘书一样，它要做什么，完全取决于C的命令。所以如果一开始你不知道VM里面应该写些什么，就先放着，当C遇到了和数据相关的任何问题，你就知道VM应该提供什么东西出来了。</p>
<p>我们上一个MVC的demo中的Model可以直接拿来用，所以在这里写MVVM的demo的时候你可以新建一个工程出来然后把MVC的Model拷贝进新的工程或者直接在原有MVC工程的基础上进行修改来实现MVVM。</p>
<p>不管你使用哪一种方式来进行MVVM的实现，都需要将Controller中的代码重新进行实现，所以，如果你在原有工程基础上进行修改的话，就要把Controller中的代码该删的删完，就像你刚建一个Controller类文件出来的那样，只保留延展的声明和ViewDidLoad方法的空的实现（如果基于新的工程则不需要这样做）。</p>
<p>这时我们的工程中就已经拥有了完整的Model，我们知道VM应该持有一个M，所以可以在.m中写一个延展来声明一个私有的M属性。</p>
<pre><code class="copyable">#import "DHNewsViewModel.h"
#import "DHNewsModel.h"
#import <UIKit/UIKit.h>

@interface DHNewsViewModel ()

@property (nonatomic, strong) DHNewsModel * model;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照我们之前的设计，Controller除了完成它的日常（初始化各种View并对View进行赋值）外，还应该持有一个ViewModel来负责进行数据解析。所以你可以先把ViewModel类建好，然后在Controller里面写一个私有的属性。这里我为ViewModel类取名为DHNewsViewModel。然后在Controller的实现文件中，首先是延展：</p>
<pre><code class="copyable">#import "ViewController.h"
#import "DHNewsViewModel.h"

@interface ViewController () <UITableViewDataSource, UITableViewDelegate>

@property (nonatomic, strong) UITableView * tableView;
@property (nonatomic, strong) DHNewsViewModel * viewModel;

- (void)_registerObeserver;
- (void)_unregisterObserver;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以对比MVC，仅仅是从持有Model换成了持有一个ViewModel。然后我们来实现私有方法进行KVO的注册和移除。</p>
<p>在实现之前，我们需要知道观察者的keyPath是什么。</p>
<p>解决这样的问题首先我们应该思考我们要什么效果，这里我们要的效果是：Controller能观察到Model里面一个叫dataList属性的变化。那么应该建立一个Controller到这个属性的keyPath路径。由于我们的持有关系是Controller持有ViewModel，ViewModel持有Model，这样的话我们在Controller里面注册观察者就只能给ViewModel来添加观察者。我们最终要观察的是Model的属性，而添加观察者的地方在Controller，而Controller不知道ViewModel是如何持有Model的（ViewModel持有Model属性的名称，或者说变量名，因为keyPath观察路径是和属性名称相关的），并且Controller也不知道Model中那个它想要观察的属性的名字叫什么（我把Controller拟人化了，虽然我们作为开发者确实知道所有属性的名字，可以在Controller中写出来，但是从面向对象的角度，应该把这些信息封装起来，所以Controller作为一个类它是无法知道这些信息的，它不该知道的信息就不应该在Controller中去写出来）。这样的话，keyPath的值应该大概就是@”vieModel中持有的那个model的变量名.model中那个数据的变量名”，这两个信息都是Controller不知道的。那我们该怎么添加观察者呢？
说明：我上面花了一大堆貌似可有可无的描述，只是为了告诉大家，一定要形成这样的思想，对于一个类，它不该知道的，不该做的事，就一定不要让它知道，不要让它去做，之所以要这样设计，主要是因为耦合度的问题，以后修改某个地方不会影响其他地方；并且出了问题以后，能够快速锁定问题出在哪里，因为所有的类各司其职，分工明确。如果所有的类都参与了这个问题，那么你很难找到问题到底出在哪个类身上。一个类暴露的信息越多，那么能使用它的地方就越多，显然就可能造成更高的耦合度，并且使用起来也更为“让人感到困扰”。这个类的.h里面有那么多属性，这些属性有什么意义？这个属性如果我不给它赋值会有什么问题？这样会给调用方或者业务逻辑的实现方产生大量的困扰，显然是对开发很不利的。所以有些属性，该readonly就readonly，该作为私有属性就要弄成私有属性。</p>
<p>好了，既然Controller不知道观察者路径，那观察者应该如何注册？这里我们进一步分析，Controller不知道路径是因为要观察的内容是Model的东西，还记得上面我提到的一个思想吗？Controller一旦遇到和Model相关的任何问题，都可以找ViewModel要。所以，我们的keyPath就应该由ViewModel提供一个方法出来供Controller调用。</p>
<p>这里我推荐大家先理一理上面的关系，从延展的@end到上一段话，中间的文字希望大家能好好去思考总结。最后为什么ViewModel应该提供一个方法给Controller来获取观察者路径，这里如果能理解了，那么接下来要做的事情就相当清晰明了了。</p>
<p>我们在ViewModel的.h里面就能添加一个方法了</p>
<pre><code class="copyable">- (NSString *)observingKeyPath;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法将返回观察者路径，在.m中可以直接实现：</p>
<pre><code class="copyable">- (NSString *)observingKeyPath
&#123;
    return @"model.dataList";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后回到Controller中来调用。</p>
<pre><code class="copyable">#pragma mark - private methods
- (void)_registerObeserver
&#123;
    [self.viewModel addObserver:self forKeyPath:[self.viewModel observingKeyPath] options:NSKeyValueObservingOptionNew context:nil];
&#125;

- (void)_unregisterObserver
&#123;
    [self.viewModel removeObserver:self forKeyPath:[self.viewModel observingKeyPath]];
&#125;   

<span class="copy-code-btn">复制代码</span></code></pre>
<p>记住在dealloc中调用unregister方法。</p>
<p>这样就相当于直接调用了</p>
<pre><code class="copyable">[self.viewModel addObserver:self forKeyPath:@”model.dataList” options:NSKeyValueObservingOptionNew context:nil];

<span class="copy-code-btn">复制代码</span></code></pre>
<p>搞清楚上面的内容后，我们剩下的操作，实际上就是“Controller要什么，ViewModel就给什么”。老板要，秘书就给（别想歪）。</p>
<p>我们继续实现Controller。私有方法写好了以后，在ViewDidLoad里面调用注册观察者。同时还要进行网络请求来获取数据。没错，问题又来了。网络请求的方法在Model里面，而Controller拿不到Model，那怎样在Controller的ViewDidLoad方法里面进行网络请求？同样的答案：ViewModel提供方法供Controller调用。“你不是想网络请求吗？我可以调用Model进行网络请求，那么我提供方法给你，你想要网络请求的时候调这个方法就行了，我在这个方法中实际上就是让Model去进行网络请求了。”ViewModel对Controller说道。</p>
<p>所以在ViewModel的.h中又声明一个新的方法：</p>
<pre><code class="copyable">- (void)getData;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现很简单：</p>
<pre><code class="copyable">- (void)getData
&#123;
    [self.model getData];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在Controller的ViewDidLoad中只需要调用ViewModel的getData方法就相当于调用了model的getData方法，这样就开始网络请求了:</p>
<pre><code class="copyable">- (void)viewDidLoad &#123;
    [super viewDidLoad];
    [self.view addSubview:self.tableView];
    [self.viewModel getData];
    [self _registerObeserver];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>/*顺便提一下，这个tableView的getter方法和MVC里面的一模一样，我就不再单独拿出来写了。说到getter，记住写viewModel的getter哈！</p>
<p>算了我还是把代码贴在这里吧，谁叫我这么负责呢！*/</p>
<p>KVO的回调以及getter的相关代码：</p>
<pre><code class="copyable">#pragma mark - callback
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
&#123;
    [self.tableView reloadData];
&#125;

#pragma mark - getter
- (UITableView *)tableView
&#123;
    if (!_tableView) &#123;
        _tableView = [[UITableView alloc] initWithFrame:self.view.bounds style:UITableViewStylePlain];
        _tableView.dataSource = self;
        _tableView.delegate = self;
        _tableView.tableFooterView = [[UIView alloc] init];

    &#125;
    return _tableView;
&#125;

- (DHNewsViewModel *)viewModel
&#123;
    if (!_viewModel) &#123;
        _viewModel = [[DHNewsViewModel alloc] init];
    &#125;
    return _viewModel;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>走到了这一步，你会发现，只剩下tableView的dataSource的实现了。</p>
<p>我们接下来就来实现协议方法：</p>
<p>一个一个来，首先是返回某个section下面有多少行cell的方法。</p>
<p>在实现这个方法的时候，你会发现，啊，这里Controller似乎又遇到问题了：多少行cell应该取决于我们model的dataList里面有多少条数据。</p>
<p>没错，所以我现在说Controller想要了，ViewModel应该怎么办？给！</p>
<p>在ViewModel的.h里面提供方法给Controller来计算第section个分组下面应该有多少行cell：</p>
<pre><code class="copyable">- (NSInteger)numberOfRowsInSection:(NSInteger)section;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现这个方法，是根据model的数据挂钩的，所以你会发现，似乎是MVC的Controller里面跟数据相关的代码全部由ViewModel代替它实现了。</p>
<pre><code class="hljs language-js copyable" lang="js">- (NSInteger)numberOfRowsInSection:(NSInteger)section
&#123;
    <span class="hljs-keyword">return</span> [self.model.dataList count];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在Controller中，这个协议方法的实现就变成了：</p>
<pre><code class="copyable">- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
&#123;
    return [self.viewModel numberOfRowsInSection:section];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>稍微对比一下MVC中的实现，会发现实际上最终都是直接返回了model中dataList的count，只是实现的地方从Controller变到了ViewModel。</p>
<p>有感觉了吗？</p>
<p>还剩下一个返回cell的方法。我会在最后把VM和Controller完整的代码贴出来，但是我希望这个返回cell的方法你们能先尝试自己去实现和VM的交互。</p>
<p>只需要记住一句话：Controller要什么，VM就给什么（和Model相关的）。</p>
<p>还记得我一开始说的，Controller的存在感被完全的降低了吗？实现完整后你在好好体会一下Controller里面的代码，看看是不是变得很“脑残了”，完全没有什么逻辑了，全是调方法。我们就应该要这样简洁的Controller。</p>
<p>这个例子实际上是比较简单的数据处理，在实际项目运用中你会发现MVVM使用起来解决一些问题相当方便，并且在后期改BUG和维护添加功能的时候相当快捷。</p>
<h1 data-id="heading-15">后记</h1>
<p>多用几次MVVM，你一定就能够非常熟练的使用它的思想了，并且我相信在这个过程中你的面向对象的思维也能够得到提高。</p>
<p>接下来你可以尝试用MVVM来实现这样一个小小的demo：Controller中用一个label现实系统当前时间。</p>
<p>提示：Model负责获取系统时间，然后存在属性中，VM负责把它从NSDate转换成NSString，Controller负责显示。</p>
<pre><code class="hljs language-js copyable" lang="js">#<span class="hljs-keyword">import</span> <span class="hljs-string">"ViewController.h"</span>
#<span class="hljs-keyword">import</span> <span class="hljs-string">"DHNewsViewModel.h"</span>

@interface ViewController () <UITableViewDataSource, UITableViewDelegate>

@property (nonatomic, strong) UITableView * tableView;
@property (nonatomic, strong) DHNewsViewModel * viewModel;

- (<span class="hljs-keyword">void</span>)_registerObeserver;
- (<span class="hljs-keyword">void</span>)_unregisterObserver;

@end

@implementation ViewController

- (<span class="hljs-keyword">void</span>)dealloc
&#123;
    [self _unregisterObserver];
&#125;

- (<span class="hljs-keyword">void</span>)viewDidLoad &#123;
    [<span class="hljs-built_in">super</span> viewDidLoad];
    [self.view addSubview:self.tableView];
    <span class="hljs-comment">// 1、我想要请求数据</span>
    [self.viewModel getData];
    <span class="hljs-comment">// 2、数据请求成功后（model的数据更新后）我应该接收回调然后用model最新的数据刷新界面</span>
    <span class="hljs-comment">// model跟view要在任意时刻保持同步</span>
    <span class="hljs-comment">// KVO</span>
    [self _registerObeserver];

&#125;

#pragma mark - private methods
- (<span class="hljs-keyword">void</span>)_registerObeserver
&#123;
    [self.viewModel addObserver:self forKeyPath:[self.viewModel observingKeyPath] options:NSKeyValueObservingOptionNew context:nil];
&#125;

- (<span class="hljs-keyword">void</span>)_unregisterObserver
&#123;
    [self.viewModel removeObserver:self forKeyPath:[self.viewModel observingKeyPath]];
&#125;


#pragma mark - UITableViewProtocol
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
&#123;
    <span class="hljs-keyword">return</span> [self.viewModel numberOfRowsInSection:section];
&#125;

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
&#123;
    UITableViewCell * cell = [tableView dequeueReusableCellWithIdentifier:@<span class="hljs-string">"cellIdf"</span>];
    <span class="hljs-keyword">if</span> (!cell) &#123;
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@<span class="hljs-string">"cellIdf"</span>];
    &#125;

    cell.textLabel.text = [self.viewModel cellTitleAtIndexPath:indexPath];
    cell.detailTextLabel.text = [self.viewModel cellDateAtIndexPath:indexPath];
    NSURL * imageUrl = [self.viewModel cellImageUrlAtIndexPath:indexPath];

    dispatch_async(dispatch_get_global_queue(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>), ^&#123;


        NSData * imageData = [NSData dataWithContentsOfURL:imageUrl];
        UIImage * image = [UIImage imageWithData:imageData];

        dispatch_async(dispatch_get_main_queue(), ^&#123;
            cell.imageView.image = image;
        &#125;);

    &#125;);

    <span class="hljs-keyword">return</span> cell;
&#125;



#pragma mark - callback
- (<span class="hljs-keyword">void</span>)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(<span class="hljs-keyword">void</span> *)context
&#123;
    [self.tableView reloadData];
&#125;

#pragma mark - getter
- (UITableView *)tableView
&#123;
    <span class="hljs-keyword">if</span> (!_tableView) &#123;
        _tableView = [[UITableView alloc] initWithFrame:self.view.bounds style:UITableViewStylePlain];
        _tableView.dataSource = self;
        _tableView.delegate = self;
        _tableView.tableFooterView = [[UIView alloc] init];

    &#125;
    <span class="hljs-keyword">return</span> _tableView;
&#125;

- (DHNewsViewModel *)viewModel
&#123;
    <span class="hljs-keyword">if</span> (!_viewModel) &#123;
        _viewModel = [[DHNewsViewModel alloc] init];
    &#125;
    <span class="hljs-keyword">return</span> _viewModel;
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">ViewModel的完整代码</h2>
<p>头文件：</p>
<pre><code class="hljs language-js copyable" lang="js">#<span class="hljs-keyword">import</span> <Foundation/Foundation.h>

@interface DHNewsViewModel : NSObject

- (<span class="hljs-keyword">void</span>)getData;

- (NSString *)observingKeyPath;


- (NSInteger)numberOfRowsInSection:(NSInteger)section;

- (NSString *)cellTitleAtIndexPath:(NSIndexPath *)indexPath;
- (NSString *)cellDateAtIndexPath:(NSIndexPath *)indexPath;
- (NSURL *)cellImageUrlAtIndexPath:(NSIndexPath *)indexPath;

- (NSString *)cellContentAtIndexPath:(NSIndexPath *)indexPath;


@end

<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现文件</p>
<pre><code class="hljs language-js copyable" lang="js">#<span class="hljs-keyword">import</span> <span class="hljs-string">"DHNewsViewModel.h"</span>
#<span class="hljs-keyword">import</span> <span class="hljs-string">"DHNewsModel.h"</span>
#<span class="hljs-keyword">import</span> <UIKit/UIKit.h>

@interface DHNewsViewModel ()

@property (nonatomic, strong) DHNewsModel * model;

- (NSDictionary *)_cellDicAtIndexPath:(NSIndexPath *)indexPath;

@end

@implementation DHNewsViewModel

#pragma mark - private methods
- (NSDictionary *)_cellDicAtIndexPath:(NSIndexPath *)indexPath
&#123;
    <span class="hljs-keyword">return</span> self.model.dataList[indexPath.row];
&#125;

#pragma mark - interface methods
- (<span class="hljs-keyword">void</span>)getData
&#123;
    [self.model getData];
&#125;

- (NSString *)observingKeyPath
&#123;
    <span class="hljs-keyword">return</span> @<span class="hljs-string">"model.dataList"</span>;
&#125;


- (NSInteger)numberOfRowsInSection:(NSInteger)section
&#123;
    <span class="hljs-keyword">return</span> [self.model.dataList count];
&#125;

- (NSString *)cellTitleAtIndexPath:(NSIndexPath *)indexPath
&#123;
    NSDictionary * cellDic = [self _cellDicAtIndexPath:indexPath];
    <span class="hljs-keyword">return</span> cellDic[@<span class="hljs-string">"title"</span>];
&#125;

- (NSString *)cellDateAtIndexPath:(NSIndexPath *)indexPath
&#123;
    NSDictionary * cellDic = [self _cellDicAtIndexPath:indexPath];
    <span class="hljs-keyword">return</span> cellDic[@<span class="hljs-string">"date"</span>];
&#125;
- (NSURL *)cellImageUrlAtIndexPath:(NSIndexPath *)indexPath
&#123;
    NSDictionary * cellDic = [self _cellDicAtIndexPath:indexPath];
    <span class="hljs-keyword">return</span> [NSURL URLWithString:cellDic[@<span class="hljs-string">"image"</span>]];
&#125;

- (NSString *)cellContentAtIndexPath:(NSIndexPath *)indexPath
&#123;
    NSDictionary * cellDic = [self _cellDicAtIndexPath:indexPath];
    <span class="hljs-keyword">return</span> cellDic[@<span class="hljs-string">"content"</span>];
&#125;

#pragma mark - getter
- (DHNewsModel *)model
&#123;
    <span class="hljs-keyword">if</span> (!_model) &#123;
        _model = [[DHNewsModel alloc] init];
    &#125;
    <span class="hljs-keyword">return</span> _model;
&#125;

@end
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            