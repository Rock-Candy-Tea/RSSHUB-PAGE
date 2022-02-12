
---
title: 'springCloud --- 高级篇(3)'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/11531502-9bd7c6876eded4ec.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/11531502-9bd7c6876eded4ec.png'
---

<div>   
<p>本系列笔记涉及到的代码在GitHub上，地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fzsllsz%2Fcloud" target="_blank">https://github.com/zsllsz/cloud</a></p>
<p>本文涉及知识点：</p>
<ul>
<li>分布式事务解决方案之Alibaba seata；</li>
</ul>
<h1>一、分布式事务问题</h1>
<p>打个比方，我们在淘宝下单买一件商品，可能涉及到了三个微服务，分别是订单服务，库存服务，支付服务。这三个服务连接的是三个不同的数据库，但是下单的这一个过程对外是表现出一个整体。比如下单成功，然后扣库存也成功了，最后支付这一步失败了，那么库存系统和订单系统都应该回滚这一次操作。同一个数据库用事务就可以回滚了，不同数据库，那就要用分布式事务了。即每个数据库内部的数据一致性由本地事务来保证，全局数据一致性就由分布式事务来保证。</p>
<hr>
<p>欢迎大家关注我的公众号 <strong>javawebkf</strong>，目前正在慢慢地将简书文章搬到公众号，以后简书和公众号文章将同步更新，且简书上的付费文章在公众号上将免费。</p>
<hr>
<h1>二、springCloud Alibaba Seata简介</h1>
<p><strong>1、是什么？</strong><br>
seata就是用来解决分布式事务的。官网地址：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fseata.io%2Fzh-cn%2F" target="_blank">http://seata.io/zh-cn/</a></p>
<p><strong>2、seata相关术语：</strong><br>
分布式事务处理过程的<code>1个id + 3个组件</code> 模型：1个id就是指全局唯一的事务id(transaction id)；3个组件指的是：</p>
<ul>
<li><p>Transaction Coordinator(TC)：事务协调者，说白了就是你服务器上安装的seata。维护全局和分支事务的状态，驱动全局事务提交或回滚。</p></li>
<li><p>Transaction Manager(TM)：事务管理者，说白了就是你加了@GlobalTransactional注解的那个方法。定义全局事务的范围，负责开启一个全局事务，并最终发起全局事务提交或者回滚的决议。</p></li>
<li><p>Resource Manager(RM)：资源管理器，说白了就是本次涉及到的数据库。管理分支事务的资源，负责分支注册、状态汇报，并接收事务协调器的指令，驱动分支(本地)事务的提交和回滚。</p></li>
</ul>
<p><strong>3、seata处理分布式事务的过程：</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="848" data-height="357"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-9bd7c6876eded4ec.png" data-original-width="848" data-original-height="357" data-original-format="image/png" data-original-filesize="116568" src="https://upload-images.jianshu.io/upload_images/11531502-9bd7c6876eded4ec.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">seata分布式事务处理过程</div>
</div>
<ul>
<li>TM向TC申请开启一个全局事务，全局事务创建成功并生成一个全局唯一的XID；</li>
<li>XID在微服务调用链路的上下文中传播；</li>
<li>RM向TC注册分支事务，将其纳入XID对用的全局事务的管辖；</li>
<li>TM向TC发起针对XID的全局提交或回滚决议；</li>
<li>TC调度XID下管辖的全部分支事务完成提交或回滚请求。</li>
</ul>
<p>简单地说，整个过程就是用一个XID关联起来的，比如下订单的过程是一个整体过程，需要用分布式事务，那么订单系统、库存系统和支付系统就会被同一个XID管着，表明它们是一个整体。每个系统就是一个RM，每个系统自己的事务由本地事务完成，每个系统的操作提交还是回滚都会告诉TM，TM再把结果告诉最终该提交还是回滚告诉TC去执行。</p>
<p><strong>3、怎么玩？</strong></p>
<ul>
<li>去哪儿下：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Ftags" target="_blank">https://github.com/seata/seata/tags</a>
</li>
<li>怎么用：本地加@Transactional注解，全局加@GlobalTrasactional注解就完事了(先有个映像，编码实战部分再看具体用法)</li>
<li>安装：官网下载后，解压</li>
<li>在seata/config目录下，有一个nacos-config.txt，打开它，关注文件中的</li>
</ul>
<pre><code>service.vgroup_mapping.my_test_tx_group=default
</code></pre>
<p><code>my_test_tx_group</code>就是组名，等下在file.conf和项目的application.yml中都要用到的。</p>
<ul>
<li>修改conf目录下的file.conf，主要改的是自定义事务组名称、事务日志存储模式改为db、数据库连接信息，如下：</li>
</ul>
<p>这一段是修改事务组名称，即修改了service块的第一行，注意第一行要跟nacos-config.txt中的那一行对应，说白了就是将nacos-config.txt中的那一行拷贝过来去掉<code>service.</code>，等于号后面的值用引号引起来就可以了。还有就是default.grouplist后面的ip和端口，就是你seata启动的ip和端口。</p>
<pre><code>service &#123;
  #vgroup->rgroup
  vgroup_mapping.my_test_tx_group = "default"
  #only support single node
  default.grouplist = "192.168.0.106:8091"
  #degrade current not support
  enableDegrade = false
  #disable
  disable = false
  #unit ms,s,m,h,d represents milliseconds, seconds, minutes, hours, days, default permanent
  max.commit.retry.timeout = "-1"
  max.rollback.retry.timeout = "-1"
