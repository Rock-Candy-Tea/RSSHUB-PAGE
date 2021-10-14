
---
title: '面试官：兄弟，说说Java的static关键字吧'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1179389-05c56c080a660ad3.gif'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1179389-05c56c080a660ad3.gif'
---

<div>   
<p>读者乙在上一篇<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FMIX4srqeg7STzphhR6Gp5g" target="_blank">我去</a>系列文章里留言说，“我盲猜下一篇标题是，‘我去，你竟然不知道 static 关键字’”。我只能说乙猜对了一半，像我这么有才华的博主，怎么可能被读者猜中了心思呢，必须搞点不一样的啊，所以本篇文章的标题你看到了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="220" data-height="162"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-05c56c080a660ad3.gif" data-original-width="220" data-original-height="162" data-original-format="image/gif" data-original-filesize="415194" src="https://upload-images.jianshu.io/upload_images/1179389-05c56c080a660ad3.gif" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>七年前，我从美女很多的苏州回到美女也不少的洛阳，抱着一幅“从二线城市退居三线城市”的心态，投了不少简历，也“约谈”了不少面试官，但仅有两三个令我感到满意。其中有一位叫老马，至今还活在我的微信通讯录里。他当时扔了一个面试题把我砸懵了：“<strong>兄弟，说说 Java 的 static 关键字吧。</strong>”</p>
<p>我那时候二十三岁，正值青春年华，自认为所有的面试题都能对答如流，结果没想到啊，被“刁难”了——原来洛阳这块互联网的荒漠也有技术专家啊。现在回想起来，脸上不自觉地泛起了羞愧的红晕：主要是自己当时太菜了。</p>
<p>不管怎么说，经过多年的努力，我现在的技术功底已经非常扎实了，有能力写篇文章剖析一下 Java 的 static 关键字了——只要能给初学者一些参考，我就觉得非常满足。</p>
<p>先来个提纲挈领（唉呀妈呀，成语区博主上线了）吧：</p>
<blockquote>
<p>static 关键字可用于变量、方法、代码块和内部类，表示某个特定的成员只属于某个类本身，而不是该类的某个对象。</p>
</blockquote>
<h3>01、静态变量</h3>
<p>静态变量也叫类变量，它属于一个类，而不是这个类的对象。</p>
<pre><code class="java">public class Writer &#123;
    private String name;
    private int age;
    public static int countOfWriters;

    public Writer(String name, int age) &#123;
        this.name = name;
        this.age = age;
        countOfWriters++;
    &#125;

    public String getName() &#123;
        return name;
    &#125;

    public void setName(String name) &#123;
        this.name = name;
    &#125;

    public int getAge() &#123;
        return age;
    &#125;

    public void setAge(int age) &#123;
        this.age = age;
    &#125;
&#125;
</code></pre>
<p>其中，countOfWriters 被称为静态变量，它有别于 name 和 age 这两个成员变量，因为它前面多了一个修饰符 <code>static</code>。</p>
<p>这意味着无论这个类被初始化多少次，静态变量的值都会在所有类的对象中共享。</p>
<pre><code class="java">Writer w1 = new Writer("沉默王二",18);
Writer w2 = new Writer("沉默王三",16);

System.out.println(Writer.countOfWriters);
</code></pre>
<p>按照上面的逻辑，你应该能推理得出，countOfWriters 的值此时应该为 2 而不是 1。从内存的角度来看，静态变量将会存储在 Java 虚拟机中一个名叫“Metaspace”（元空间，Java 8 之后）的特定池中。</p>
<p>静态变量和成员变量有着很大的不同，成员变量的值属于某个对象，不同的对象之间，值是不共享的；但静态变量不是的，它可以用来统计对象的数量，因为它是共享的。就像上面例子中的 countOfWriters，创建一个对象的时候，它的值为 1，创建两个对象的时候，它的值就为 2。</p>
<p>简单小结一下：</p>
<p>1）由于静态变量属于一个类，所以不要通过对象引用来访问，而应该直接通过类名来访问；</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="554" data-height="120"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-0f87e19ac7874abb.png" data-original-width="554" data-original-height="120" data-original-format="image/png" data-original-filesize="14674" src="https://upload-images.jianshu.io/upload_images/1179389-0f87e19ac7874abb.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>2）不需要初始化类就可以访问静态变量。</p>
<pre><code class="java">public class WriterDemo &#123;
    public static void main(String[] args) &#123;
        System.out.println(Writer.countOfWriters); // 输出 0
    &#125;
&#125;
</code></pre>
<h3>02、静态方法</h3>
<p>静态方法也叫类方法，它和静态变量类似，属于一个类，而不是这个类的对象。</p>
<pre><code class="java">public static void setCountOfWriters(int countOfWriters) &#123;
    Writer.countOfWriters = countOfWriters;
