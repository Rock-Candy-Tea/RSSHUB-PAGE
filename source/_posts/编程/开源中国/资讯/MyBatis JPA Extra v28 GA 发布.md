
---
title: 'MyBatis JPA Extra v2.8 GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9457'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 10:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9457'
---

<div>   
<div class="content">
                                                                                            <p>MyBatis JPA Extra</p> 
<p><strong>MyBatis JPA Extra</strong>对MyBatis扩展JPA功能    </p> 
<p>1.JPA 2.1注释<strong>简化CUID操作</strong>;    </p> 
<p>2.Interceptor实现数据库<strong>SELECT分页查询</strong>;    </p> 
<p>3.<strong>链式</strong>Query查询条件构造器;</p> 
<p>4.提供starter,<strong>简化SpringBoot集成</strong>;</p> 
<h2>1、JPA 2.1注释</h2> 
<h2>1.1、注释</h2> 
<p>仅支持6个注释</p> 
<blockquote> 
 <ul> 
  <li><a href="https://my.oschina.net/u/1260961" target="_blank">@Entity</a></li> 
  <li><a href="https://my.oschina.net/u/2493882" target="_blank">@Table</a></li> 
  <li><a href="https://my.oschina.net/u/1218" target="_blank">@Column</a></li> 
  <li><a href="https://my.oschina.net/u/3451001" target="_blank">@Id</a></li> 
  <li>@GeneratedValue</li> 
  <li>@Transient</li> 
 </ul> 
</blockquote> 
<h2>1.2、主键策略</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>序号</th> 
   <th>策略</th> 
   <th>支持</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><strong>AUTO</strong></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4种主键自动填充策略<br> snowflakeid(雪花ID-推荐)<br> uuid(UUID)<br> uuid.hex(UUID十六进制)<br> serial(JPA Extra序列)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><strong>SEQUENCE</strong></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">数据库序列生成，generator值为数据库序列名</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><strong>IDENTITY</strong></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">数据库表自增主键</td> 
  </tr> 
 </tbody> 
</table> 
<h2>1.3、Java Bean 注释</h2> 
<pre><code class="language-java">
@Entity
@Table(name = "STUDENTS")  
public class Students extends JpaBaseEntity implements Serializable&#123;
   
    @Id
    @Column
    @GeneratedValue(strategy=GenerationType.AUTO,generator="snowflakeid")
    //@GeneratedValue(strategy=GenerationType.SEQUENCE,generator="SEQ_MYBATIS_STUD")
    //@GeneratedValue(strategy=GenerationType.IDENTITY)
    private String id;
   
    @Column
    private String stdNo;
   
    @Column
    private String stdName;
   
    @Column
    private String stdGender;
   
    @Column
    private int stdAge;
   
    @Column
    private String stdMajor;
   
    @Column
    private String stdClass;
   
    @Column
    private byte[] images;
   
    public Students() &#123;&#125;

    public get()&#123;&#125;;
    public void set()&#123;&#125;;
    //...
&#125;

