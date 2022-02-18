
---
title: 'fastmybatis 1.11.1 发布，mybatis 开发利器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1480'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 09:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1480'
---

<div>   
<div class="content">
                                                                                            <p>fastmybatis 1.11.1 发布，本次更新内容如下：</p> 
<p>mapper新增如下方法：</p> 
<ul> 
 <li><code>E getBySpecifiedColumns(List<String> columns, Query query)</code><span> </span>查询单条数据并返回指定字段</li> 
 <li><code><T> T getBySpecifiedColumns(List<String> columns, Query query, Class<T> clazz)</code><span> </span>查询单条数据并返回指定字段并转换到指定类中</li> 
 <li><code>List<E> listByIds(Collection<I> ids)</code><span> </span>根据多个主键值查询</li> 
 <li><code>T getColumnValue(String column, Query query, Class<T> clazz)</code><span> </span>查询某个字段值</li> 
 <li><code>List<T> listColumnValues(String column, Query query, Class<T> clazz)</code><span> </span>查询指定列，返指定列集合</li> 
 <li><code>int saveOrUpdate(E entity)</code><span> </span>保存或更新（所有字段）</li> 
 <li><code>int saveOrUpdateIgnoreNull(E entity)</code><span> </span>保存或更新（不为null的字段）</li> 
 <li><code>int deleteByIds(Collection<I> ids)</code><span> </span>根据多个主键id删除，在有逻辑删除字段的情况下，做UPDATE操作</li> 
 <li><code>int deleteByColumn(String column, Object value)</code><span> </span>根据指定字段值删除，在有逻辑删除字段的情况下，做UPDATE操作</li> 
 <li><code>int saveUnique(Collection<E> entitys)</code><span> </span>批量保存并去重</li> 
 <li> <p><code>int saveUnique(Collection<E> entitys, Comparator<E> comparator)</code><span> </span>批量保存并去重，指定比较器</p> </li> 
 <li> <p><code>新增BaseService</code>通用service</p> </li> 
 <li> <p><code>新增IService</code>通用接口</p> </li> 
</ul> 
<p><strong>查询单条数据并返回指定字段</strong></p> 
<p>有时候只想查询某一行某几列数据，</p> 
<pre><code class="language-java">Query query = new Query().eq("id", 6);
TUser tUser = mapper.getBySpecifiedColumns(Arrays.asList("id", "username"), query);</code></pre> 
<p>对应SQL:</p> 
<pre><em>SELECT id , username FROM `t_user` t WHERE id = 6 AND LIMIT 0,1</em></pre> 
<p>查询出来实体类对应的id，usernam字段是有数据的，其它字段为null，也可以转换成其它类：</p> 
<pre><em>UserVO userVo = mapper.getBySpecifiedColumns(Arrays.asList("id", "username"), query, UserVO.class);</em></pre> 
<p><strong>查询某个字段值</strong></p> 
<p>只查询某一行某一列数据</p> 
<pre><em>Query query = new Query().eq("id", 6);
String username = mapper.getColumnValue("username", query, String.class);</em></pre> 
<p>对应SQL:</p> 
<pre><em>SELECT username FROM `t_user` t WHERE id = 6 LIMIT 0,1</em></pre> 
<p>查询某一列多行数据，比如查询所有的username</p> 
<pre><em>// 年龄大于10岁的所有用户名
Query query = new Query().gt("age", 10);
List</em><em><String> username</em><em>List = mapper.listColumnValues("username", query, Integer.class);</em></pre> 
<p>对应SQL：</p> 
<pre><em>SELECT username FROM `t_user` t WHERE age > 10;</em>
</pre> 
<p><strong>通用Service类</strong></p> 
<p>本次新增了一个通用Service类，只需简单继承便具备所有的增删改查功能，使用方法如下：</p> 
<pre><span style="color:#bbb529">@Service
</span><span style="color:#cc7832">public class </span>UserService <span style="color:#cc7832">extends </span>BaseService<TUser<span style="color:#808080">/*</span><span style="color:#808080">实体类</span><span style="color:#808080">*/</span><span style="color:#cc7832">, </span>Integer<span style="color:#808080">/*</span><span style="color:#808080">主键类型</span><span style="color:#808080">*/</span><span style="color:#cc7832">, </span>TUserMapper<span style="color:#808080">/*Mapper*/</span>> &#123;

