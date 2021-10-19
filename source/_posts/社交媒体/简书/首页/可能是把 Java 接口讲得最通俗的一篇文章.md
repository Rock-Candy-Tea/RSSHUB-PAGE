
---
title: '可能是把 Java 接口讲得最通俗的一篇文章'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1179389-348cd3720181526d.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1179389-348cd3720181526d.png'
---

<div>   
<p>读者春夏秋冬在<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FyES5bPg6wbCYuBciZhPYaQ" target="_blank">抽象类</a>的那篇文章中留言，“二哥，面试官最喜欢问的一个问题就是，‘兄弟，说说抽象类和接口之间的区别？’，啥时候讲讲接口呗！”</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="240" data-height="240"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-348cd3720181526d.png" data-original-width="240" data-original-height="240" data-original-format="image/png" data-original-filesize="49219" src="https://upload-images.jianshu.io/upload_images/1179389-348cd3720181526d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>对于面向对象编程来说，抽象是一个极具魅力的特征。如果一个程序员的抽象思维很差，那他在编程中就会遇到很多困难，无法把业务变成具体的代码。在 Java 中，可以通过两种形式来达到抽象的目的，一种是抽象类，另外一种就是接口。</p>
<p>如果你现在就想知道抽象类与接口之间的区别，我可以提前给你说一个：</p>
<ul>
<li>一个类只能继承一个抽象类，但却可以实现多个接口。</li>
</ul>
<p>当然了，在没有搞清楚接口到底是什么，它可以做什么之前，这个区别理解起来会有点难度。</p>
<h3>01、接口是什么</h3>
<p>接口是通过 interface 关键字定义的，它可以包含一些常量和方法，来看下面这个示例。</p>
<pre><code class="java">public interface Electronic &#123;
    // 常量
    String LED = "LED";

    // 抽象方法
    int getElectricityUse();

    // 静态方法
    static boolean isEnergyEfficient(String electtronicType) &#123;
        return electtronicType.equals(LED);
    &#125;

    // 默认方法
    default void printDescription() &#123;
        System.out.println("电子");
    &#125;
&#125;
</code></pre>
<p>1）接口中定义的变量会在编译的时候自动加上 <code>public static final</code> 修饰符，也就是说 LED 变量其实是一个常量。</p>
<p>Java 官方文档上有这样的声明：</p>
<blockquote>
<p>Every field declaration in the body of an interface is implicitly public, static, and final.</p>
</blockquote>
<p>换句话说，接口可以用来作为常量类使用，还能省略掉 <code>public static final</code>，看似不错的一种选择，对吧？</p>
<p>不过，这种选择并不可取。因为接口的本意是对方法进行抽象，而常量接口会对子类中的变量造成命名空间上的“污染”。</p>
<p>2）没有使用 <code>private</code>、<code>default</code> 或者 <code>static</code> 关键字修饰的方法是隐式抽象的，在编译的时候会自动加上 <code>public abstract</code> 修饰符。也就是说 <code>getElectricityUse()</code> 其实是一个抽象方法，没有方法体——这是定义接口的本意。</p>
<p>3）从 Java 8 开始，接口中允许有静态方法，比如说 <code>isEnergyEfficient()</code> 方法。</p>
<p>静态方法无法由（实现了该接口的）类的对象调用，它只能通过接口的名字来调用，比如说 <code>Electronic.isEnergyEfficient("LED")</code>。</p>
<p>接口中定义静态方法的目的是为了提供一种简单的机制，使我们不必创建对象就能调用方法，从而提高接口的竞争力。</p>
<p>4）接口中允许定义 <code>default</code> 方法也是从 Java 8 开始的，比如说 <code>printDescription()</code>，它始终由一个代码块组成，为实现该接口而不覆盖该方法的类提供默认实现，也就是说，无法直接使用一个“;”号来结束默认方法——编译器会报错的。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="430" data-height="134"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-68bde3d324ab5d44.png" data-original-width="430" data-original-height="134" data-original-format="image/png" data-original-filesize="9316" src="https://upload-images.jianshu.io/upload_images/1179389-68bde3d324ab5d44.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>允许在接口中定义默认方法的理由是很充分的，因为一个接口可能有多个实现类，这些类就必须实现接口中定义的抽象类，否则编译器就会报错。假如我们需要在所有的实现类中追加某个具体的方法，在没有 <code>default</code> 方法的帮助下，我们就必须挨个对实现类进行修改。</p>
<p>来看一下 Electronic 接口反编译后的字节码吧，你会发现，接口中定义的所有变量或者方法，都会自动添加上 <code>public</code> 关键字——假如你想知道编译器在背后都默默做了哪些辅助，记住反编译字节码就对了。</p>
<pre><code class="java">public interface Electronic
&#123;

    public abstract int getElectricityUse();

    public static boolean isEnergyEfficient(String electtronicType)
    &#123;
        return electtronicType.equals("LED");
    &#125;

    public void printDescription()
    &#123;
        System.out.println("\u7535\u5B50");
    &#125;

    public static final String LED = "LED";
