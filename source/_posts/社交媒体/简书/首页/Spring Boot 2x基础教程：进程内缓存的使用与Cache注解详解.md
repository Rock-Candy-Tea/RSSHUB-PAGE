
---
title: 'Spring Boot 2.x基础教程：进程内缓存的使用与Cache注解详解'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1447174-4afa3ca51dc5899d.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1447174-4afa3ca51dc5899d.png'
---

<div>   
<p>随着时间的积累，应用的使用用户不断增加，数据规模也越来越大，往往数据库查询操作会成为影响用户使用体验的瓶颈，此时使用缓存往往是解决这一问题非常好的手段之一。Spring 3开始提供了强大的基于注解的缓存支持，可以通过注解配置方式低侵入的给原有Spring应用增加缓存功能，提高数据访问性能。</p>
<p>在Spring Boot中对于缓存的支持，提供了一系列的自动化配置，使我们可以非常方便的使用缓存。下面我们通过一个简单的例子来展示，我们是如何给一个既有应用增加缓存功能的。</p>
<h2>快速入门</h2>
<p>下面我们将使用<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fblog.didispace.com%2Fspring-boot-learning-21-3-4%2F" target="_blank">使用Spring Data JPA访问MySQL</a>一文的案例为基础。这个案例中包含了使用Spring Data JPA访问User数据的操作，利用这个基础，我们为其添加缓存，来减少对数据库的IO，以达到访问加速的作用。如果您还不熟悉如何实现对MySQL的读写操作，那么建议先阅读前文，完成这个基础案例的编写。</p>
<p>先简单回顾下这个案例的基础内容：</p>
<p><strong>User实体的定义</strong></p>
<pre><code class="java">@Entity
@Data
@NoArgsConstructor
public class User &#123;

    @Id
    @GeneratedValue
    private Long id;

    private String name;
    private Integer age;

    public User(String name, Integer age) &#123;
        this.name = name;
        this.age = age;
    &#125;
&#125;
</code></pre>
<p><strong>User实体的数据访问实现</strong></p>
<pre><code class="java">public interface UserRepository extends JpaRepository<User, Long> &#123;

    User findByName(String name);

    User findByNameAndAge(String name, Integer age);

    @Query("from User u where u.name=:name")
    User findUser(@Param("name") String name);

&#125;
</code></pre>
<p>为了更好的理解缓存，我们先对该工程做一些简单的改造。</p>
<ul>
<li>
<code>application.properties</code>文件中新增<code>spring.jpa.show-sql=true</code>，开启hibernate对sql语句的打印。如果是1.x版本，使用<code>spring.jpa.properties.hibernate.show_sql=true</code>参数。</li>
<li>修改单元测试类，插入User表一条用户名为AAA，年龄为10的数据。并通过findByName函数完成两次查询，具体代码如下：</li>
</ul>
<pre><code class="java">@RunWith(SpringRunner.class)
@SpringBootTest
public class Chapter51ApplicationTests &#123;

    @Autowired
    private UserRepository userRepository;

    @Test
    public void test() throws Exception &#123;
        // 创建1条记录
        userRepository.save(new User("AAA", 10));

        User u1 = userRepository.findByName("AAA");
        System.out.println("第一次查询：" + u1.getAge());

        User u2 = userRepository.findByName("AAA");
        System.out.println("第二次查询：" + u2.getAge());
    &#125;

&#125;
</code></pre>
<p>在没有加入缓存之前，我们可以先执行一下这个案例，可以看到如下的日志：</p>
<pre><code class="bash">Hibernate: select user0_.id as id1_0_, user0_.age as age2_0_, user0_.name as name3_0_ from user user0_ where user0_.name=?
第一次查询：10
Hibernate: select user0_.id as id1_0_, user0_.age as age2_0_, user0_.name as name3_0_ from user user0_ where user0_.name=?
第二次查询：10
</code></pre>
<p>两次<code>findByName</code>查询都执行了两次SQL，都是对MySQL数据库的查询。</p>
<h2>引入缓存</h2>
<p>第一步：在<code>pom.xml</code>中引入cache依赖，添加如下内容：</p>
<pre><code class="xml"><dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-cache</artifactId>
</dependency>
</code></pre>
<p>第二步：在Spring Boot主类中增加<code>@EnableCaching</code>注解开启缓存功能，如下：</p>
<pre><code class="java">@EnableCaching
@SpringBootApplication
public class Chapter51Application &#123;

    public static void main(String[] args) &#123;
        SpringApplication.run(Chapter51Application.class, args);
    &#125;

&#125;
</code></pre>
<p>第三步：在数据访问接口中，增加缓存配置注解，如：</p>
<pre><code class="java">@CacheConfig(cacheNames = "users")
public interface UserRepository extends JpaRepository<User, Long> &#123;

    @Cacheable
    User findByName(String name);