&#125;
</code></pre>
<p>store块，存储模式由file改为db。</p>
<pre><code>store &#123;
  ## store mode: file、db
  mode = "db"
  ……
&#125;
</code></pre>
<p>db块中配置自己的数据库连接信息。</p>
<pre><code>db &#123;
    ## the implement of javax.sql.DataSource, such as DruidDataSource(druid)/BasicDataSource(dbcp) etc.
    datasource = "dbcp"
    ## mysql/oracle/h2/oceanbase etc.
    db-type = "mysql"
    driver-class-name = "com.mysql.jdbc.Driver"
    url = "jdbc:mysql://192.168.0.106:3306/seata"
    user = "root"
    password = "zsl"
    min-conn = 1
    max-conn = 3
    global.table = "global_table"
    branch.table = "branch_table"
    lock-table = "lock_table"
    query-limit = 100
  &#125;
</code></pre>
<ul>
<li>新建数据库seata；</li>
<li>在seata里新建表，建表的sql在conf目录下，名为db_store.sql，在seata库执行就好了；</li>
<li>修改conf目录下的registry.conf，指明注册中心为nacos，配置nacos的连接信息，如下：</li>
</ul>
<pre><code>registry &#123;
  # file 、nacos 、eureka、redis、zk、consul、etcd3、sofa
  type = "nacos"

  nacos &#123;
    serverAddr = "192.168.0.106:8848"
    namespace = ""
    cluster = "default"
  &#125;
</code></pre>
<ul>
<li>启动nacos；</li>
<li>初始化seata的nacos配置：进入seata/conf目录，执行：</li>
</ul>
<pre><code>sh nacos-config.sh 192.168.0.106
</code></pre>
<p>这个ip就是你nacos所在的服务器IP。</p>
<ul>
<li>启动seata-server，直接执行seata/bin目录执行：</li>
</ul>
<pre><code>sh seata-server.sh -p 8091 -m db
</code></pre>
<p>-p是端口，-m是存储模式，我们配置了db存储，所以这里用db。</p>
<p>最后日志打印出如下日志表明启动成功：</p>
<pre><code>load RegistryProvider[Nacos] extension by class[io.seata.discovery.registry.nacos.NacosRegistryProvider]
</code></pre>
<h1>三、实战之数据库的准备</h1>
<p>创建三个微服务，调用链路为 下订单 ---> 扣库存 ---> 减余额。<br>
<strong>1、创建数据库：</strong></p>
<ul>
<li>seata_order：存储订单信息的数据库</li>
<li>seata_storage：存储库存信息的数据库</li>
<li>seata_account：存储账户信息的数据库<br>
建库的sql如下：</li>
</ul>
<pre><code>create database seata_order;
create database seata_storage;
create database seata_account;
</code></pre>
<p><strong>2、建立业务数据表：</strong></p>
<ul>
<li>seata_order库下新建t_order表：</li>
</ul>
<pre><code>DROP TABLE IF EXISTS `t_order`;
CREATE TABLE `t_order`  (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) DEFAULT NULL COMMENT '用户id',
  `product_id` bigint(11) DEFAULT NULL COMMENT '产品id',
  `count` int(11) DEFAULT NULL COMMENT '数量',
  `money` decimal(11, 0) DEFAULT NULL COMMENT '金额',
  `status` int(1) DEFAULT NULL COMMENT '订单状态:  0:创建中 1:已完结',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '订单表' ROW_FORMAT = Dynamic;