&#125;
</code></pre>
<p>有些读者可能会问，“二哥，为什么我反编译后的字节码和你的不一样，你用了什么反编译工具？”其实没有什么秘密，微信搜「沉默王二」回复关键字「<strong>JAD</strong>」就可以免费获取了，超级好用。</p>
<h3>02、定义接口的注意事项</h3>
<p>由之前的例子我们就可以得出下面这些结论：</p>
<ul>
<li>接口中允许定义变量</li>
<li>接口中允许定义抽象方法</li>
<li>接口中允许定义静态方法（Java 8 之后）</li>
<li>接口中允许定义默认方法（Java 8 之后）</li>
</ul>
<p>除此之外，我们还应该知道：</p>
<p>1）接口不允许直接实例化。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="468" data-height="102"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-4a3a762eae494531.png" data-original-width="468" data-original-height="102" data-original-format="image/png" data-original-filesize="7147" src="https://upload-images.jianshu.io/upload_images/1179389-4a3a762eae494531.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>需要定义一个类去实现接口，然后再实例化。</p>
<pre><code class="java">public class Computer implements Electronic &#123;

    public static void main(String[] args) &#123;
        new Computer();
    &#125;

    @Override
    public int getElectricityUse() &#123;
        return 0;
    &#125;
&#125;
</code></pre>
<p>2）接口可以是空的，既不定义变量，也不定义方法。</p>
<pre><code class="java">public interface Serializable &#123;
&#125;
</code></pre>
<p>Serializable 是最典型的一个空的接口，我之前分享过一篇文章《Java Serializable：明明就一个空的接口嘛》，感兴趣的读者可以去我的个人博客看一看，你就明白了空接口的意义。</p>
<blockquote>
<p><a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.itwanger.com%2Fjava%2F2019%2F11%2F14%2Fjava-serializable.html" target="_blank">http://www.itwanger.com/java/2019/11/14/java-serializable.html</a></p>
</blockquote>
<p>3）不要在定义接口的时候使用 final 关键字，否则会报编译错误，因为接口就是为了让子类实现的，而 final 阻止了这种行为。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="374" data-height="59"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-25bbbe251b2d4e77.png" data-original-width="374" data-original-height="59" data-original-format="image/png" data-original-filesize="6023" src="https://upload-images.jianshu.io/upload_images/1179389-25bbbe251b2d4e77.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>4）接口的抽象方法不能是 private、protected 或者 final。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="390" data-height="94"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-c385bee5b112fde3.png" data-original-width="390" data-original-height="94" data-original-format="image/png" data-original-filesize="7371" src="https://upload-images.jianshu.io/upload_images/1179389-c385bee5b112fde3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="397" data-height="100"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-71a24aff16c3f3c4.png" data-original-width="397" data-original-height="100" data-original-format="image/png" data-original-filesize="7669" src="https://upload-images.jianshu.io/upload_images/1179389-71a24aff16c3f3c4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="398" data-height="100"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-3d2f21dcc78e39f8.png" data-original-width="398" data-original-height="100" data-original-format="image/png" data-original-filesize="7350" src="https://upload-images.jianshu.io/upload_images/1179389-3d2f21dcc78e39f8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>5）接口的变量是隐式 <code>public static final</code>，所以其值无法改变。</p>
<h3>03、接口可以做什么</h3>
<p>1）使某些实现类具有我们想要的功能，比如说，实现了 Cloneable 接口的类具有拷贝的功能，实现了 Comparable 或者 Comparator 的类具有比较功能。</p>
<p>Cloneable 和 Serializable 一样，都属于标记型接口，它们内部都是空的。实现了 Cloneable 接口的类可以使用 <code>Object.clone()</code> 方法，否则会抛出 CloneNotSupportedException。</p>
<pre><code class="java">public class CloneableTest implements Cloneable &#123;
    @Override
    protected Object clone() throws CloneNotSupportedException &#123;
        return super.clone();
    &#125;

    public static void main(String[] args) throws CloneNotSupportedException &#123;
        CloneableTest c1 = new CloneableTest();
        CloneableTest c2 = (CloneableTest) c1.clone();
    &#125;
