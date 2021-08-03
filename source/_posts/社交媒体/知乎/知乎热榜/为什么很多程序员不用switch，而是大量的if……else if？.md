
---
title: '为什么很多程序员不用switch，而是大量的if……else if？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=6171'
author: 知乎
comments: false
date: Tue, 03 Aug 2021 08:03:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=6171'
---

<div>   
古明地觉的回答<br><br><p>不会吧还有人用if else和switch case？三目运算符？</p><p>不会吧？ 不会吧？大佬都是全都不用的！以JAVA为例</p><p>条件判断语句的四种写法，茴字的四种写法大家不会不知道吧</p><p><b>1.正常人写法：</b></p><div class="highlight"><pre><code class="language-text"><span>    private static String MAN = "man";
    private static String WOMAN = "woman";
    @Data
    static class Person&#123;
        private String gender;
        private String name;
    &#125;  
    public static void main(String[] args) &#123;
        Person p = new Person();
        p.setGender(MAN);
        p.setName("张三");

        if(Objects.equals(p.getGender(),MAN))&#123;
            System.out.println(p.getName() + "应该去男厕所");
        &#125;

        if(Objects.equals(p.getGender(),WOMAN))&#123;
            System.out.println(p.getName() + "应该去女厕所");
        &#125;

    &#125;
//输出 ：张三应该去男厕所
</span></code></pre></div><p><b>2.Lambda策略模式写法：</b></p><p>某些大公司P6级别以上（年薪30w-50w）标准写法，写if else是要被骂的</p><div class="highlight"><pre><code class="language-text"><span>    private static Map<String, Consumer<String>> FUNC_MAP = new ConcurrentHashMap<>();
    private static String MAN = "man";
    private static String WOMAN = "woman";
    static &#123;
        FUNC_MAP.put(MAN,person ->&#123;System.out.println(person + "应该去男厕所");&#125;);
        FUNC_MAP.put(WOMAN,person ->&#123;System.out.println(person + "应该去女厕所");&#125;);
    &#125;
    @Data
    static class Person&#123;
        private String gender;
        private String name;
    &#125;
    public static void main(String[] args) &#123;
        Person p = new Person();
        p.setGender(MAN);
        p.setName("张三");
        Person p2 = new Person();
        p2.setGender(WOMAN);
        p2.setName("张三他老婆");

        FUNC_MAP.get(p.getGender()).accept(p.name);
        FUNC_MAP.get(p2.getGender()).accept(p2.name);

    &#125;


//输出：
//张三应该去男厕所
//张三他老婆应该去女厕所
</span></code></pre></div><p><b>3.DDD领域驱动设计思想+策略模式写法：</b></p><p>某些大公司P7级别以上（年薪40w-70w）标准写法（笑）</p><div class="highlight"><pre><code class="language-text"><span>    private static String MAN = "man";
    private static String WOMAN = "woman";
    @Data
    static class Person&#123;
        private String gender;
        private String name;

        private static Map<String, Consumer<String>> FUNC_MAP = new ConcurrentHashMap<>();
        static &#123;
            FUNC_MAP.put(MAN,person ->&#123;System.out.println(person + "应该去男厕所");&#125;);
            FUNC_MAP.put(WOMAN,person ->&#123;System.out.println(person + "应该去女厕所");&#125;);
        &#125;
        public void goToWC()&#123;
            FUNC_MAP.get(gender).accept(name);
        &#125;
    &#125;

    static class PersonFactory&#123;
        public static Person initPerson(String name ,String gender)&#123;
            Person p = new Person();
            p.setName(name);
            p.setGender(gender);
            return p;
        &#125;
    &#125;
    public static void main(String[] args) &#123;
        Person p = PersonFactory.initPerson("张三",MAN);
        Person p2 = PersonFactory.initPerson("张三他老婆",WOMAN);
        p.goToWC();
        p2.goToWC();
    &#125;


//输出：
//张三应该去男厕所
//张三他老婆应该去女厕所
</span></code></pre></div><p>某些奇葩公司就是喜欢这种语法，看起来够装逼，实际上效率并没有高多少，可读性差了很多，而且Debug比较麻烦</p><p><b>4.Actor模型+领域驱动设计+策略模式+事件响应式架构</b></p><p>真正的P8年薪百万架构师级写法，逼王才这么写代码，装逼的极限，内卷的奥义</p><p>Maven依赖：</p><p>依赖Akka框架 Actor模型，懂得都懂，大数据分布式计算Spark框架RDD依赖的框架，很复杂，源码是Scala语言，逼王必学。也可以Scala做架构，Java做上层，有兴趣可以了解一下，反正管他是什么，够牛逼就完了。哎，就是得有牌面。if else什么的太low，应届毕业生水平才写if else（魔怔领导原话）。</p><div class="highlight"><pre><code class="language-text"><span>       <dependency>
            <groupId>com.typesafe.akka</groupId>
            <artifactId>akka-actor_2.12</artifactId>
            <version>2.5.2</version>
        </dependency>
</span></code></pre></div><p>代码</p><div class="highlight"><pre><code class="language-text"><span>    private static String MAN = "man";
    private static String WOMAN = "woman";
    private static String WC_EVENT= "想上厕所";
    @Data
    static class Person extends UntypedActor &#123;
        private String gender;
        private String name;

        public static Props props(final String name,final String gender) &#123;
            return Props.create(new Creator<Person>() &#123;
                private static final long serialVersionUID = 1L;
                @Override
                public Person create() throws Exception &#123;
                    Person p = new Person();
                    p.setGender(gender);
                    p.setName(name);
                    return p;
                &#125;
            &#125;);
        &#125;
        @Override
        public void onReceive(Object message) throws Throwable &#123;
            Pair<String,ActorRef> m = (Pair<String,ActorRef>)message;
            System.out.println(name + m.getLeft());
            m.getRight().tell(this, ActorRef.noSender());

        &#125;
    &#125;

    @Data
    static class Toilet extends UntypedActor &#123;
        private static Map<String, Consumer<String>> FUNC_MAP = new ConcurrentHashMap<>();
        static &#123;
            FUNC_MAP.put(MAN,person ->&#123;System.out.println(person + "应该去男厕所");&#125;);
            FUNC_MAP.put(WOMAN,person ->&#123;System.out.println(person + "应该去女厕所");&#125;);
        &#125;

        public void wc(Person p )&#123;
            FUNC_MAP.get(p.getGender()).accept(p.getName());
        &#125;

        public static Props props() &#123;
            return Props.create(Toilet.class);
        &#125;

        @Override
        public void onReceive(Object message) throws Throwable &#123;
            Person p = (Person) message;
            wc(p);
        &#125;
    &#125;

    public static void main(String[] args) &#123;
        ActorSystem actorSystem = ActorSystem.create();
        ActorRef person = actorSystem.actorOf(Person.props("张三",MAN), "ZhangSan");
        ActorRef toilet = actorSystem.actorOf(Toilet.props(), "Toilet");
        Pair<String,ActorRef> message = Pair.of(WC_EVENT,toilet);
        person.tell(message,ActorRef.noSender());
    &#125;
//输出
//张三想上厕所
//张三应该去男厕所
</span></code></pre></div><p><br></p><p>总结，代码还是正常写就得了，能实现业务不出bug好维护的就是好代码，切勿为了装逼使用各种奇技淫巧，if else没啥不好的。</p>  
</div>
            