</code></pre>
<ul>
<li>seata_storage库下新建t_storage表：</li>
</ul>
<pre><code>DROP TABLE IF EXISTS `t_storage`;
CREATE TABLE `t_storage`  (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `product_id` bigint(11) DEFAULT NULL COMMENT '产品id',
  `total` int(11) DEFAULT NULL COMMENT '总库存',
  `used` int(11) DEFAULT NULL COMMENT '已用库存',
  `residue` int(11) DEFAULT NULL COMMENT '剩余库存',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '库存' ROW_FORMAT = Dynamic;
INSERT INTO `t_storage` VALUES (1, 1, 100, 0, 100);
</code></pre>
<ul>
<li>seata_account库下新建t_account表：</li>
</ul>
<pre><code>CREATE TABLE `t_account`  (
  `id` bigint(11) NOT NULL COMMENT 'id',
  `user_id` bigint(11) DEFAULT NULL COMMENT '用户id',
  `total` decimal(10, 0) DEFAULT NULL COMMENT '总额度',
  `used` decimal(10, 0) DEFAULT NULL COMMENT '已用余额',
  `residue` decimal(10, 0) DEFAULT NULL COMMENT '剩余可用额度',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '账户表' ROW_FORMAT = Dynamic;
 
INSERT INTO `t_account` VALUES (1, 1, 1000, 0, 1000);
</code></pre>
<p><strong>3、新建事务回滚日志表：</strong><br>
上面新建的三个数据库都需要新建各自的回滚日志表。在三个业务数据库中都执行<code>seata-server-0.9.0\seata\conf\</code>目录下的<code>db_undo_log.sql</code>即可。</p>
<h1>四、实战之业务代码的编写</h1>
<p>业务需求：下订单 ---> 减库存 ---> 扣余额 ---> 改订单状态。<br>
<strong>1、新建订单模块seata-order-service2001：</strong></p>
<ul>
<li>pom.xml：主要是nacos、seata、openfeign和数据库连接那一套。</li>
</ul>
<pre><code> <!-- nacos -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
<!-- nacos -->
<!-- seata -->
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
    <exclusions>
        <exclusion>
            <groupId>io.seata</groupId>
            <artifactId>seata-all</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>io.seata</groupId>
    <artifactId>seata-all</artifactId>
    <version>0.9.0</version>
</dependency>
<!-- seata -->
<!--feign -->
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
</dependency>
<!-- druid-spring-boot-starter -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.1.22</version>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
<!--jdbc -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
</code></pre>
<ul>
<li>application.yml（主要是要注意tx-service-group的值要与nacos-config.txt和file.conf中的对应）：</li>
</ul>
<pre><code>server:
  port: 2001

spring:
  application:
    name: seata-order-service
  cloud:
    alibaba:
      seata:
        # 自定义事务组名称需要与seata-server中的对应
        tx-service-group: my_test_tx_group
    nacos:
      discovery:
        server-addr: 192.168.0.106:8848
  datasource:
    # 当前数据源操作类型
    type: com.alibaba.druid.pool.DruidDataSource
    # mysql驱动类
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://192.168.0.106:3306/seata_order?useUnicode=true&characterEncoding=UTF-8&useSSL=false&serverTimezone=GMT%2B8
    username: root
    password: zsl
feign:
  hystrix:
    enabled: false
logging:
  level:
    io:
      seata: info

mybatis:
  mapper-locations: classpath:mapper/*.xml
</code></pre>
<ul>
<li>seata配置文件：将seata/conf下的file.conf和registry.conf拷贝到application.yml的同级目录下。</li>
</ul>
<ul>
<li>CommonResult.java：</li>
</ul>
<pre><code>@Data
@AllArgsConstructor
@NoArgsConstructor
public class CommonResult<T> &#123;
    
    private Integer code;
    private String message;
    private T data;
&#125;
</code></pre>
<ul>
<li>Order.java：</li>
</ul>
<pre><code>@Data
@AllArgsConstructor
@NoArgsConstructor
public class Order &#123;
    
    private Long id;
    private Long userId;
    private Long productId;
    private Integer count;
    private BigDecimal money;
    private Integer status; // 0:创建中， 1:已完结

&#125;
</code></pre>
<ul>
<li>OrderDao.java：</li>
</ul>
<pre><code>@Mapper
public interface OrderDao &#123;
    /** 创建订单 */
    public void create(Order order);
    /** 修改订单状态 */
    public void update(@Param("userId") Long userId, @Param("status") Integer status);
&#125;
</code></pre>
<ul>
<li>OrderMapper.xml：</li>
</ul>
<pre><code><?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
    PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.zhusl.springcloud.dao.OrderDao">
  
   <insert id="create" parameterType="Order" useGeneratedKeys="true" keyProperty="id">
      insert into t_order(user_id, product_id, count, money, status) 
      values(#&#123;userId&#125;, #&#123;productId&#125;, #&#123;count&#125;, #&#123;money&#125;, 0);
   </insert>
   
   <update id="update">
      update t_order set status = 1 where user_id = #&#123;userId&#125; and status = #&#123;status&#125;;
   </update>
  
</mapper>
</code></pre>
<ul>
<li>OrderService.java：</li>
</ul>
<pre><code>public interface OrderService &#123;
    /** 创建订单 */
    public void create(Order order);
&#125;
</code></pre>
<ul>
<li>OrderServiceImpl.java：</li>
</ul>
<pre><code>@Service
@Slf4j
public class OrderServiceImpl implements OrderService&#123;
    
    @Autowired
    private OrderDao orderDao;
    @Autowired
    private StorageService storageService;
    @Autowired
    private AccountService accountService;

    @Override
    public void create(Order order) &#123;
        log.info("================= 新建订单start ==============");
        orderDao.create(order);
        log.info("================= 新建订单end ==============");
        
        log.info("================= 订单微服务调用库存微服务扣减库存start ==============");
        storageService.decrease(order.getProductId(), order.getCount());
        log.info("================= 订单微服务调用库存微服务扣减库存end ==============");
        
        log.info("================= 订单微服务调用账户微服务做扣减余额start ==============");
        accountService.decrease(order.getUserId(), order.getMoney());
        log.info("================= 订单微服务调用账户微服务做扣减余额end ==============");
        
        log.info("================= 修改订单状态start ==============");
        orderDao.update(order.getUserId(), 0);
        log.info("================= 修改订单状态end ==============");
        
        log.info("================= 下单完成✔ ==============");
        
    &#125;
&#125;
</code></pre>
<ul>
<li>StorageService.java：</li>
</ul>
<pre><code>@FeignClient(value = "seata-storage-service")
public interface StorageService &#123;

    /** 扣减库存 */
    @PostMapping("/storage/decrease")
    public CommonResult<?> decrease(@RequestParam("productId") Long id, @RequestParam("count") Integer count);
&#125;
</code></pre>
<ul>
<li>AccountService.java：</li>
</ul>
<pre><code>@FeignClient(value = "seata-account-service")
public interface AccountService &#123;

    /** 扣余额 */
    @PostMapping("/account/decrease")
    public CommonResult<?> decrease(@RequestParam("userId") Long userId, @RequestParam("money") BigDecimal money);
&#125;
</code></pre>
<ul>
<li>OrderController.java：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/order")
public class OrderController &#123;
    
    @Autowired
    private OrderService orderService;
    
    @GetMapping("/create")
    public CommonResult<?> create(Order order) &#123;
        orderService.create(order);
        return new CommonResult<>(200, "订单创建成功", null);
    &#125;
&#125;
</code></pre>
<ul>
<li>DataSourceProxyConfig.java：</li>
</ul>
<pre><code>package com.zhusl.springcloud.config;

import javax.sql.DataSource;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.transaction.SpringManagedTransactionFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import com.alibaba.druid.pool.DruidDataSource;

import io.seata.rm.datasource.DataSourceProxy;


/**
 * 使用seata对数据源进行代理
 * @author zhu
 *
 */
@Configuration
public class DataSourceProxyConfig &#123;

    @Value("$&#123;mybatis.mapperLocations&#125;")
    private String mapperLocations;
    
    @Bean
    @ConfigurationProperties(prefix = "spring.datasource")
    public DataSource druidDataSource() &#123;
        return new DruidDataSource();
    &#125;
    
    @Bean
    public DataSourceProxy dataSourceProxy(DataSource dataSource) &#123;
        return new DataSourceProxy(dataSource);
    &#125;
    
    @Bean
    public SqlSessionFactory sqlSessionFactoryBean(DataSourceProxy dataSourceProxy) throws Exception&#123;
        SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
        sqlSessionFactoryBean.setDataSource(dataSourceProxy);
        sqlSessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources(mapperLocations));
        sqlSessionFactoryBean.setTransactionFactory(new SpringManagedTransactionFactory());
        return sqlSessionFactoryBean.getObject();
    &#125;

&#125;
</code></pre>
<ul>
<li>主启动类：</li>
</ul>
<pre><code>@SpringBootApplication(exclude = DataSourceAutoConfiguration.class) // 取消数据源的自动创建，用自己配置的
@EnableDiscoveryClient
@EnableFeignClients
@MapperScan(&#123;"com.zhusl.springcloud.dao"&#125;)
public class App &#123;
    public static void main(String[] args) throws Exception &#123;
        SpringApplication.run(App.class, args);
    &#125;
&#125;
</code></pre>
<p>准备完成，现在依次启动nacos、seata和2001这个项目，最后项目控制台打印出如下日志并且在nacos中有seata和2001这两个服务表明启动成功。<br>
启动成功的日志：</p>
<pre><code>2020-06-05 11:29:12.393  INFO 74764 --- [           main] com.zhusl.springcloud.App                : Started App in 7.465 seconds (JVM running for 7.931)
2020-06-05 11:29:12.676  INFO 74764 --- [imeoutChecker_1] i.s.c.r.netty.NettyClientChannelManager  : will connect to 192.168.2.43:8091
2020-06-05 11:29:12.676  INFO 74764 --- [imeoutChecker_1] i.s.core.rpc.netty.NettyPoolableFactory  : NettyPool create channel to transactionRole:TMROLE,address:192.168.2.43:8091,msg:< RegisterTMRequest&#123;applicationId='seata-order-service', transactionServiceGroup='my_test_tx_group'&#125; >
2020-06-05 11:29:12.751  INFO 74764 --- [imeoutChecker_1] i.s.core.rpc.netty.NettyPoolableFactory  : register success, cost 71 ms, version:0.9.0,role:TMROLE,channel:[id: 0x9fe21753, L:/192.168.2.36:65186 - R:/192.168.2.43:8091]
</code></pre>
<p><strong><em>在配置启动过程中遇到了很多问题，大家可以去官网寻找解决方案。遇事不要慌，官网来帮忙。</em></strong><br>
<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fseata%2Fseata-samples" target="_blank">https://github.com/seata/seata-samples</a></p>
<p><strong>2、新建名为seata-storage-service2002的库存module:</strong></p>
<ul>
<li>pom.xml：和2001订单module的一模一样；</li>
<li>application.yml：端口改成2002，微服务名称改成seata-storage-service，连接的数据库改成seata_storage，其他的都和2001的一样；</li>
<li>把file.conf和registry.conf复制粘贴到application.yml的同级目录下；</li>
<li>Storage.java：</li>
</ul>
<pre><code>@Data
@AllArgsConstructor
@NoArgsConstructor
public class Storage &#123;

    private Long id;
    /** 产品id */
    private Long productId;
    /** 总库存 */
    private Integer total;
    /** 已用库存 */
    private Integer used;
    /** 剩余库存 */
    private Integer residue;
&#125;
</code></pre>
<ul>
<li>StorageDao.java：</li>
</ul>
<pre><code>@Mapper
public interface StorageDao &#123;
    /** 扣减库存 */
    void decrease(@Param("productId") Long productId, @Param("count") Integer count);
&#125;
</code></pre>
<ul>
<li>StorageMapper.xml：</li>
</ul>
<pre><code><?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
    PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.zhusl.springcloud.dao.StorageDao">
   <update id="decrease">
      update t_storage set used = used + #&#123;count&#125;, residue = residue - #&#123;count&#125; where product_id = #&#123;productId&#125;;
   </update>
</mapper>
</code></pre>
<ul>
<li>StorageServiceImpl.java：</li>
</ul>
<pre><code>@Service
@Slf4j
public class StorageServiceImpl implements StorageService &#123;
    @Autowired
    private StorageDao storageDao;
    @Override
    public void decrease(Long productId, Integer count) &#123;
        log.info("============== storageService 扣减库存 start =============");
        storageDao.decrease(productId, count);
        log.info("============== storageService 扣减库存 end =============");
    &#125;
&#125;
</code></pre>
<ul>
<li>StorageController.java：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/storage")
public class StorageController &#123;

    @Autowired
    private StorageService storageService;
    
    @PostMapping("/decrease")
    public CommonResult<?> decrease(Long productId, Integer count) &#123;
        storageService.decrease(productId, count);
        return new CommonResult<>(200, "扣减库存成功！", null);
    &#125;
&#125;
</code></pre>
<ul>
<li>最后数据源的配置和主启动类和都和2001的一样，复制粘贴即可。</li>
</ul>
<p><strong>3、新建名为seata-account-service2003的账户module：</strong></p>
<ul>
<li>pom.xml：和2001的一模一样；</li>
<li>application.yml：端口改为2003，服务名改成seata-account-service，连接的数据库改成seata_account；</li>
<li>复制粘贴file.conf和registry.conf到application.yml的同级目录；</li>
<li>Account.java：</li>
</ul>
<pre><code>@Data
@AllArgsConstructor
@NoArgsConstructor
public class Account &#123;
    private Long id;
    /** 用户id */
    private Long userId;
    /** 总额度 */
    private BigDecimal total;
    /** 已用额度 */
    private BigDecimal used;
    /** 剩余额度 */
    private BigDecimal residue;
&#125;
</code></pre>
<ul>
<li>AccountDao.java：</li>
</ul>
<pre><code>@Mapper
public interface AccountDao &#123;
    /** 扣减余额 */
    void decrease(@Param("userId") Long userId, @Param("money") BigDecimal money);
&#125;
</code></pre>
<ul>
<li>AccountMapper.xml：</li>
</ul>
<pre><code><?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
    PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.zhusl.springcloud.dao.AccountDao">
   <update id="decrease">
      update t_account set residue = residue - #&#123;money&#125;,used = used + #&#123;money&#125; where user_id = #&#123;userId&#125;;
   </update>
</mapper>
</code></pre>
<ul>
<li>AccountServiceImpl.java：</li>
</ul>
<pre><code>@Service
@Slf4j
public class AccountServiceImpl implements AccountService &#123;
    @Autowired
    private AccountDao accountDao;
    @Override
    public void decrease(Long userId, BigDecimal money) &#123;
        log.info("================ account-service 扣减余额 start ===============");
        accountDao.decrease(userId, money);
        log.info("================ account-service 扣减余额 end ===============");
    &#125;
&#125;
</code></pre>
<ul>
<li>AccountController.java：</li>
</ul>
<pre><code>@RestController
@RequestMapping("/account")
public class AccountController &#123;
    @Autowired
    private AccountService accountService;
    @PostMapping("/decrease")
    public CommonResult<?> decrease(Long userId, BigDecimal money) &#123;
        accountService.decrease(userId, money);
        return new CommonResult<>(200, "扣减余额成功!", null);
    &#125;
&#125;
</code></pre>
<ul>
<li>最后别忘记主启动类和数据源配置类。</li>
</ul>
<p><strong>4、测试：</strong><br>
3个module建完，先测试一下能否成功运行起来，先启动nacos，再启动seata，然后依次启动3个module。下面是3张表的初始情况：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="624" data-height="532"><img data-original-src="//upload-images.jianshu.io/upload_images/11531502-1e37f9bb3736b2e6.png" data-original-width="624" data-original-height="532" data-original-format="image/png" data-original-filesize="93493" src="https://upload-images.jianshu.io/upload_images/11531502-1e37f9bb3736b2e6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">数据库初始状态</div>
</div>
<p>现在模拟正常下单：<br>
<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A2001%2Forder%2Fcreate%3FuserId%3D1%26productId%3D1%26count%3D10%26money%3D100" target="_blank">http://localhost:2001/order/create?userId=1&productId=1&count=10&money=100</a><br>
访问之后，可能出现两种情况：</p>
<ul>
<li>返回成功信息，数据库成功的创建了一条订单，account和storage也成功的扣除了对应的数量。</li>
<li>openfeign报错，read timeout，成功创建了订单，但是account没有扣减。</li>
</ul>
<p>如果出现第二种情况，那也充分说明了目前这三个操作没有在一个事务里。如果你想不报错，不想让openfeign超时，加上在application.yml中加上如下配置即可：</p>
<pre><code>ribbon:
  ReadTimeout: 10000 #10秒应该就不会超时了
  ConnectTimeout: 10000
</code></pre>
<p>接下来我们在account的service里让线程睡11秒钟，虽然刚才openfeign设置了超时时间10秒，但是现在睡11秒，肯定还是会异常的。然后在OrderServiceImpl类上加上全局事务注解：</p>
<pre><code>@GlobalTransactional(name = "create-order", rollbackFor = Exception.class)
</code></pre>
<p>name随意，不冲突就好，rollbackFor表示什么情况下回滚，这里的意思是报异常了就回滚。</p>
<p>配置好之后，重新启动account和order这两个微服务，最后再次访问下订单的链接。就会发现报超时异常了，但是三个数据库的三张表都没有数据变化，即使全部都回滚了，这就表明分布式事务起作用了。</p>
<h1>五、关于seata的其他说明</h1>
<p>seata官网上说它支持AT、TCC、SAGA 和 XA 事务模式，我们用的是默认的AT模式。</p>
<p><strong>1、AT模式如何做到对业务无侵入的？</strong></p>
<ul>
<li>AT模式的前提：基于支持ACID事务的关系型数据库，通过JDBC访问数据库的java应用；</li>
<li>整体机制：两阶段提交协议。</li>
<li>一阶段：seata会拦截业务sql，找到业务要更新的数据，在被更新之前，将其保存为before image；执行业务sql，更新业务数据；在业务数据更新之后，将其保存为after image，最后生成行锁。一阶段的操作都在一个数据库事务内完成，保证了一阶段操作的原子性。这就类似spring的aop思想，前置通知和后置通知。</li>
<li>二阶段提交：如果顺利，二阶段就进行提交。因为一阶段已经执行过业务sql了，所以这里只需要将一阶段保存的before image、after image和行锁删除即可。</li>
<li>二阶段回滚：如果出异常了需要回滚，通过一阶段的回滚日志进行反向补偿。首先会比较当前库中数据和after image是否一致，如果一致，那么就将数据库中的数据还原成before image；如果不一致，说明数据出现过脏写，需要人工处理。</li>
</ul>
  
</div>
            