&#125;
</code></pre>
<p>运行后没有报错。现在把 <code>implements Cloneable</code> 去掉。</p>
<pre><code class="java">public class CloneableTest &#123;
    @Override
    protected Object clone() throws CloneNotSupportedException &#123;
        return super.clone();
    &#125;

    public static void main(String[] args) throws CloneNotSupportedException &#123;
        CloneableTest c1 = new CloneableTest();
        CloneableTest c2 = (CloneableTest) c1.clone();

    &#125;
&#125;
</code></pre>
<p>运行后抛出 CloneNotSupportedException：</p>
<pre><code>Exception in thread "main" java.lang.CloneNotSupportedException: com.cmower.baeldung.interface1.CloneableTest
    at java.base/java.lang.Object.clone(Native Method)
    at com.cmower.baeldung.interface1.CloneableTest.clone(CloneableTest.java:6)
    at com.cmower.baeldung.interface1.CloneableTest.main(CloneableTest.java:11)
</code></pre>
<p>至于 Comparable 和 Comparator 的用法，感兴趣的读者可以参照我之前写的另外一篇文章《来吧，一文彻底搞懂Java中的Comparable和Comparator》。</p>
<blockquote>
<p><a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.itwanger.com%2Fjava%2F2020%2F01%2F04%2Fjava-comparable-comparator.html" target="_blank">http://www.itwanger.com/java/2020/01/04/java-comparable-comparator.html</a></p>
</blockquote>
<p>2）Java 原则上只支持单一继承，但通过接口可以实现多重继承的目的。</p>
<p>可能有些读者会问，“二哥，为什么 Java 只支持单一继承？”简单来解释一下。</p>
<p>如果有两个类共同继承（extends）一个有特定方法的父类，那么该方法会被两个子类重写。然后，如果你决定同时继承这两个子类，那么在你调用该重写方法时，编译器不能识别你要调用哪个子类的方法。这也正是著名的菱形问题，见下图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="570" data-height="335"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-da9057082e43aad1.png" data-original-width="570" data-original-height="335" data-original-format="image/png" data-original-filesize="5457" src="https://upload-images.jianshu.io/upload_images/1179389-da9057082e43aad1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>ClassC 同时继承了 ClassA 和 ClassB，ClassC 的对象在调用 ClassA 和 ClassB 中重载的方法时，就不知道该调用 ClassA 的方法，还是 ClassB 的方法。</p>
<p>接口没有这方面的困扰。来定义两个接口，Fly 会飞，Run 会跑。</p>
<pre><code class="java">public interface Fly &#123;
    void fly();
&#125;
public interface Run &#123;
    void run();
&#125;
</code></pre>
<p>然后让一个类同时实现这两个接口。</p>
<pre><code class="java">public class Pig implements Fly,Run&#123;
    @Override
    public void fly() &#123;
        System.out.println("会飞的猪");
    &#125;

    @Override
    public void run() &#123;
        System.out.println("会跑的猪");
    &#125;