&#125;</pre> 
<p>如果Service已经继承了其它类，可以通过实现接口解决</p> 
<pre><span style="color:#cc7832">public class </span>UserService extends OtherService <span style="color:#cc7832">implements </span>IService<TUser<span style="color:#cc7832">, </span>Integer> &#123;

    @Autowired
    <span style="color:#cc7832">private </span>TUserMapper <span style="color:#9876aa">userMapper</span><span style="color:#cc7832">;
</span>
<span style="color:#cc7832">    </span><span style="color:#bbb529">@Override
</span><span style="color:#bbb529">    </span><span style="color:#cc7832">public </span>CrudMapper<TUser<span style="color:#cc7832">, </span>Integer> <span style="color:#ffc66d">getMapper</span>() &#123;
        <span style="color:#cc7832">return </span><span style="color:#9876aa">userMapper</span><span style="color:#cc7832">;
</span><span style="color:#cc7832">    </span>&#125;
&#125;
</pre> 
<p>controller增删改查例子：</p> 
<pre><code class="language-java">/**
 * 增删改查例子
 */
@RestController
public class CrudController &#123;

    @Autowired
    private UserService userService;


    /**
     * 分页查询
     * http://localhost:8080/user/page?id=10
     * http://localhost:8080/user/page?pageIndex=1&pageSize=5
     *
     * @param param
     * @return
     */
    @GetMapping("/user/page")
    public Result<PageInfo<TUser>> page(UserParam param) &#123;
        Query query = param.toQuery();
        PageInfo<TUser> pageInfo = userService.page(query);
        return Result.ok(pageInfo);
    &#125;

    /**
     * 新增记录，这里为了方便演示用了GET方法，实际上应该使用POST
     * http://localhost:8080/user/save?username=jim
     *
     * @param user
     * @return
     */
    @GetMapping("/user/save")
    public Result<Integer> save(TUser user) &#123;
        userService.saveIgnoreNull(user);
        // 返回添加后的主键值
        return Result.ok(user.getId());
    &#125;

    /**
     * 修改记录，这里为了方便演示用了GET方法，实际上应该使用POST
     * http://localhost:8080/user/update?id=10&username=jim
     *
     * @param user 表单数据
     * @return
     */
    @GetMapping("/user/update")
    public Result<?> update(TUser user) &#123;
        userService.updateIgnoreNull(user);
        return Result.ok();
    &#125;

    /**
     * 删除记录，这里为了方便演示用了GET方法，实际上应该使用DELETE
     * http://localhost:8080/user/delete?id=10
     *
     * @param id 主键id
     * @return
     */
    @GetMapping("/user/delete")
    public Result<?> delete(Integer id) &#123;
        userService.deleteById(id);
        return Result.ok();
    &#125;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>完整的Mapper方法 <a href="https://durcframework.gitee.io/fastmybatis/#/files/10011_Mapper%E8%AF%A6%E8%A7%A3?t=1645098153801" target="_blank">doc</a></strong></p> 