&#125;
</code></pre>
<p>第四步：再来执行以下单元测试，可以在控制台中输出了下面的内容</p>
<pre><code class="bash">Hibernate: insert into user (age, name, id) values (?, ?, ?)
Hibernate: select user0_.id as id1_0_, user0_.age as age2_0_, user0_.name as name3_0_ from user user0_ where user0_.name=?
第一次查询：10
第二次查询：10
</code></pre>
<p>到这里，我们可以看到，在调用第二次<code>findByName</code>函数时，没有再执行select语句，也就直接减少了一次数据库的读取操作。</p>
<p>为了可以更好的观察，缓存的存储，我们可以在单元测试中注入<code>CacheManager</code>。</p>
<pre><code>@Autowired
private CacheManager cacheManager;
</code></pre>
<p>使用debug模式运行单元测试，观察<code>CacheManager</code>中的缓存集users以及其中的User对象的缓存加深理解。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1702" data-height="1868"><img data-original-src="//upload-images.jianshu.io/upload_images/1447174-4afa3ca51dc5899d.png" data-original-width="1702" data-original-height="1868" data-original-format="image/png" data-original-filesize="342048" src="https://upload-images.jianshu.io/upload_images/1447174-4afa3ca51dc5899d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>可以看到，在第一次调用<code>findByName</code>函数之后，<code>CacheManager</code>将这个查询结果保存了下来，所以在第二次访问的时候，就能匹配上而不需要再访问数据库了。</p>
<h2>Cache配置注解详解</h2>
<p>回过头来我们再来看这里使用到的两个注解分别作了什么事情：</p>
<ul>
<li>
<code>@CacheConfig</code>：主要用于配置该类中会用到的一些共用的缓存配置。在这里<code>@CacheConfig(cacheNames = "users")</code>：配置了该数据访问对象中返回的内容将存储于名为users的缓存对象中，我们也可以不使用该注解，直接通过<code>@Cacheable</code>自己配置缓存集的名字来定义。</li>
<li>
<code>@Cacheable</code>：配置了findByName函数的返回值将被加入缓存。同时在查询时，会先从缓存中获取，若不存在才再发起对数据库的访问。该注解主要有下面几个参数：
<ul>
<li>
<code>value</code>、<code>cacheNames</code>：两个等同的参数（<code>cacheNames</code>为Spring 4新增，作为<code>value</code>的别名），用于指定缓存存储的集合名。由于Spring 4中新增了<code>@CacheConfig</code>，因此在Spring 3中原本必须有的<code>value</code>属性，也成为非必需项了</li>
<li>
<code>key</code>：缓存对象存储在Map集合中的key值，非必需，缺省按照函数的所有参数组合作为key值，若自己配置需使用SpEL表达式，比如：<code>@Cacheable(key = "#p0")</code>：使用函数第一个参数作为缓存的key值，更多关于SpEL表达式的详细内容可参考<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fdocs.spring.io%2Fspring%2Fdocs%2Fcurrent%2Fspring-framework-reference%2Fhtml%2Fcache.html%23cache-spel-context" target="_blank">官方文档</a>
</li>
<li>
<code>condition</code>：缓存对象的条件，非必需，也需使用SpEL表达式，只有满足表达式条件的内容才会被缓存，比如：<code>@Cacheable(key = "#p0", condition = "#p0.length() < 3")</code>，表示只有当第一个参数的长度小于3的时候才会被缓存，若做此配置上面的AAA用户就不会被缓存，读者可自行实验尝试。</li>
<li>
<code>unless</code>：另外一个缓存条件参数，非必需，需使用SpEL表达式。它不同于<code>condition</code>参数的地方在于它的判断时机，该条件是在函数被调用之后才做判断的，所以它可以通过对result进行判断。</li>
<li>
<code>keyGenerator</code>：用于指定key生成器，非必需。若需要指定一个自定义的key生成器，我们需要去实现<code>org.springframework.cache.interceptor.KeyGenerator</code>接口，并使用该参数来指定。需要注意的是：<strong>该参数与<code>key</code>是互斥的</strong>
</li>
<li>
<code>cacheManager</code>：用于指定使用哪个缓存管理器，非必需。只有当有多个时才需要使用</li>
<li>
<code>cacheResolver</code>：用于指定使用那个缓存解析器，非必需。需通过<code>org.springframework.cache.interceptor.CacheResolver</code>接口来实现自己的缓存解析器，并用该参数指定。</li>
</ul>
</li>
</ul>
<p>除了这里用到的两个注解之外，还有下面几个核心注解：</p>
<ul>
<li>
<code>@CachePut</code>：配置于函数上，能够根据参数定义条件来进行缓存，它与<code>@Cacheable</code>不同的是，它每次都会真是调用函数，所以主要用于数据新增和修改操作上。它的参数与<code>@Cacheable</code>类似，具体功能可参考上面对<code>@Cacheable</code>参数的解析</li>
<li>
<code>@CacheEvict</code>：配置于函数上，通常用在删除方法上，用来从缓存中移除相应数据。除了同<code>@Cacheable</code>一样的参数之外，它还有下面两个参数：
<ul>
<li>
<code>allEntries</code>：非必需，默认为false。当为true时，会移除所有数据</li>
<li>
<code>beforeInvocation</code>：非必需，默认为false，会在调用方法之后移除数据。当为true时，会在调用方法之前移除数据。</li>
</ul>
</li>
</ul>
<h2>代码示例</h2>
<p>本文的相关例子可以查看下面仓库中的<code>chapter5-1</code>目录：</p>
<ul>
<li>Github：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fdyc87112%2FSpringBoot-Learning%2Ftree%2Fmaster%2F2.1.x" target="_blank">https://github.com/dyc87112/SpringBoot-Learning/</a>
</li>
<li>Gitee：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgitee.com%2Fdidispace%2FSpringBoot-Learning%2Ftree%2Fmaster%2F2.1.x" target="_blank">https://gitee.com/didispace/SpringBoot-Learning/</a>
</li>
</ul>
<p><strong>如果您觉得本文不错，欢迎<code>Star</code>支持，您的关注是我坚持的动力！</strong></p>
<blockquote>
<p>本文首发：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fblog.didispace.com%2Fspring-boot-learning-21-5-1%2F" target="_blank">Spring Boot 2.x基础教程：进程内缓存的使用与Cache注解详解</a>，转载请注明出处。<br>
欢迎关注我的公众号：程序猿DD，获得独家整理的学习资源和日常干货推送。<br>
如果您对我的其他专题内容感兴趣，直达我的个人博客：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fblog.didispace.com" target="_blank">didispace.com</a>。</p>
</blockquote>
  
</div>
            