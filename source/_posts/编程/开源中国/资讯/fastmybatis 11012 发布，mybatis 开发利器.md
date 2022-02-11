
---
title: 'fastmybatis 1.10.12 发布，mybatis 开发利器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7090'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 13:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7090'
---

<div>   
<div class="content">
                                                                                            <p>fastmybatis 1.10.12 发布，本次发布内容如下：</p> 
<ul> 
 <li>Query类新增条件表达式<code>query.eq(StringUtils.hasText(name), "name", name);</code></li> 
 <li>修复mysql下tinyint(1)返回boolean值问题</li> 
 <li>检查空字符串默认进行一次trim。<code>mybatis.empty-string-with-trim=true</code></li> 
 <li>查询字段忽略空字符调整为默认开启<code>mybatis.ignore-empty-string=true</code></li> 
</ul> 
<p>到1.10.12版本为止，fastmybatis实现多个有用的功能</p> 
<p><strong>将参数放在对象中查询</strong></p> 
<p>参数类，接收前端传递过来的请求参数</p> 
<pre><code>@Data
public class UserParam &#123;
/**
     * userId
     */
    @Condition(index = 0)
    private Integer userId;

/**
     * 用户名
     */
    @Condition(operator = Operator.like, index = 1)
    private String username;

    /**
     * 注册开始时间
     */
    @Condition(column = "reg_time", operator = Operator.ge, index = 2)
    private Date regBeginTime;

    /**
     * 注册结束时间
     */
    @Condition(column = "reg_time", operator = Operator.le, handlerClass = EndDateConditionValueHandler.class, index = 3)
    private Date regEndTime;
&#125;</code></pre> 
<p>controller类：</p> 
<pre><code class="language-java">// http://localhost:8080/listUser?userId=1&username=jim&regBeginTime=2021-11-12&regEndTime=2021-11-13
@GetMapping("listUser")
public List<TUser> listUser(UserParam userParam) &#123;
    Query query = Query.build(userParam);
    // SELECT id, username, reg_time FROM t_user 
    // WHERE user_id=? AND username LIKE '%?%' AND reg_time >= ? AND reg_time <= ?
    List<TUser> list = mapper.list(query);
    return list;