</code></pre> 
<h2>2、基本操作</h2> 
<h2>2.1、CURD</h2> 
<pre><code class="language-java">    //新增数据
    @Test
    public void insert() throws Exception&#123;
        _logger.info("insert...");
        Students student=new Students();
        student.setStdNo("10024");
        student.setStdGender("M");
        student.setStdName("司马昭");
        student.setStdAge(20);
        student.setStdMajor("政治");
        student.setStdClass("4");
        service.insert(student);
       
        Thread.sleep(1000);
        _logger.info("insert id " + student.getId());
    &#125;
   
    //查询数据实体并更新
    @Test
    public void update() throws Exception&#123;
        _logger.info("get...");
        Students student=service.get("317d5eda-927c-4871-a916-472a8062df23");
        System.out.println("Students "+student);
         _logger.info("Students "+student);
         _logger.info("update...");
         student.setImages(null);
         service.update(student);
         _logger.info("updateed.");
         
         student.setImages("ssss".getBytes());
         service.update(student);
         _logger.info("updateed2.");
    &#125;
   
    //根据实体查询并更新
    @Test
    public void merge() throws Exception&#123;
        _logger.info("merge...");
        Students student=new Students();
        //student.setId("10024");
        student.setStdNo("10024");
        student.setStdGender("M");
        student.setStdName("司马昭");
        student.setStdAge(20);
        student.setStdMajor("政治");
        student.setStdClass("4");
        service.merge(student);
       
        Thread.sleep(1000);
        _logger.info("merge id " + student.getId());
    &#125;

    //根据ID查询
    @Test
    public void get() throws Exception&#123;
        _logger.info("get...");
        Students student=service.get("317d5eda-927c-4871-a916-472a8062df23");
        System.out.println("Students "+student);
         _logger.info("Students "+student);
    &#125;
   
    //根据实体查询
    @Test
    public void query() throws Exception&#123;
        _logger.info("query...");
        Students student=new Students();
        student.setStdGender("M");
        List<Students> listStudents =service.query(student);
        //...
    &#125;

    //查询所有记录
    @Test
    public void findAll() throws Exception&#123;
        _logger.info("findAll...");
        List<Students> listStudents =service.findAll();
        //...
    &#125;

    //根据ID删除
    @Test
    public void remove() throws Exception&#123;
        _logger.info("remove...");
        service.remove("921d3377-937a-4578-b1e2-92fb23b5e512");
    &#125;
   
    //根据ID集合批量删除
    @Test
    public void batchDelete() throws Exception&#123;
        _logger.info("batchDelete...");
        List<String> idList=new ArrayList<String>();
        idList.add("8584804d-b5ac-45d2-9f91-4dd8e7a090a7");
        idList.add("ab7422e9-a91a-4840-9e59-9d911257c918");
        idList.add("12b6ceb8-573b-4f01-ad85-cfb24cfa007c");
        idList.add("dafd5ba4-d2e3-4656-bd42-178841e610fe");
        service.deleteBatch(idList);
    &#125;
   
    //根据ID批量逻辑删除
    @Test
    public void logicDelete() throws Exception&#123;
        _logger.info("logicDelete...");
        List<String> idList=new ArrayList<String>();
        idList.add("8584804d-b5ac-45d2-9f91-4dd8e7a090a7");
        idList.add("ab7422e9-a91a-4840-9e59-9d911257c918");
        idList.add("12b6ceb8-573b-4f01-ad85-cfb24cfa007c");
        idList.add("dafd5ba4-d2e3-4656-bd42-178841e610fe");
        service.logicDelete(idList);
    &#125;

    //根据ID批量删除
    @Test
    public void batchDeleteByIds() throws Exception&#123;
        _logger.info("batchDeleteByIds...");
        service.deleteBatch("2");
        service.deleteBatch("2,639178432667713536");
    &#125;

</code></pre> 
<h2>2.2、Find查询和Qruey构造器</h2> 
<pre><code class="language-java">    //springJDBC 的查询方式
    @Test
    public void find() throws Exception&#123;
        _logger.info("find by filter StdNo = '10024' or StdNo = '10004'");
        List<Students> listStudents = service.find(" StdNo = ? or StdNo = ?  ",
                            new Object[]&#123;"10024","10004"&#125;,
                            new int[]&#123;Types.VARCHAR,Types.INTEGER&#125;
                        );
        //...
    &#125;

    //根据链式条件构造器查询
    //WHERE (stdMajor = '政治' and STDAGE > 30 and stdMajor in ( '政治' , '化学' )  or  ( stdname = '周瑜' or stdname = '吕蒙' ) )
    @Test
    public void filterByQuery() throws Exception&#123;
        _logger.info("filterByQuery...");
        List<Students> listStudents = service.query(
                new Query().eq("stdMajor", "政治").and().gt("STDAGE", 30).and().in("stdMajor", new Object[]&#123;"政治","化学"&#125;)
                .or(new Query().eq("stdname", "周瑜").or().eq("stdname", "吕蒙")));
        //...
    &#125;

</code></pre> 
<h2>2.3、分页查询并count数据量</h2> 
<pre><code class="language-java">    //根据实体分页查询
    @Test
    public void queryPageResults() throws Exception&#123;
        _logger.info("queryPageResults...");
         Students student=new Students();
         //student.setStdGender("M");
         //student.setStdMajor(政治");
         student.setPageSize(10);
         //student.setPageNumber(2);
         student.calculate(21);
         JpaPageResults<Students>  results = service.queryPageResults(student);
         List<Students> rowsStudents = results.getRows();
         long records =results.getRecords();//当前页记录数量
         long totalPage =results.getTotalPage();//总页数
         long total =results.getTotal();//总数据量
         long page =results.getPage();//当前页
        //...
    &#125;

    //mapper id分页查询
    @Test
    public void queryPageResultsByMapperId() throws Exception&#123;
        _logger.info("queryPageResults by mapperId...");
         Students student=new Students();
         student.setStdGender("M");
         //student.setStdMajor(政治");
         student.setPageSize(10);
         student.setPageNumber(2);
         JpaPageResults<Students>  results =
                 service.queryPageResults("queryPageResults1",student);
        //...
    &#125;

</code></pre> 
<h2>3、版本更新</h2> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">新增链式Query查询条件构造器</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">底层代码的优化和整合</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">完善readme</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">统一jar包版本配置</p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">升级相关的jar包</p>
                                        </div>
                                      
</div>
            