&#125;
</code></pre>
<p>这就在某种形式上达到了多重继承的目的：现实世界里，猪的确只会跑，但在雷军的眼里，站在风口的猪就会飞，这就需要赋予这只猪更多的能力，通过抽象类是无法实现的，只能通过接口。</p>
<p>3）实现多态。</p>
<p>什么是多态呢？通俗的理解，就是同一个事件发生在不同的对象上会产生不同的结果，鼠标左键点击窗口上的 X 号可以关闭窗口，点击超链接却可以打开新的网页。</p>
<p>多态可以通过继承（<code>extends</code>）的关系实现，也可以通过接口的形式实现。来看这样一个例子。</p>
<p>Shape 是表示一个形状。</p>
<pre><code class="java">public interface Shape &#123;
    String name();
&#125;
</code></pre>
<p>圆是一个形状。</p>
<pre><code class="java">public class Circle implements Shape &#123;
    @Override
    public String name() &#123;
        return "圆";
    &#125;
&#125;
</code></pre>
<p>正方形也是一个形状。</p>
<pre><code class="java">public class Square implements Shape &#123;
    @Override
    public String name() &#123;
        return "正方形";
    &#125;
&#125;
</code></pre>
<p>然后来看测试类。</p>
<pre><code class="java">List<Shape> shapes = new ArrayList<>();
Shape circleShape = new Circle();
Shape squareShape = new Square();

shapes.add(circleShape);
shapes.add(squareShape);

for (Shape shape : shapes) &#123;
    System.out.println(shape.name());
&#125;
</code></pre>
<p>多态的存在 3 个前提：</p>
<p>1、要有继承关系，Circle 和 Square 都实现了 Shape 接口<br>
2、子类要重写父类的方法，Circle 和 Square 都重写了 <code>name()</code> 方法<br>
3、父类引用指向子类对象，circleShape 和 squareShape 的类型都为 Shape，但前者指向的是 Circle 对象，后者指向的是 Square 对象。</p>
<p>然后，我们来看一下测试结果：</p>
<pre><code>圆
正方形
</code></pre>
<p>也就意味着，尽管在 for 循环中，shape 的类型都为 Shape，但在调用 <code>name()</code> 方法的时候，它知道 Circle 对象应该调用 Circle 类的 <code>name()</code> 方法，Square 对象应该调用 Square 类的 <code>name()</code> 方法。</p>
<h3>04、接口与抽象类的区别</h3>
<p>好了，关于接口的一切，你应该都搞清楚了。现在回到读者春夏秋冬的那条留言，“兄弟，说说抽象类和接口之间的区别？”</p>
<p>1）语法层面上</p>
<ul>
<li>接口中不能有 public 和 protected 修饰的方法，抽象类中可以有。</li>
<li>接口中的变量只能是隐式的常量，抽象类中可以有任意类型的变量。</li>
<li>一个类只能继承一个抽象类，但却可以实现多个接口。</li>
</ul>
<p>2）设计层面上</p>
<p>抽象类是对类的一种抽象，继承抽象类的类和抽象类本身是一种 <code>is-a</code> 的关系。</p>
<p>接口是对类的某种行为的一种抽象，接口和类之间并没有很强的关联关系，所有的类都可以实现 <code>Serializable</code> 接口，从而具有序列化的功能。</p>
<p>就这么多吧，能说道这份上，我相信面试官就不会为难你了。</p>
<p>如果觉得文章对你有点帮助，请微信搜索「 <strong>沉默王二</strong> 」第一时间阅读，回复「<strong>并发</strong>」更有一份阿里大牛重写的 Java 并发编程实战，从此再也不用担心面试官在这方面的刁难了。</p>
<blockquote>
<p>本文已收录 GitHub，<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqinggee%2Fitwanger.github.io" target="_blank"><strong>传送门~</strong></a> ，里面更有大厂面试完整考点，欢迎 Star。</p>
</blockquote>
<p>我是沉默王二，一枚有颜值却靠才华苟且的程序员。<strong>关注即可提升学习效率，别忘了三连啊，点赞、收藏、留言，我不挑，嘻嘻</strong>。</p>
  
</div>
            