&#125;</code></pre> 
<p>Query.build会自动将请求参数封装成sql条件进行查询</p> 
<p><strong><span style="background-color:#ffffff; color:#34495e">对查询出来的结果做进一步加工</span></strong></p> 
<pre><code class="language-java">Query query = new Query();
    // 添加查询条件
    query.eq("username", "张三")
        .page(1, 2) // 分页查询，按页码分，通常使用这种。
    ;

    // 分页信息
    PageInfo<TUser> pageInfo = mapper.page(query, tUser -> &#123;
        // 对每行数据进行转换
        String username = tUser.getUsername();
        if ("张三".equals(username)) &#123;
            tUser.setUsername("法外狂徒");
        &#125;
        return tUser;
    &#125;);</code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><strong>返回指定字段</strong></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">有时候只需要查询几个字段，并不需要返回所有字段</p> 
<pre><code class="language-java">/**
 * 返回自定义字段，并转换成自定义类集合
 * 
 * <pre>
 * SELECT id, user_address FROM `t_user` t WHERE username = ?
 * </pre>
 */
@Test
public void testGivenColumns2() &#123;
    Query query = new Query();
    // 添加查询条件
    query.eq("username", "张三");

    // 数据库字段
    List<String> columns = Arrays.asList("id", "user_address");
    // 查询，自定义集合
    List<UserVO> list = mapper.listBySpecifiedColumns(columns, query, UserVO.class);

    for (UserVO obj : list) &#123;
        System.out.println(obj);
    &#125;
&#125;</code></pre> 
<p><strong>返回指定字段并分页</strong></p> 
<pre><code class="language-java">Query query = new Query()
        .eq("state", 0)
        .page(1, 6);
PageInfo<UserVO> mapPageInfo = mapper.pageBySpecifiedColumns(Arrays.asList("id", "username"), query, UserVO.class);
System.out.println(mapPageInfo);</code></pre> 
<p><strong><span style="background-color:#ffffff; color:#34495e">只返回一个字段</span></strong></p> 
<pre><code class="language-java">// 返回username列
List<String> usernameList = mapper.listBySpecifiedColumns(Collections.singletonList("username"), query, String.class);
for (String username : usernameList) &#123;
    System.out.println(username);
&#125;

// 返回时间列
List<Date> dateList = mapper.listBySpecifiedColumns(Collections.singletonList("add_time"), query, Date.class);
for (Date date : dateList) &#123;
    System.out.println(date);
&#125;

// 返回decimal列
List<BigDecimal> moneyList = mapper.listBySpecifiedColumns(Collections.singletonList("money"), query, BigDecimal.class);
for (BigDecimal money : moneyList) &#123;
    System.out.println(money);
&#125;</code></pre> 
<p><strong>格式化查询参数</strong></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">在做日期查询时，前端会传一个日期范围：开始日期、结束日期，如：<code>2022-02-01</code>、<code>2022-02-02</code>，此时对应数据库查询的日期范围是：<code>2022-02-01 00:00:00 ~ 2022-02-02 23:59:59</code></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">此时我们需要对结束时间做一下修改：</p> 
<pre><code class="language-java">public class EndDateConditionValueHandler implements ConditionValueHandler &#123;  

    public Object getConditionValue(Object defaultValue, String fieldName, Object target) &#123;
        if (defaultValue == null) &#123;
            return null;
        &#125; else if (defaultValue instanceof Date) &#123;
            // 设置时间部分
            return setHMS((Date)defaultValue, 23, 59, 59);
        &#125; else &#123;
            return defaultValue instanceof LocalDateTime ? setHMS((LocalDateTime)defaultValue, 23, 59, 59) : defaultValue;
        &#125;
    &#125;

    /**
     * 设置时间部分
     *
     * @param date   日期
     * @param hour   时，0~23
     * @param minute 分，0~59
     * @param second 秒，0~59
     * @return 返回新的对象
     */
    public static Date setHMS(Date date, int hour, int minute, int second) &#123;
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(date);
        calendar.set(Calendar.HOUR_OF_DAY, hour);
        calendar.set(Calendar.MINUTE, minute);
        calendar.set(Calendar.SECOND, second);
        calendar.set(Calendar.MILLISECOND, 0);
        return calendar.getTime();
    &#125;

    /**
     * 设置时间部分
     *
     * @param date   日期
     * @param hour   时，0~23
     * @param minute 分，0~59
     * @param second 秒，0~59
     * @return 返回新的对象
     */
    public static LocalDateTime setHMS(LocalDateTime date, int hour, int minute, int second) &#123;
        return date.withHour(hour).withMinute(minute).withSecond(second).withNano(0);
    &#125;
&#125;</code></pre> 
<p><span style="background-color:#ffffff; color:#34495e">然后使用</span></p> 
<pre><code>/**
 * 有效期，开始时间
 * @mock 2021-12-02
 */
@Condition(column = "begin_time", operator = Operator.ge, index = 2)
private Date effectiveBeginTime;

/**
 * 有效期，结束时间
 * @mock 2021-12-09
 */
@Condition(column = "end_time", operator = Operator.le, handlerClass = EndDateConditionValueHandler.class, index = 3)
private Date effectiveEndTime;</code></pre> 
<p>更多demo请参考：<a href="https://gitee.com/durcframework/fastmybatis/blob/master/fastmybatis-demo/fastmybatis-demo-springboot/src/test/java/com/myapp/TUserMapperTest.java" target="_blank">测试用例</a></p> 
<p><strong>关于fastmybatis</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">fastmybatis是一个mybatis开发框架，其宗旨为：简单、快速、有效。</p> 
<ul> 
 <li>零配置快速上手</li> 
 <li>无需编写xml文件即可完成CRUD操作</li> 
 <li>支持mysql、sqlserver、oracle、postgresql、sqlite</li> 
 <li>支持自定义sql，对于基本的增删改查不需要写SQL，对于其它特殊SQL（如统计SQL）可写在xml中</li> 
 <li>支持与spring-boot集成，依赖starter即可</li> 
 <li>支持插件编写</li> 
 <li>轻量级，无侵入性，是官方mybatis的一种扩展</li> 
</ul>
                                        </div>
                                      
</div>
            