&#125;
</code></pre>
<p><code>setCountOfWriters()</code> 就是一个静态方法，它由 static 关键字修饰。</p>
<p>如果你用过 java.lang.Math 类或者 Apache 的一些工具类（比如说 StringUtils）的话，对静态方法一定不会感动陌生。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="270" data-height="256"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-160ef699f1300577.png" data-original-width="270" data-original-height="256" data-original-format="image/png" data-original-filesize="12034" src="https://upload-images.jianshu.io/upload_images/1179389-160ef699f1300577.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>Math 类的几乎所有方法都是静态的，可以直接通过类名来调用，不需要创建类的对象。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="318" data-height="277"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-fbf58be4bd12b2d7.png" data-original-width="318" data-original-height="277" data-original-format="image/png" data-original-filesize="18422" src="https://upload-images.jianshu.io/upload_images/1179389-fbf58be4bd12b2d7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>简单小结一下：</p>
<p>1）Java 中的静态方法在编译时解析，因为静态方法不能被重写（方法重写发生在运行时阶段，为了多态）。</p>
<p>2）抽象方法不能是静态的。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="346" data-height="54"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-582bfd27669c3b40.png" data-original-width="346" data-original-height="54" data-original-format="image/png" data-original-filesize="5939" src="https://upload-images.jianshu.io/upload_images/1179389-582bfd27669c3b40.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>3）静态方法不能使用 this 和 super 关键字。</p>
<p>4）成员方法可以直接访问其他成员方法和成员变量。</p>
<p>5）成员方法也可以直接方法静态方法和静态变量。</p>
<p>6）静态方法可以访问所有其他静态方法和静态变量。</p>
<p>7）静态方法无法直接访问成员方法和成员变量。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="326" data-height="165"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-853cb7426a721068.png" data-original-width="326" data-original-height="165" data-original-format="image/png" data-original-filesize="14201" src="https://upload-images.jianshu.io/upload_images/1179389-853cb7426a721068.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>03、静态代码块</h3>
<p>静态代码块可以用来初始化静态变量，尽管静态方法也可以在声明的时候直接初始化，但有些时候，我们需要多行代码来完成初始化。</p>
<pre><code class="java">public class StaticBlockDemo &#123;
    public static List<String> writes = new ArrayList<>();

    static &#123;
        writes.add("沉默王二");
        writes.add("沉默王三");
        writes.add("沉默王四");

        System.out.println("第一块");
    &#125;

    static &#123;
        writes.add("沉默王五");
        writes.add("沉默王六");

        System.out.println("第二块");
    &#125;
&#125;
</code></pre>
<p>writes 是一个静态的 ArrayList，所以不太可能在声明的时候完成初始化，因此需要在静态代码块中完成初始化。</p>
<p>简单小结一下：</p>
<p>1）一个类可以有多个静态代码块。</p>
<p>2）静态代码块的解析和执行顺序和它在类中的位置保持一致。为了验证这个结论，可以在 StaticBlockDemo 类中加入空的 main 方法，执行完的结果如下所示：</p>
<pre><code>第一块
第二块
</code></pre>
<h3>04、静态内部类</h3>
<p>Java 允许我们在一个类中声明一个内部类，它提供了一种令人信服的方式，允许我们只在一个地方使用一些变量，使代码更具有条理性和可读性。</p>
<p>常见的内部类有四种，成员内部类、局部内部类、匿名内部类和静态内部类，限于篇幅原因，前三种不在我们本次文章的讨论范围，以后有机会再细说。</p>
<pre><code class="java">public class Singleton &#123;
    private Singleton() &#123;&#125;

    private static class SingletonHolder &#123;
        public static final Singleton instance = new Singleton();
    &#125;

    public static Singleton getInstance() &#123;
        return SingletonHolder.instance;
    &#125;
&#125;
</code></pre>
<p>以上这段代码是不是特别熟悉，对，这就是创建单例的一种方式，第一次加载 Singleton 类时并不会初始化 instance，只有第一次调用 <code>getInstance()</code> 方法时 Java 虚拟机才开始加载 SingletonHolder 并初始化 instance，这样不仅能确保线程安全也能保证 Singleton 类的唯一性。不过，创建单例更优雅的一种方式是使用枚举。</p>
<p>简单小结一下：</p>
<p>1）静态内部类不能访问外部类的所有成员变量。</p>
<p>2）静态内部类可以访问外部类的所有静态变量，包括私有静态变量。</p>
<p>3）外部类不能声明为 static。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="367" data-height="88"><img data-original-src="//upload-images.jianshu.io/upload_images/1179389-45bd16699801f954.png" data-original-width="367" data-original-height="88" data-original-format="image/png" data-original-filesize="8215" src="https://upload-images.jianshu.io/upload_images/1179389-45bd16699801f954.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>学到了吧？学到就是赚到。</p>
<p>我是沉默王二，一枚有趣的程序员。如果觉得文章对你有点帮助，请微信搜索「 <strong>沉默王二</strong> 」第一时间阅读，回复【<strong>666</strong>】更有我为你精心准备的 500G 高清教学视频（已分门别类）。</p>
<blockquote>
<p>本文 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fqinggee%2Fitwanger.github.io" target="_blank">GitHub</a> 已经收录，有大厂面试完整考点，欢迎 Star。</p>
</blockquote>
<p><strong>原创不易，莫要白票，请你为本文点个赞吧</strong>，这将是我写作更多优质文章的最强动力。</p>
  
</div>
            