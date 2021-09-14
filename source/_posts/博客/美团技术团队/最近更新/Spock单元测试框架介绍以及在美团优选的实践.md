
---
title: 'Spock单元测试框架介绍以及在美团优选的实践'
categories: 
 - 博客
 - 美团技术团队
 - 最近更新
headimg: 'https://p1.meituan.net/travelcube/e6e5b4bcf455e8f0827043dbe6ec04a635315.jpg'
author: 美团技术团队
comments: false
date: Fri, 06 Aug 2021 00:00:00 GMT
thumbnail: 'https://p1.meituan.net/travelcube/e6e5b4bcf455e8f0827043dbe6ec04a635315.jpg'
---

<div>   
<h2 id="1-背景">1. 背景</h2><p>​XML之父Tim Bray最近在博客里有个好玩的说法：“代码不写测试就像上了厕所不洗手……单元测试是对软件未来的一项必不可少的投资。”具体来说，单元测试有哪些收益呢？</p><ul><li>它是最容易保证代码覆盖率达到100%的测试。</li><li>可以⼤幅降低上线时的紧张指数。</li><li>单元测试能更快地发现问题（见下图左）。</li><li>单元测试的性价比最高，因为错误发现的越晚，修复它的成本就越高，而且难度呈指数式增长，所以我们要尽早地进行测试（见下图右）。</li><li>编码人员，一般也是单元测试的主要执行者，是唯一能够做到生产出无缺陷程序的人，其他任何人都无法做到这一点。</li><li>有助于源码的优化，使之更加规范，快速反馈，可以放心进行重构。</li></ul><table><thead><tr><th><img src="https://p1.meituan.net/travelcube/e6e5b4bcf455e8f0827043dbe6ec04a635315.jpg" alt referrerpolicy="no-referrer"></th><th><img src="https://p0.meituan.net/travelcube/4cfde1566b1928486c051bbe8287be2d42010.jpg" alt="pic2" referrerpolicy="no-referrer"></th></tr></thead><tbody><tr><td>这张图来自微软的统计数据：Bug在单元测试阶段被发现，平均耗时3.25小时，如果漏到系统测试阶段，要花费11.5小时。</td><td>这张图，旨在说明两个问题：85%的缺陷都在代码设计阶段产生，而发现Bug的阶段越靠后，耗费成本就越高，指数级别的增高。</td></tr></tbody></table><p>尽管单元测试有如此的收益，但在我们日常的工作中，仍然存在不少项目它们的单元测试要么是不完整要么是缺失的。常见的原因总结如下：代码逻辑过于复杂；写单元测试时耗费的时间较长；任务重、工期紧，或者干脆就不写了。</p><p>基于以上问题，相较于传统的JUnit单元测试，今天为大家推荐一款名为Spock的测试框架。目前，美团优选物流技术团队绝大部分后端服务已经采用了Spock作为测试框架，在开发效率、可读性和维护性方面取得了不错的收益。</p><p>不过网上Spock资料比较简单，甚至包括官网的Demo，无法解决我们项目中复杂业务场景面临的问题，通过深入学习和实践之后，本文会将一些经验分享出来，希望能够帮助大家提高开发测试的效率。</p><h2 id="2-spock是什么-和junit-jmock有什么区别">2. Spock是什么？和JUnit、jMock有什么区别？</h2><p>Spock是一款国外优秀的测试框架，基于<a href="https://en.wikipedia.org/wiki/Behavior-driven_development">BDD</a>（行为驱动开发）思想实现，功能非常强大。Spock结合Groovy动态语言的特点，提供了各种标签，并采用简单、通用、结构化的描述语言，让编写测试代码更加简洁、高效。<a href="https://spockframework.org/">官方的介绍</a>如下：</p><p><img src="https://p0.meituan.net/travelcube/4403846a46a805b9cf304187317da94a52377.png" alt referrerpolicy="no-referrer"></p><blockquote><p>What is it?
Spock is a testing and specification framework for Java and Groovy applications. What makes it stand out from the crowd is its beautiful and highly expressive specification language. Thanks to its JUnit runner, Spock is compatible with most IDEs, build tools, and continuous integration servers. Spock is inspired from JUnit, RSpec, jMock, Mockito, Groovy, Scala, Vulcans, and other fascinating life forms.</p></blockquote><p>Spock是一个Java和Groovy`应用的测试和规范框架。之所以能够在众多测试框架中脱颖而出，是因为它优美而富有表现力的规范语言。Spock的灵感来自JUnit、RSpec、jMock、Mockito、Groovy、Scala、Vulcans。</p><p>简单来讲，Spock主要特点如下：</p><ul><li>让测试代码更规范，内置多种标签来规范单元测试代码的语义，测试代码结构清晰，更具可读性，降低后期维护难度。</li><li>提供多种标签，比如：<code>given</code>、<code>when</code>、<code>then</code>、<code>expect</code>、<code>where</code>、<code>with</code>、<code>thrown</code>……帮助我们应对复杂的测试场景。</li><li>使用Groovy这种动态语言来编写测试代码，可以让我们编写的测试代码更简洁，适合敏捷开发，提高编写单元测试代码的效率。</li><li>遵从<a href="https://en.wikipedia.org/wiki/Behavior-driven_development">BDD</a>（行为驱动开发）模式，有助于提升代码的质量。</li><li>IDE兼容性好，自带Mock功能。</li></ul><h3 id="为什么使用spock-spock和junit-jmock-mockito的区别在哪里">为什么使用Spock？ Spock和JUnit、jMock、Mockito的区别在哪里？</h3><p>总的来说，JUnit、jMock、Mockito都是相对独立的工具，只是针对不同的业务场景提供特定的解决方案。其中JUnit单纯用于测试，并不提供Mock功能。</p><p>我们的服务大部分是分布式微服务架构。服务与服务之间通常都是通过接口的方式进行交互。即使在同一个服务内也会分为多个模块，业务功能需要依赖下游接口的返回数据，才能继续后面的处理流程。这里的下游不限于接口，还包括中间件数据存储比如Squirrel、DB、MCC配置中心等等，所以如果想要测试自己的代码逻辑，就必须把这些依赖项Mock掉。因为如果下游接口不稳定可能会影响我们代码的测试结果，让下游接口返回指定的结果集（事先准备好的数据），这样才能验证我们的代码是否正确，是否符合逻辑结果的预期。</p><p>尽管jMock、Mockito提供了Mock功能，可以把接口等依赖屏蔽掉，但不能对静态方法Mock。虽然PowerMock、jMockit能够提供静态方法的Mock，但它们之间也需要配合（JUnit + Mockito PowerMock）使用，并且语法上比较繁琐。工具多了就会导致不同的人写出的单元测试代码“五花八门”，风格相差较大。</p><p>Spock通过提供规范性的描述，定义多种标签（<code>given</code>、<code>when</code>、<code>then</code>、<code>where</code>等），去描述代码“应该做什么”，“输入条件是什么”，“输出是否符合预期”，从语义层面规范了代码的编写。</p><p>Spock自带Mock功能，使用简单方便（也支持扩展其他Mock框架，比如PowerMock），再加上Groovy动态语言的强大语法，能写出简洁高效的测试代码，同时能方便直观地验证业务代码的行为流转，增强工程师对代码执行逻辑的可控性。</p><h2 id="3-使用spock解决单元测试开发中的痛点">3. 使用Spock解决单元测试开发中的痛点</h2><p>如果在（<code>if/else</code>）分支很多的复杂场景下，编写单元测试代码的成本会变得非常高，正常的业务代码可能只有几十行，但为了测试这个功能覆盖大部分的分支场景，编写的测试代码可能远不止几十行。</p><p>之前有遇到过某个功能上线很久一直都很正常，没有出现过问题，但后来有个调用请求的数据不一样，走到了代码中一个不常用的逻辑分支时，出现了Bug。当时写这段代码的同学也认为只有很小几率才能走到这个分支，尽管当时写了单元测试，但因为时间比较紧张，分支又多，就漏掉了这个分支的测试。</p><p>尽管使用JUnit的@Parametered参数化注解或者DataProvider方式可以解决多数据分支问题，但不够直观，而且如果其中某一次分支测试Case出错了，它的报错信息也不够详尽。</p><p>这就需要一种编写测试用例高效、可读性强、占用工时少、维护成本低的测试框架。首先不能让业务人员排斥编写单元测试，更不能让工程师觉得写单元测试是在浪费时间。而且使用JUnit做测试工作量不算小。据初步统计，采用JUnit的话，它的测试代码行和业务代码行能到3:1。如果采用Spock作为测试框架的话，它的比例可缩减到1:1，能够大大提高编写测试用例的效率。</p><p>下面借用《编程珠玑》中一个计算税金的例子。</p><pre><code class="language-java">public double calc(double income) &#123;
        BigDecimal tax;
        BigDecimal salary = BigDecimal.valueOf(income);
        if (income <= 0) &#123;
            return 0;
        &#125;
        if (income > 0 && income <= 3000) &#123;
            BigDecimal taxLevel = BigDecimal.valueOf(0.03);
            tax = salary.multiply(taxLevel);
        &#125; else if (income > 3000 && income <= 12000) &#123;
            BigDecimal taxLevel = BigDecimal.valueOf(0.1);
            BigDecimal base = BigDecimal.valueOf(210);
            tax = salary.multiply(taxLevel).subtract(base);
        &#125; else if (income > 12000 && income <= 25000) &#123;
            BigDecimal taxLevel = BigDecimal.valueOf(0.2);
            BigDecimal base = BigDecimal.valueOf(1410);
            tax = salary.multiply(taxLevel).subtract(base);
        &#125; else if (income > 25000 && income <= 35000) &#123;
            BigDecimal taxLevel = BigDecimal.valueOf(0.25);
            BigDecimal base = BigDecimal.valueOf(2660);
            tax = salary.multiply(taxLevel).subtract(base);
        &#125; else if (income > 35000 && income <= 55000) &#123;
            BigDecimal taxLevel = BigDecimal.valueOf(0.3);
            BigDecimal base = BigDecimal.valueOf(4410);
            tax = salary.multiply(taxLevel).subtract(base);
        &#125; else if (income > 55000 && income <= 80000) &#123;
            BigDecimal taxLevel = BigDecimal.valueOf(0.35);
            BigDecimal base = BigDecimal.valueOf(7160);
            tax = salary.multiply(taxLevel).subtract(base);
        &#125; else &#123;
            BigDecimal taxLevel = BigDecimal.valueOf(0.45);
            BigDecimal base = BigDecimal.valueOf(15160);
            tax = salary.multiply(taxLevel).subtract(base);
        &#125;
        return tax.setScale(2, BigDecimal.ROUND_HALF_UP).doubleValue();
    &#125;
</code></pre><p>能够看到上面的代码中有大量的<code>if-else</code>语句，Spock提供了where标签，可以让我们通过表格的方式来测试多种分支。</p><pre><code class="language-groovy">@Unroll
def "个税计算,收入:#income, 个税:#result"() &#123;
  expect: "when + then 的组合"
  CalculateTaxUtils.calc(income) == result

  where: "表格方式测试不同的分支逻辑"
  income || result
  -1     || 0
  0      || 0
  2999   || 89.97
  3000   || 90.0
  3001   || 90.1
  11999  || 989.9
  12000  || 990.0
  12001  || 990.2
  24999  || 3589.8
  25000  || 3590.0
  25001  || 3590.25
  34999  || 6089.75
  35000  || 6090.0
  35001  || 6090.3
  54999  || 12089.7
  55000  || 12090
  55001  || 12090.35
  79999  || 20839.65
  80000  || 20840.0
  80001  || 20840.45
&#125;
</code></pre><p><img src="https://p0.meituan.net/travelcube/39c39b05b983ca33b760e060c598ec19255399.png" alt referrerpolicy="no-referrer"></p><p>上图中左边使用Spock写的单元测试代码，语法简洁，表格方式测试覆盖分支场景更加直观，开发效率高，更适合敏捷开发。</p><h3 id="单元测试代码的可读性和后期维护">单元测试代码的可读性和后期维护</h3><p>我们微服务场景很多时候需要依赖其他接口返回的结果，才能验证自己的代码逻辑。Mock工具是必不可少的。但jMock、Mockito的语法比较繁琐，再加上单元测试代码不像业务代码那么直观，又不能完全按照业务流程的思路写单元测试，这就让不少同学对单元测试代码可读性不够重视，最终导致测试代码难以阅读，维护起来更是难上加难。甚至很多同学自己写的单元测试，过几天再看也一样觉得“云里雾里”的。也有改了原来的代码逻辑导致单元测试执行失败的；或者新增了分支逻辑，单元测试没有覆盖到的；最终随着业务的快速迭代单元测试代码越来越难以维护。</p><p>Spock提供多种语义标签，如：<code>given</code>、<code>when</code>、<code>then</code>、<code>expect</code>、<code>where</code>、<code>with</code>、<code>and</code>等，从行为上规范了单元测试代码，每一种标签对应一种语义，让单元测试代码结构具有层次感，功能模块划分更加清晰，也便于后期的维护。</p><p>Spock自带Mock功能，使用上简单方便（Spock也支持扩展第三方Mock框架，比如PowerMock）。我们可以再看一个样例，对于如下的代码逻辑进行单元测试：</p><pre><code class="language-java">public StudentVO getStudentById(int id) &#123;
        List<StudentDTO> students = studentDao.getStudentInfo();
        StudentDTO studentDTO = students.stream().filter(u -> u.getId() == id).findFirst().orElse(null);
        StudentVO studentVO = new StudentVO();
        if (studentDTO == null) &#123;
            return studentVO;
        &#125;
        studentVO.setId(studentDTO.getId());
        studentVO.setName(studentDTO.getName());
        studentVO.setSex(studentDTO.getSex());
        studentVO.setAge(studentDTO.getAge());
        // 邮编
        if ("上海".equals(studentDTO.getProvince())) &#123;
            studentVO.setAbbreviation("沪");
            studentVO.setPostCode("200000");
        &#125;
        if ("北京".equals(studentDTO.getProvince())) &#123;
            studentVO.setAbbreviation("京");
            studentVO.setPostCode("100000");
        &#125;
        return studentVO;
    &#125;
</code></pre><p><img src="https://p0.meituan.net/travelcube/6960c566d92d7208e01c83c22b2a5781496781.png" alt referrerpolicy="no-referrer"></p><p>比较明显，左边的JUnit单元测试代码冗余，缺少结构层次，可读性差，随着后续的迭代，势必会导致代码的堆积，维护成本会变得越来越高。右边的单元测试代码Spock会强制要求使用<code>given</code>、<code>when</code>、<code>then</code>这样的语义标签（至少一个），否则编译不通过，这样就能保证代码更加规范，结构模块化，边界范围清晰，可读性强，便于扩展和维护。而且使用了自然语言描述测试步骤，让非技术人员也能看懂测试代码（<code>given</code>表示输入条件，<code>when</code>触发动作，<code>then</code>验证输出结果）。</p><p>Spock自带的Mock语法也非常简单：<code>dao.getStudentInfo() >> [student1, student2]</code>。</p><p>两个右箭头<code>>></code>表示模拟<code>getStudentInfo</code>接口的返回结果，再加上使用的Groovy语言，可以直接使用<code>[]</code>中括号表示返回的是<code>List</code>类型。</p><h3 id="单元测试不仅仅是为了统计代码覆盖率-更重要的是验证业务代码的健壮性-业务逻辑的严谨性以及设计的合理性">单元测试不仅仅是为了统计代码覆盖率，更重要的是验证业务代码的健壮性、业务逻辑的严谨性以及设计的合理性</h3><p>在项目初期阶段，可能为了追赶进度而没有时间写单元测试，或者这个时期写的单元测试只是为了达到覆盖率的要求（比如为了满足新增代码行或者分支覆盖率统计要求）。</p><p>很多工程师写的单元测试基本都是采用Java这种强类型语言编写，各种底层接口的Mock写起来不仅繁琐而且耗时。这时的单元测试代码可能就写得比较粗糙，有粒度过大的，也有缺少单元测试结果验证的。这样的单元测试对代码的质量帮助不大，更多是为了测试而测试。最后时间没少花，可效果却没有达到。</p><p>针对有效测试用例方面，我们测试基础组件组开发了一些检测工具（作为抓手），比如去扫描大家写的单元测试，检测单元测试的断言有效性等。另外在结果校验方面，Spock表现也是十分优异的。我们可以来看接下来的场景：<code>void</code>方法，没有返回结果，如何写测试这段代码的逻辑是否正确？</p><p>如何确保单元测试代码是否执行到了<code>for</code>循环里面的语句，循环里面的打折计算又是否正确呢？</p><pre><code class="language-java">  public void calculatePrice(OrderVO order)&#123;
        BigDecimal amount = BigDecimal.ZERO;
        for (SkuVO sku : order.getSkus()) &#123;
            Integer skuId = sku.getSkuId();
            BigDecimal skuPrice = sku.getSkuPrice();
            BigDecimal discount = BigDecimal.valueOf(discountDao.getDiscount(skuId));
            BigDecimal price = skuPrice * discount;
            amount = amount.add(price);
        &#125;
        order.setAmount(amount.setScale(2, BigDecimal.ROUND_HALF_DOWN));
    &#125;

</code></pre><p>如果用Spock写的话，就会方便很多，如下图所示：</p><p><img src="https://p0.meituan.net/travelcube/28caf06f8af1824ed8e0745bd939c248133342.png" alt referrerpolicy="no-referrer"></p><p>这里，<code>2 * discountDao.getDiscount(_) >> 0.95 >> 0.8</code> 在<code>for</code>循环中一共调用了2次，第一次返回结果0.95，第二次返回结果0.8，最后再进行验证，类似于JUnit中的Assert断言。</p><p>这样的收益还是比较明显的，不仅提高了单元测试的可控性，而且方便验证业务代码的逻辑正确性和合理性，这也是BDD思想的一种体现。</p><h2 id="4-mock模拟">4. Mock模拟</h2><p>考虑如下场景，代码如下：</p><pre><code class="language-java">@Service
public class StudentService &#123;
    @Autowired
    private StudentDao studentDao;
    public StudentVO getStudentById(int id) &#123;
        List<StudentDTO> students = studentDao.getStudentInfo();
        StudentDTO studentDTO = students.stream().filter(u -> u.getId() == id).findFirst().orElse(null);
        StudentVO studentVO = new StudentVO();
        if (studentDTO == null) &#123;
            return studentVO;
        &#125;
        studentVO.setId(studentDTO.getId());
        studentVO.setName(studentDTO.getName());
        studentVO.setSex(studentDTO.getSex());
        studentVO.setAge(studentDTO.getAge());
        // 邮编
        if ("上海".equals(studentDTO.getProvince())) &#123;
            studentVO.setAbbreviation("沪");
            studentVO.setPostCode("200000");
        &#125;
        if ("北京".equals(studentDTO.getProvince())) &#123;
            studentVO.setAbbreviation("京");
            studentVO.setPostCode("100000");
        &#125;
        return studentVO;
    &#125;
&#125;
</code></pre><p>其中<code>studentDao</code>是使用Spring注入的实例对象，我们只有拿到了返回的<code>students</code>，才能继续下面的逻辑（根据<code>id</code>筛选学生，<code>DTO</code>和<code>VO</code>转换，邮编等）。所以正常的做法是把<code>studentDao</code>的<code>getStudentInfo()</code>方法Mock掉，模拟一个指定的值，因为我们真正关心的是拿到<code>students</code>后自己代码的逻辑，这是需要重点验证的地方。按照上面的思路使用Spock编写的测试代码如下：</p><pre><code class="language-groovy">class StudentServiceSpec extends Specification &#123;
    def studentDao = Mock(StudentDao)
    def tester = new StudentService(studentDao: studentDao)

    def "test getStudentById"() &#123;
        given: "设置请求参数"
        def student1 = new StudentDTO(id: 1, name: "张三", province: "北京")
        def student2 = new StudentDTO(id: 2, name: "李四", province: "上海")

        and: "mock studentDao返回值"
        studentDao.getStudentInfo() >> [student1, student2]

        when: "获取学生信息"
        def response = tester.getStudentById(1)

        then: "结果验证"
        with(response) &#123;
            id == 1
            abbreviation == "京"
            postCode == "100000"
        &#125;
    &#125;
&#125;
</code></pre><p>这里主要讲解Spock的代码（从上往下）。</p><p><code>def studentDao = Mock(StudentDao)</code> 这一行代码使用Spock自带的Mock方法，构造一个<code>studentDao</code>的Mock对象，如果要模拟<code>studentDao</code>方法的返回，只需<code>studentDao.方法名() >> "模拟值"</code>的方式，两个右箭头的方式即可。<code>test getStudentById</code>方法是单元测试的主要方法，可以看到分为4个模块：<code>given</code>、<code>and</code>、<code>when</code>、<code>then</code>，用来区分不同单元测试代码的作用：</p><ul><li><code>given</code>：输入条件（前置参数）。</li><li><code>when</code>：执行行为（<code>Mock</code>接口、真实调用）。</li><li><code>then</code>：输出条件（验证结果）。</li><li><code>and</code>：衔接上个标签，补充的作用。</li></ul><p>每个标签后面的双引号里可以添加描述，说明这块代码的作用（非强制），如<code>when："获取信息"</code>。因为Spock使用Groovy作为单元测试开发语言，所以代码量上比使用Java写的会少很多，比如<code>given</code>模块里通过构造函数的方式创建请求对象。</p><p><img src="https://p0.meituan.net/travelcube/f2481f9065acf487106ca4ce5d8b7e1a45797.png" alt referrerpolicy="no-referrer"></p><p>实际上<code>StudentDTO.java</code> 这个类并没有3个参数的构造方法，是Groovy帮我们实现的。Groovy默认会提供一个包含所有对象属性的构造方法。而且调用方式上可以指定属性名，类似于<code>key:value</code>的语法，非常人性化，方便在属性多的情况下构造对象，如果使用Java写，可能就要调用很多的<code>setXxx()</code>方法，才能完成对象初始化的工作。</p><p><img src="https://p0.meituan.net/travelcube/71741f252a0c73d52bce0993c51e908d23530.png" alt referrerpolicy="no-referrer"></p><p>这个就是Spock的Mock用法，当调用<code>studentDao.getStudentInfo()</code>方法时返回一个<code>List</code>。<code>List</code>的创建也很简单，中括号<code>[]</code>即表示<code>List</code>，Groovy会根据方法的返回类型，自动匹配是数组还是<code>List</code>，而<code>List</code>里的对象就是之前<code>given</code>块里构造的<code>user</code>对象，其中 <code>>></code> 就是指定返回结果，类似<code>Mockito</code>的<code>when().thenReturn()</code>语法，但更简洁一些。</p><p>如果要指定返回多个值的话，可以使用<code>3</code>个右箭头<code>>>></code>，比如：<code>studentDao.getStudentInfo() >>> [[student1,student2],[student3,student4],[student5,student6]]</code>。</p><p>也可以写成这样：<code>studentDao.getStudentInfo() >> [student1,student2] >> [student3,student4] >> [student5,student6]</code>。</p><p>每次调用<code>studentDao.getStudentInfo()</code>方法返回不同的值。</p><pre><code class="language-java">public List<StudentDTO> getStudentInfo(String id)&#123;
    List<StudentDTO> students = new ArrayList<>();
    return students;
&#125;
</code></pre><p>这个<code>getStudentInfo(String id)</code>方法，有个参数<code>id</code>，这种情况下如果使用Spock的Mock模拟调用的话，可以使用下划线<code>_</code>匹配参数，表示任何类型的参数，多个逗号隔开，类似于<code>Mockito</code>的<code>any()</code>方法。如果类中存在多个同名方法，可以通过 <code>_ as参数类型</code> 的方式区别调用，如下面的语法：</p><pre><code class="language-groovy">// _ 表示匹配任意类型参数
List<StudentDTO> students = studentDao.getStudentInfo(_);

// 如果有同名的方法，使用as指定参数类型区分
List<StudentDTO> students = studentDao.getStudentInfo(_ as String);
</code></pre><p><code>when</code>模块里是真正调用要测试方法的入口<code>tester.getStudentById()</code>。<code>then</code>模块作用是验证被测方法的结果是否正确，符合预期值，所以这个模块里的语句必须是<code>boolean</code>表达式，类似于JUnit的<code>assert</code>断言机制，但不必显示地写<code>assert</code>，这也是一种约定优于配置的思想。<code>then</code>块中使用了Spock的<code>with</code>功能，可以验证返回结果<code>response</code>对象内部的多个属性是否符合预期值，这个相对于JUnit的<code>assertNotNull</code>或<code>assertEquals</code>的方式更简单一些。</p><h4 id="强大的where">强大的Where</h4><p>上面的业务代码有2个<code>if</code>判断，是对邮编处理逻辑：</p><pre><code class="language-java">  // 邮编
  if ("上海".equals(studentDTO.getProvince())) &#123;
       studentVO.setAbbreviation("沪");
       studentVO.setPostCode("200000");
   &#125;
   if ("北京".equals(studentDTO.getProvince())) &#123;
       studentVO.setAbbreviation("京");
       studentVO.setPostCode("100000");
   &#125;
</code></pre><p>如果要完全覆盖这2个分支就需要构造不同的请求参数，多次调用被测试方法才能走到不同的分支。在前面，我们介绍了Spock的<code>where</code>标签可以很方便的实现这种功能，代码如下所示：</p><pre><code class="language-groovy">   @Unroll
   def "input 学生id:#id, 返回的邮编:#postCodeResult, 返回的省份简称:#abbreviationResult"() &#123;
        given: "Mock返回的学生信息"
        studentDao.getStudentInfo() >> students

        when: "获取学生信息"
        def response = tester.getStudentById(id)

        then: "验证返回结果"
        with(response) &#123;
            postCode == postCodeResult
            abbreviation == abbreviationResult
        &#125;
        where: "经典之处：表格方式验证学生信息的分支场景"
        id | students                    || postCodeResult | abbreviationResult
        1  | getStudent(1, "张三", "北京") || "100000"       | "京"
        2  | getStudent(2, "李四", "上海") || "200000"       | "沪"
    &#125;

    def getStudent(def id, def name, def province) &#123;
        return [new StudentDTO(id: id, name: name, province: province)]
    &#125;
</code></pre><p><code>where</code>模块第一行代码是表格的列名，多个列使用<code>|</code>单竖线隔开，<code>||</code>双竖线区分输入和输出变量，即左边是输入值，右边是输出值。格式如下：</p><p><code>输入参数1 | 输入参数2 || 输出结果1 | 输出结果2</code></p><p>而且<code>IntelliJ IDEA</code>支持<code>format</code>格式化快捷键，因为表格列的长度不一样，手动对齐比较麻烦。表格的每一行代表一个测试用例，即被测方法执行了2次，每次的输入和输出都不一样，刚好可以覆盖全部分支情况。比如<code>id</code>、<code>students</code>都是输入条件，其中<code>students</code>对象的构造调用了<code>getStudent</code>方法，每次测试业务代码传入不同的<code>student</code>值，<code>postCodeResult</code>、<code>abbreviationResult</code>表示对返回的<code>response</code>对象的属性判断是否正确。第一行数据的作用是验证返回的邮编是否是<code>100000</code>，第二行是验证邮编是否是<code>200000</code>。这个就是<code>where</code>+<code>with</code>的用法，更符合我们实际测试的场景，既能覆盖多种分支，又可以对复杂对象的属性进行验证，其中在定义的测试方法名，使用了Groovy的字面值特性：</p><p><img src="https://p1.meituan.net/travelcube/3c34e7616ad46b6652bebe2766d62c6530352.png" alt referrerpolicy="no-referrer"></p><p>即把请求参数值和返回结果值的字符串动态替换掉，<code>#id</code>、<code>#postCodeResult</code>、<code>#abbreviationResult</code>#号后面的变量是在方法内部定义的，实现占位符的功能。</p><p><code>@Unroll</code>注解，可以把每一次调用作为一个单独的测试用例运行，这样运行后的单元测试结果更加直观：</p><p><img src="https://p0.meituan.net/travelcube/bff376f956a6462437d1660f5cbe86d857414.png" alt referrerpolicy="no-referrer"></p><p>而且如果其中某行测试结果不对，Spock的错误提示信息也很详细，方便进行排查（比如我们把第1条测试用例返回的邮编改成<code>100001</code>）：</p><p><img src="https://p0.meituan.net/travelcube/bc83d5d0711eb30b962558f711058095365939.png" alt referrerpolicy="no-referrer"></p><p>可以看出，第1条测试用例失败，错误信息是<code>postCodeResult</code>的预期结果和实际结果不符，业务代码逻辑返回的邮编是<code>100000</code>，而我们预期的邮编是<code>100001</code>，这样就可以排查是业务代码逻辑有问题，还是我们的断言不对。</p><h2 id="5-异常测试">5. 异常测试</h2><p>我们再看下异常方面的测试，例如下面的代码：</p><pre><code class="language-java"> public void validateStudent(StudentVO student) throws BusinessException &#123;
        if(student == null)&#123;
            throw new BusinessException("10001", "student is null");
        &#125;
        if(StringUtils.isBlank(student.getName()))&#123;
            throw new BusinessException("10002", "student name is null");
        &#125;
        if(student.getAge() == null)&#123;
            throw new BusinessException("10003", "student age is null");
        &#125;
        if(StringUtils.isBlank(student.getTelephone()))&#123;
            throw new BusinessException("10004", "student telephone is null");
        &#125;
        if(StringUtils.isBlank(student.getSex()))&#123;
            throw new BusinessException("10005", "student sex is null");
        &#125;
    &#125;
</code></pre><p><code>BusinessException</code>是封装的业务异常，主要包含<code>code</code>、<code>message</code>属性：</p><pre><code class="language-java">/**
 * 自定义业务异常
 */
public class BusinessException extends RuntimeException &#123;
    private String code;
    private String message;

    setXxx...
    getXxx...
&#125;
</code></pre><p>这个大家应该都很熟悉，针对这种抛出多个不同错误码和错误信息的异常。如果使用JUnit的方式测试，会比较麻烦。如果是单个异常还好，如果是多个的话，测试代码就不太好写。</p><pre><code class="language-java">    @Test
    public void testException() &#123;
        StudentVO student = null;
        try &#123;
            service.validateStudent(student);
        &#125; catch (BusinessException e) &#123;
            Assert.assertEquals(e.getCode(), "10001");
            Assert.assertEquals(e.getMessage(), "student is null");
        &#125;

        student = new StudentVO();
        try &#123;
            service.validateStudent(student);
        &#125; catch (BusinessException e) &#123;
            Assert.assertEquals(e.getCode(), "10002");
            Assert.assertEquals(e.getMessage(), "student name is null");
        &#125;
    &#125;
</code></pre><p>当然可以使用JUnit的<code>ExpectedException</code>方式：</p><pre><code class="language-java">@Rule
public ExpectedException exception = ExpectedException.none();
exception.expect(BusinessException.class); // 验证异常类型
exception.expectMessage("xxxxxx"); //验证异常信息
</code></pre><p>或者使用<code>@Test(expected = BusinessException.class)</code> 注解，但这两种方式都有缺陷。</p><p><code>@Test</code>方式不能指定断言的异常属性，比如<code>code</code>、<code>message</code>。<code>ExpectedException</code>的方式也只提供了<code>expectMessage</code>的API，对自定义的<code>code</code>不支持，尤其像上面的有很多分支抛出多种不同异常码的情况。接下来我们看下Spock是如何解决的。Spock内置<code>thrown()</code>方法，可以捕获调用业务代码抛出的预期异常并验证，再结合<code>where</code>表格的功能，可以很方便地覆盖多种自定义业务异常，代码如下：</p><pre><code class="language-groovy">    @Unroll
    def "validate student info: #expectedMessage"() &#123;
        when: "校验"
        tester.validateStudent(student)

        then: "验证"
        def exception = thrown(expectedException)
        exception.code == expectedCode
        exception.message == expectedMessage

        where: "测试数据"
        student           || expectedException | expectedCode | expectedMessage
        getStudent(10001) || BusinessException | "10001"      | "student is null"
        getStudent(10002) || BusinessException | "10002"      | "student name is null"
        getStudent(10003) || BusinessException | "10003"      | "student age is null"
        getStudent(10004) || BusinessException | "10004"      | "student telephone is null"
        getStudent(10005) || BusinessException | "10005"      | "student sex is null"
    &#125;

    def getStudent(code) &#123;
        def student = new StudentVO()
        def condition1 = &#123;
            student.name = "张三"
        &#125;
        def condition2 = &#123;
            student.age = 20
        &#125;
        def condition3 = &#123;
            student.telephone = "12345678901"
        &#125;
        def condition4 = &#123;
            student.sex = "男"
        &#125;

        switch (code) &#123;
            case 10001:
                student = null
                break
            case 10002:
                student = new StudentVO()
                break
            case 10003:
                condition1()
                break
            case 10004:
                condition1()
                condition2()
                break
            case 10005:
                condition1()
                condition2()
                condition3()
                break
        &#125;
        return student
    &#125;
</code></pre><p>在<code>then</code>标签里用到了Spock的<code>thrown()</code>方法，这个方法可以捕获我们要测试的业务代码里抛出的异常。<code>thrown()</code>方法的入参<code>expectedException</code>，是我们自己定义的异常变量，这个变量放在<code>where</code>标签里就可以实现验证多种异常情况的功能（<code>Intellij Idea</code>格式化快捷键，可以自动对齐表格）。<code>expectedException</code>类型调用<code>validateUser</code>方法里定义的<code>BusinessException</code>异常，可以验证它所有的属性，<code>code</code>、<code>message</code>是否符合预期值。</p><p><img src="https://p0.meituan.net/travelcube/6fd52ed3170746695dd2304502688d8367835.png" alt referrerpolicy="no-referrer"></p><h2 id="6-spock静态方法测试">6. Spock静态方法测试</h2><p>接下来，我们一起看下Spock如何扩展第三方PowerMock对静态方法进行测试。</p><p>Spock的单元测试代码继承自<code>Specification</code>基类，而<code>Specification</code>又是基于JUnit的注解<code>@RunWith()</code>实现的，代码如下：</p><p><img src="https://p1.meituan.net/travelcube/80992f576e33e752c798d854e1733b1238195.png" alt referrerpolicy="no-referrer"></p><p>PowerMock的<code>PowerMockRunner</code>也是继承自JUnit，所以使用PowerMock的<code>@PowerMockRunnerDelegate()</code>注解，可以指定Spock的父类<code>Sputnik</code>去代理运行PowerMock，这样就可以在Spock里使用<code>PowerMock</code>去模拟静态方法、<code>final</code>方法、私有方法等。其实Spock自带的GroovyMock可以对Groovy文件的静态方法Mock，但对Java代码支持不完整，只能Mock当前Java类的静态方法，<a href="http://spockframework.org/spock/docs/1.3/all_in_one.html#_mocking_static_methods">官方给出的解释</a>如下：</p><p><img src="https://p0.meituan.net/travelcube/20ddd0aafe9dfcd5eae1f072fd311667106791.png" alt referrerpolicy="no-referrer"></p><p>如下代码：</p><pre><code class="language-java"> public StudentVO getStudentByIdStatic(int id) &#123;
        List<StudentDTO> students = studentDao.getStudentInfo();

        StudentDTO studentDTO = students.stream().filter(u -> u.getId() == id).findFirst().orElse(null);
        StudentVO studentVO = new StudentVO();
        if (studentDTO == null) &#123;
            return studentVO;
        &#125;
        studentVO.setId(studentDTO.getId());
        studentVO.setName(studentDTO.getName());
        studentVO.setSex(studentDTO.getSex());
        studentVO.setAge(studentDTO.getAge());

        // 静态方法调用
        String abbreviation = AbbreviationProvinceUtil.convert2Abbreviation(studentDTO.getProvince());
        studentVO.setAbbreviation(abbreviation);
        studentVO.setPostCode(studentDTO.getPostCode());

        return studentVO;
    &#125;
</code></pre><p>上面使用了<code>AbbreviationProvinceUtil.convert2Abbreviation()</code>静态方法，对应的测试用例代码如下：</p><pre><code class="language-Groovy">@RunWith(PowerMockRunner.class)
@PowerMockRunnerDelegate(Sputnik.class)
@PrepareForTest([AbbreviationProvinceUtil.class])
@SuppressStaticInitializationFor(["example.com.AbbreviationProvinceUtil"])
class StudentServiceStaticSpec extends Specification &#123;
    def studentDao = Mock(StudentDao)
    def tester = new StudentService(studentDao: studentDao)

    void setup() &#123;
        // mock静态类
        PowerMockito.mockStatic(AbbreviationProvinceUtil.class)
    &#125;

    def "test getStudentByIdStatic"() &#123;
        given: "创建对象"
        def student1 = new StudentDTO(id: 1, name: "张三", province: "北京")
        def student2 = new StudentDTO(id: 2, name: "李四", province: "上海")

        and: "Mock掉接口返回的学生信息"
        studentDao.getStudentInfo() >> [student1, student2]

        and: "Mock静态方法返回值"
        PowerMockito.when(AbbreviationProvinceUtil.convert2Abbreviation(Mockito.any())).thenReturn(abbreviationResult)

        when: "调用获取学生信息方法"
        def response = tester.getStudentByIdStatic(id)

        then: "验证返回结果是否符合预期值"
        with(response) &#123;
            abbreviation == abbreviationResult
        &#125;
        where:
        id || abbreviationResult
        1  || "京"
        2  || "沪"
    &#125;
&#125;
</code></pre><p>在<code>StudentServiceStaticSpec</code>类的头部使用<code>@PowerMockRunnerDelegate(Sputnik.class)</code>注解，交给Spock代理执行，这样既可以使用Spock +Groovy的各种功能，又可以使用PowerMock的对静态，<code>final</code>等方法的Mock。<code>@SuppressStaticInitializationFor(["example.com.AbbreviationProvinceUtil"])</code>，这行代码的作用是限制<code>AbbreviationProvinceUtil</code>类里的静态代码块初始化，因为<code>AbbreviationProvinceUtil</code>类在第一次调用时可能会加载一些本地资源配置，所以可以使用PowerMock禁止初始化。然后在<code>setup()</code>方法里对静态类进行Mock设置，<code>PowerMockito.mockStatic(AbbreviationProvinceUtil.class)</code>。最后在<code>test getStudentByIdStatic</code>测试方法里对<code>convert2Abbreviation()</code>方法指定返回默认值：<code>PowerMockito.when(AbbreviationProvinceUtil.convert2Abbreviation(Mockito.any())).thenReturn(abbreviationResult)</code>。</p><p>运行时在控制台会输出：</p><p><img src="https://p0.meituan.net/travelcube/da0606bde2a302e2da004f6d7d8b57b9206036.png" alt referrerpolicy="no-referrer"></p><p><font color="#dd0000">Notifications are not supported for behaviour ALL_TESTINSTANCES_ARE_CREATED_FIRST</font></p><p>这是Powermock的警告信息，不影响运行结果。</p><p>如果单元测试代码不需要对静态方法、<code>final</code>方法Mock，就没必要使用PowerMock，使用Spock自带的<code>Mock()</code>就足够了。因为PowerMock的原理是在编译期通过ASM字节码修改工具修改代码，然后使用自己的<code>ClassLoader</code>加载，而加载的静态方法越多，测试耗时就会越长。</p><h2 id="7-动态mock静态方法">7. 动态Mock静态方法</h2><p>考虑场景，让静态方法每次调用返回不同的值。</p><p>以下代码：</p><pre><code class="language-java">public List<OrderVO> getOrdersBySource()&#123;
        List<OrderVO> orderList = new ArrayList<>();
        OrderVO order = new OrderVO();
        if ("APP".equals(HttpContextUtils.getCurrentSource())) &#123;
            if("CNY".equals(HttpContextUtils.getCurrentCurrency()))&#123;
                System.out.println("source -> APP, currency -> CNY");
            &#125; else &#123;
                System.out.println("source -> APP, currency -> !CNY");
            &#125;
            order.setType(1);
        &#125; else if ("WAP".equals(HttpContextUtils.getCurrentSource())) &#123;
            System.out.println("source -> WAP");
            order.setType(2);
        &#125; else if ("ONLINE".equals(HttpContextUtils.getCurrentSource())) &#123;
            System.out.println("source -> ONLINE");
            order.setType(3);
        &#125;
        orderList.add(order);
        return orderList;
&#125;
</code></pre><p>这段代码的<code>if else</code>分支逻辑，主要是依据<code>HttpContextUtils</code>这个工具类的静态方法<code>getCurrentSource()</code>和<code>getCurrentCurrency()</code>的返回值来决定流程。这样的业务代码也是我们平时写单元测试时经常遇到的场景，如果能让<code>HttpContextUtils.getCurrentSource()</code>静态方法每次Mock出不同的值，就可以很方便地覆盖<code>if else</code>的全部分支逻辑。Spock的<code>where</code>标签可以方便地和PowerMock结合使用，让PowerMock模拟的静态方法每次返回不同的值，代码如下：</p><p><img src="https://p0.meituan.net/travelcube/64057c9b1e17b8b06f38c03012a67e62195579.png" alt referrerpolicy="no-referrer"></p><p>PowerMock的<code>thenReturn</code>方法返回的值是<code>source</code>和<code>currency</code>等2个变量，不是具体的数据，这2个变量对应<code>where</code>标签里的前两列<code>source|currency</code>。这样的写法，就可以在每次测试业务方法时，让<code>HttpContextUtils.getCurrentSource()</code>和<code>HttpContextUtils.getCurrentCurrency()</code>返回不同的来源和币种，就能轻松的覆盖<code>if</code>和<code>else</code>的分支代码。即Spock使用<code>where</code>表格的方式让PowerMock具有了动态Mock的功能。接下来，我们再看一下如何对于<code>final</code>变量进行Mock。</p><pre><code class="language-java">public List<OrderVO> convertOrders(List<OrderDTO> orders)&#123;
        List<OrderVO> orderList = new ArrayList<>();
        for (OrderDTO orderDTO : orders) &#123;
            OrderVO orderVO = OrderMapper.INSTANCE.convert(orderDTO);
            if (1 == orderVO.getType()) &#123;
                orderVO.setOrderDesc("App端订单");
            &#125; else if(2 == orderVO.getType()) &#123;
                orderVO.setOrderDesc("H5端订单");
            &#125; else if(3 == orderVO.getType()) &#123;
                orderVO.setOrderDesc("PC端订单");
            &#125;
            orderList.add(orderVO);
        &#125;
        return orderList;
&#125;
</code></pre><p>这段代码里的<code>for</code>循环第一行调用了<code>OrderMapper.INSTANCE.convert()</code>转换方法，将<code>orderDTO</code>转换为<code>orderVO</code>，然后根据<code>type</code>值走不同的分支，而<code>OrderMapper</code>是一个接口，代码如下：</p><pre><code class="language-java">@Mapper
public interface OrderMapper &#123;
    // 即使不用static final修饰，接口里的变量默认也是静态、final的
    static final OrderMapper INSTANCE = Mappers.getMapper(OrderMapper.class);

    @Mappings(&#123;&#125;)
    OrderVO convert(OrderDTO requestDTO);
&#125;
</code></pre><p><code>INSTANCE</code>是接口<code>OrderMapper</code>里定义的变量，接口里的变量默认都是<code>static final</code>的，所以我们要先把这个<code>INSTANCE</code>静态<code>final</code>变量Mock掉，这样才能调用它的方法<code>convert()</code>返回我们想要的值。<code>OrderMapper</code>这个接口是<code>mapstruct</code>工具的用法，<code>mapstruct</code>是做对象属性映射的一个工具，它会自动生成<code>OrderMapper</code>接口的实现类，生成对应的<code>set</code>、<code>get</code>方法，把<code>orderDTO</code>的属性值赋给<code>orderVO</code>属性，通常情况下会比使用反射的方式好不少。看下Spock如何写这个单元测试：</p><pre><code class="language-Groovy">@Unroll
def "test convertOrders"() &#123;
  given: "Mock掉OrderMapper的静态final变量INSTANCE，并结合Spock设置动态返回值"
  def orderMapper = Mock(OrderMapper.class)
  Whitebox.setInternalState(OrderMapper.class, "INSTANCE", orderMapper)
  orderMapper.convert(_) >> order

  when: 
  def orders = service.convertOrders([new OrderDTO()])

  then: "验证结果"
  with(orders) &#123;
    it[0].orderDesc == desc
  &#125;

  where: "测试数据"
  order                || desc
  new OrderVO(type: 1) || "App端订单"
  new OrderVO(type: 2) || "H5端订单"
  new OrderVO(type: 3) || "PC端订单"
&#125;
</code></pre><ul><li>首先使用Spock自带的<code>Mock()</code>方法，将<code>OrderMapper</code>类Mock为一个模拟对象<code>orderMapper</code>，<code>def orderMapper = Mock(OrderMapper.class)</code>。</li><li>然后使用PowerMock的<code>Whitebox.setInternalState()</code>，对<code>OrderMapper</code>接口的<code>static final</code>常量<code>INSTANCE</code>赋值(<code>Spock</code>不支持静态常量的<code>Mock</code>)，赋的值正是使用SpockMock的对象<code>orderMapper</code>。</li><li>使用Spock的Mock模拟<code>convert()</code>方法调用，<code>orderMapper.convert(_) >> order</code>，再结合<code>where</code>表格，实现动态Mock接口的功能。</li></ul><p>主要是这3行代码：</p><pre><code class="language-groovy">def orderMapper = Mock(OrderMapper.class) // 先使用Spock的Mock
Whitebox.setInternalState(OrderMapper.class, "INSTANCE", orderMapper) // 通过PowerMock把Mock对象orderMapper赋值给静态常量INSTANCE
orderMapper.convert(_) >> order // 结合where模拟不同的返回值
</code></pre><p>这样就可以使用Spock结合PowerMock测试静态常量，达到覆盖<code>if else</code>不同分支逻辑的功能。</p><h2 id="8-覆盖率">8. 覆盖率</h2><p>Jacoco是统计单元测试覆盖率的一种工具，当然Spock也自带了覆盖率统计的功能，这里使用第三方Jacoco的原因主要是国内公司使用的比较多一些，包括美团很多技术团队现在使用的也是Jacoco，所以为了兼容就以Jacoco来查看单元测试覆盖率。这里说下如何通过Jacoco确认分支是否完全覆盖到。</p><p>在pom文件里引用Jacoco的插件：<code>jacoco-maven-plugin</code>，然后执行<code>mvn package</code> 命令，成功后会在target目录下生成单元测试覆盖率的报告，点开报告找到对应的被测试类查看覆盖情况。</p><p><img src="https://p0.meituan.net/travelcube/c4b6ed707ffff42ce3c034ebd1109088440367.png" alt referrerpolicy="no-referrer"></p><p>绿色背景表示完全覆盖，黄色是部分覆盖，红色没有覆盖到。比如第<code>34</code>行黄色背景的<code>else if()</code> 判断，提示有二分之一的分支缺失，虽然它下面的代码也被覆盖了（显示为绿色），这种情况跟具体使用哪种单元测试框架没关系，因为这只是分支覆盖率统计的规则，只不过使用Spock的话，解决起来会更简单，只需在<code>where</code>下增加一行针对的测试数据即可。</p><h2 id="9-dao层测试">9. DAO层测试</h2><p>DAO层的测试有些不太一样，不能再使用Mock，否则无法验证SQL是否正确。对于DAO测试有一般最简的方式是直接使用<code>@SpringBootTest</code>注解启动测试环境，通过Spring创建Mybatis、Mapper实例，但这种方式并不属于单元测试，而是集成测试范畴了，因为当启用<code>@SpringBootTest</code>时，会把整个应用的上下文加载进来。不仅耗时时间长，而且一旦依赖环境上有任何问题，可能会影响启动，进而影响DAO层的测试。最后，需要到数据库尽可能隔离，因为如果大家都使用同一个Test环境的数据的话，一旦测试用例编写有问题，就可能会污染Test环境的数据。</p><p>针对以上场景，可采用以下方案：
1. 通过MyBatis的SqlSession启动mapper实例（避免通过Spring启动加载上下文信息）。
2. 通过内存数据库（如H2）隔离大家的数据库连接（完全隔离不会存在互相干扰的现象）。
3. 通过DBUnit工具，用作对于数据库层的操作访问工具。
4. 通过扩展Spock的注解，提供对于数据库Schema创建和数据Data加载的方式。如csv、xml或直接<code>Closure</code>编写等。</p><p>在pom文件增加相应的依赖。</p><pre><code class="language-xml"><dependency>
     <groupId>com.h2database</groupId>
     <artifactId>h2</artifactId>
     <version>1.4.200</version>
     <scope>test</scope>
 </dependency>
 <dependency>
     <groupId>org.dbunit</groupId>
     <artifactId>dbunit</artifactId>
     <version>2.5.1</version>
     <scope>test</scope>
 </dependency>
</code></pre><p>增加Groovy的maven插件、资源文件拷贝以及测试覆盖率统计插件。</p><pre><code class="language-xml"><!-- 测试插件 -->
<plugin>
  <groupId>org.codehaus.gmavenplus</groupId>
  <artifactId>gmavenplus-plugin</artifactId>
  <version>1.8.1</version>
  <executions>
    <execution>
      <goals>
        <goal>addSources</goal>
        <goal>addTestSources</goal>
        <goal>generateStubs</goal>
        <goal>compile</goal>
        <goal>generateTestStubs</goal>
        <goal>compileTests</goal>
        <goal>removeStubs</goal>
        <goal>removeTestStubs</goal>
      </goals>
    </execution>
  </executions>
</plugin>
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>3.0.0-M3</version>
  <configuration>
    <useFile>false</useFile>
    <includes>
      <include>**/*Spec.java</include>
    </includes>
    <parallel>methods</parallel>
    <threadCount>10</threadCount>
    <testFailureIgnore>true</testFailureIgnore>
  </configuration>
</plugin>
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-resources-plugin</artifactId>
  <version>2.6</version>
  <executions>
    <execution>
      <id>copy-resources</id>
      <phase>compile</phase>
      <goals>
        <goal>copy-resources</goal>
      </goals>
      <configuration>
        <outputDirectory>$&#123;basedir&#125;/target/resources</outputDirectory>
        <resources>
          <resource>
            <directory>$&#123;basedir&#125;/src/main/resources</directory>
            <filtering>true</filtering>
          </resource>
        </resources>
      </configuration>
    </execution>
  </executions>
</plugin>
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.2</version>
  <executions>
    <execution>
      <id>prepare-agent</id>
      <goals>
        <goal>prepare-agent</goal>
      </goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>prepare-package</phase>
      <goals>
        <goal>report</goal>
      </goals>
    </execution>
    <execution>
      <id>post-unit-test</id>
      <phase>test</phase>
      <goals>
        <goal>report</goal>
      </goals>
      <configuration>
        <dataFile>target/jacoco.exec</dataFile>
        <outputDirectory>target/jacoco-ut</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
</code></pre><p>加入对于Spock扩展的自动处理框架（用于数据<code>Schema</code>和<code>Data</code>初始化操作）。</p><p><img src="https://p0.meituan.net/travelcube/bf6258bf6608da3d9e6e3f28806ae056104189.png" alt referrerpolicy="no-referrer"></p><p>这里介绍一下主要内容，注解<code>@MyDbUnit</code>：</p><pre><code class="language-java">@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@ExtensionAnnotation(MyDbUnitExtension.class)
@interface MyDbUnit &#123;
    /**
     * <pre>
     * content = &#123;
     *    your_table_name(id: 1, name: 'xxx', age: 21)
     *    your_table_name(id: 2, name: 'xxx', age: 22)
     * &#125;)
     </pre>
     * @return
     */
    Class<? extends Closure> content() default Closure.class;
    /**
     * xml存放路径(相对于测试类)
     * @return
     */
    String xmlLocation() default "";
    /**
     * csv存放路径(相对于测试类)
     * @return
     */
    String csvLocation() default "";
&#125;
</code></pre><p>考虑以下代码的测试：</p><pre><code class="language-java">@Repository("personInfoMapper")
public interface PersonInfoMapper &#123;
    @Delete("delete from person_info where id=#&#123;id&#125;")
    int deleteById(Long id);

    @Select("select count(*) from person_info")
    int count();

    @Select("select * from user_info")
    List<PersonInfoDO> selectAll();
&#125;
</code></pre><p><code>Demo1</code> （使用<code>@MyDbUnit</code>，<code>content</code>指定导入数据内容，格式<code>Closure</code>）。</p><pre><code class="language-groovy">class Demo1Spec extends MyBaseSpec &#123;

    /**
     * 直接获取待测试的mapper
     */
    def personInfoMapper = MapperUtil.getMapper(PersonInfoMapper.class)

    /**
     * 测试数据准备，通常为sql表结构创建用的ddl，支持多个文件以逗号分隔。
     */
    def setup() &#123;
        executeSqlScriptFile("com/xxx/xxx/xxx/......../schema.sql")
    &#125;
    /**
     * 数据表清除，通常待drop的数据表
     */
    def cleanup() &#123;
        dropTables("person_info")
    &#125;

    /**
     * 直接构造数据库中的数据表,此方法适用于数据量较小的mapper sql测试
     */
    @MyDbUnit(
            content = &#123;
                person_info(id: 1, name: "abc", age: 21)
                person_info(id: 2, name: "bcd", age: 22)
                person_info(id: 3, name: "cde", age: 23)
            &#125;
    )
    def "demo1_01"() &#123;
        when:
        int beforeCount = personInfoMapper.count()
        // groovy sql用于快速执行sql，不仅能验证数据结果，也可向数据中添加数据。
        def result = new Sql(dataSource).firstRow("select * from `person_info`") 
        int deleteCount = personInfoMapper.deleteById(1L)
        int afterCount = personInfoMapper.count()

        then:
        beforeCount == 3
        result.name == "abc"
        deleteCount == 1
        afterCount == 2
    &#125;

    /**
     * 直接构造数据库中的数据表,此方法适用于数据量较小的mapper sql测试
     */
    @MyDbUnit(content = &#123;
        person_info(id: 1, name: 'a', age: 21)
    &#125;)
    def "demo1_02"() &#123;
        when:
        int beforeCount = personInfoMapper.count()
        def result = new Sql(dataSource).firstRow("select * from `person_info`")
        int deleteCount = personInfoMapper.deleteById(1L)
        int afterCount = personInfoMapper.count()

        then:
        beforeCount == 1
        result.name == "a"
        deleteCount == 1
        afterCount == 0
    &#125;
&#125;
</code></pre><p><img src="https://p0.meituan.net/travelcube/c3ef02e720850a7dfd896a4cba48e45e64936.png" alt referrerpolicy="no-referrer"></p><p>在<code>setup()</code>阶段，把数据库表中的<code>Schema</code>创建好，然后通过下面的<code>@MyDbUnit</code>注解的<code>content</code>属性，把数据导入到数据库中。<code>person_info</code>是表名，<code>id</code>、<code>name</code>、<code>age</code>是数据。</p><p><img src="https://p0.meituan.net/travelcube/c594497ed85fa3c3600290ec1ff9d95372574.png" alt referrerpolicy="no-referrer"></p><p>通过<code>MapperUtil.getMapper()</code>方法获取<code>mapper</code>实例。</p><p><img src="https://p0.meituan.net/travelcube/a7c0d905fdb3d37d462c78daf1a3b33b37850.png" alt referrerpolicy="no-referrer"></p><p>当测试数据量较大时，可以编写相应的数据文件，通过<code>@MyDbUnit</code>的<code>xmlLocation</code>或<code>csvLocation</code>加载文件（分别支持csv和xml格式）。</p><p><img src="https://p0.meituan.net/travelcube/ffd4e358f8b1aba82c238851df3fe460171003.png" alt referrerpolicy="no-referrer"></p><p>如通过csv加载文件，<code>csvLocation</code>指向csv文件所在文件夹。</p><pre><code class="language-groovy"> @MyDbUnit(csvLocation = "com/xxx/........./data01")
    def "demo2_01"() &#123;
        when:
        int beforeCount = personInfoMapper.count()
        def result = new Sql(dataSource).firstRow("select * from `person_info`")
        int deleteCount = personInfoMapper.deleteById(1L)
        int afterCount = personInfoMapper.count()

        then:
        beforeCount == 3
        result.name == "abc"
        deleteCount == 1
        afterCount == 2
    &#125;
</code></pre><p>通过xml加载文件，<code>xmlLocation</code>指向xml文件所在路径。</p><pre><code class="language-groovy">@MyDbUnit(xmlLocation = "com/xxxx/........./demo3_02.xml")
    def "demo3_02"() &#123;
        when:
        int beforeCount = personInfoMapper.count()
        def result = new Sql(dataSource).firstRow("select * from `person_info`")
        int deleteCount = personInfoMapper.deleteById(1L)
        int afterCount = personInfoMapper.count()

        then:
        beforeCount == 1
        result.name == "a"
        deleteCount == 1
        afterCount == 0
    &#125;
</code></pre><p>还可以不通过<code>@MyDbUnit</code>而使用API直接加载测试数据文件。</p><pre><code class="language-groovy">class Demo4Spec extends MyBaseSpec &#123;
    def personInfoMapper = MapperUtil.getMapper(PersonInfoMapper.class)

    /**
     * 数据表清除，通常待drop的数据表
     */
    def cleanup() &#123;
        dropTables("person_info")
    &#125;
    def "demo4_01"() &#123;
        given:
        executeSqlScriptFile("com/xxxx/.........../schema.sql")
        IDataSet dataSet = MyDbUnitUtil.loadCsv("com/xxxx/.........../data01");
        DatabaseOperation.CLEAN_INSERT.execute(MyIDatabaseConnection.getInstance().getConnection(), dataSet);

        when:
        int beforeCount = personInfoMapper.count()
        def result = new Sql(dataSource).firstRow("select * from `person_info`")
        int deleteCount = personInfoMapper.deleteById(1L)
        int afterCount = personInfoMapper.count()

        then:
        beforeCount == 3
        result.name == "abc"
        deleteCount == 1
        afterCount == 2
    &#125;

    def "demo4_02"() &#123;
        given:
        executeSqlScriptFile("com/xxxx/.........../schema.sq")
        IDataSet dataSet = MyDbUnitUtil.loadXml("com/xxxx/.........../demo3_02.xml");
        DatabaseOperation.CLEAN_INSERT.execute(MyIDatabaseConnection.getInstance().getConnection(), dataSet);

        when:
        int beforeCount = personInfoMapper.count()
        def result = new Sql(dataSource).firstRow("select * from `person_info`")
        int deleteCount = personInfoMapper.deleteById(1L)
        int afterCount = personInfoMapper.count()

        then:
        beforeCount == 1
        result.name == "a"
        deleteCount == 1
        afterCount == 0
    &#125;
&#125;
</code></pre><p>最后为大家梳理了一些文档，供大家参考。</p><ul><li><a href="https://spockframework.org/spock/docs/2.0/all_in_one.html">Spock Framework Reference Documentation</a></li><li><a href="https://javakk.com/category/spock">老K的Java博客</a></li></ul><h2 id="作者简介">作者简介</h2><p>建华，美团优选事业部工程师。</p>  
</div>
            