<table cellspacing="0" style="-webkit-font-smoothing:antialiased; -webkit-tap-highlight-color:rgba(0, 0, 0, 0); -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#34495e; display:block; font-family:"Source Sans Pro","Helvetica Neue",Arial,sans-serif; font-size:15px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:1rem; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-size-adjust:none; text-transform:none; white-space:normal; widows:2; width:1200.3px; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>方法</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>E getByColumn(String column, Object value)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据字段查询一条记录</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>E getById(I id)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据主键查询</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>E getByQuery(Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据条件查找单条记录</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>E getBySpecifiedColumns(List<String> columns, Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询单条数据并返回指定字段</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><T> T getBySpecifiedColumns(List<String> columns, Query query, Class<T> clazz)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询单条数据返回指定字段并转换到指定类中</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><T> T getColumnValue(String column, Query query, Class<T> clazz)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询某一行某个字段值</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>long getCount(Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询总记录数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>List<E> list(Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询结果集</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>List<E> listByArray(String column, Object[] values)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据多个字段值查询结果集</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>List<E> listByCollection(String column, Collection<?> values)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据字段多个值查询结果集</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>List<E> listByColumn(String column, Object value)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据字段查询结果集</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>List<E> listByIds(Collection<I> ids)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据多个主键查询</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>List<E> listBySpecifiedColumns(List<String> columns, Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询返回指定的列，返回实体类集合</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><T> List<T> listBySpecifiedColumns(List<String> columns, Query query, Class<T> clazz)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询返回指定的列，返指定类集合</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><T> List<T> listColumnValues(String column, Query query, Class<T> clazz)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询指定列，返指定列集合</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>PageInfo<E> page(Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">分页查询</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><R> PageInfo<R> page(Query query, Function<E, R> converter)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询结果集，并转换结果集中的记录，转换处理每一行</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><R> PageInfo<R> page(Query query, Supplier<R> target, Consumer<R> format)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询结果集，并转换结果集中的记录，并对记录进行额外处理</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><T> PageInfo<T> page(Query query, Supplier<T> target)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询结果集，并转换结果集中的记录</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><R> PageInfo<R> pageAndConvert(Query query, Function<List<E>, List<R>> converter)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询结果集，并转换结果集中的记录，转换处理list</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><T> PageInfo<T> pageBySpecifiedColumns(List<String> columns, Query query, Class<T> clazz)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询返回指定的列，返回分页数据</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>PageEasyui<E> pageEasyui(Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询返回easyui结果集</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code><T> PageEasyui<T> pageEasyui(Query query, Class<T> clazz)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">查询返回easyui结果集，并转换结果集中的记录</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>E forceById(I id)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据主键查询强制查询，忽略逻辑删除字段</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int save(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">保存，保存所有字段</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int saveBatch(Collection<E> entitys)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">批量保存</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int saveIgnoreNull(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">保存，忽略null字段</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int saveMultiSet(Collection<E> entitys)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">批量保存,兼容更多的数据库版本,忽略重复行，此方式采用union的方式批量insert</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int saveOrUpdate(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">保存或修改，当数据库存在记录执行UPDATE，否则执行INSERT</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int saveOrUpdateIgnoreNull(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">保存或修改，忽略null字段，当数据库存在记录执行UPDATE，否则执行INSERT</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int saveUnique(Collection<E> entitys)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">批量保存，去除重复行，通过对象是否相对判断重复数据，实体类需要实现equals方法</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int saveUnique(Collection<E> entitys, Comparator<E> comparator)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">批量保存，去除重复行，指定比较器判断</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int update(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">更新，更新所有字段</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int updateByQuery(E entity, Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据条件更新</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int updateIgnoreNull(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">更新，忽略null字段</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int updateByMap(Map<String, Object> map, Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据条件更新，map中的数据转化成update语句set部分，key为数据库字段名</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int delete(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">删除，在有逻辑删除字段的情况下，做UPDATE操作</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int deleteByColumn(String column, Object value)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据指定字段值删除，在有逻辑删除字段的情况下，做UPDATE操作</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int deleteById(I id)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据id删除，在有逻辑删除字段的情况下，做UPDATE操作</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int deleteByIds(Collection<I> ids)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据多个主键id删除，在有逻辑删除字段的情况下，做UPDATE操作</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int deleteByQuery(Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据条件删除，在有逻辑删除字段的情况下，做UPDATE操作</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int forceDelete(E entity)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">强制删除（底层根据id删除），忽略逻辑删除字段，执行DELETE语句</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int forceDeleteById(I id)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据id强制删除，忽略逻辑删除字段，执行DELETE语句</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><code>int forceDeleteByQuery(Query query)</code></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">根据条件强制删除，忽略逻辑删除字段，执行DELETE语句</td> 
  </tr> 
 </tbody> 
</table> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>关于fastmybatis</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">fastmybatis是一个mybatis开发框架，其宗旨为：简单、快速、有效。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>零配置快速上手</li> 
 <li>无需编写xml文件即可完成CRUD操作</li> 
 <li>支持mysql、sqlserver、oracle、postgresql、sqlite</li> 
 <li>支持自定义sql，对于基本的增删改查不需要写SQL，对于其它特殊SQL（如统计SQL）可写在xml中</li> 
 <li>支持与spring-boot集成，依赖starter即可</li> 
 <li>支持插件编写</li> 
 <li>轻量级，无侵入性，是官方mybatis的一种扩展</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            