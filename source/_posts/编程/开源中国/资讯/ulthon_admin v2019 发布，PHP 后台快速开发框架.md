
---
title: 'ulthon_admin v2.0.19 发布，PHP 后台快速开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9912'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 23:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9912'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>本次发行版中，优化了底层建设的代码，并实现了一个强大的特性（对我来说如此）：</p> 
 <ul> 
  <li>从数据库生成数据库迁移代码</li> 
 </ul> 
 <h2>用法</h2> 
 <h3>什么是数据库迁移工具</h3> 
 <p>ulthon_admin标准的安装流程是使用<code>数据库迁移工具</code>进行安装，他不仅可以安装到mysql数据库，也支持<code>sqlite</code>，<code>sqlserver</code>等其它数据库。</p> 
 <p>具体用法参考文档：</p> 
 <p><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.kancloud.cn%2Fmanual%2Fthinkphp6_0%2F1118028" target="_blank">https://www.kancloud.cn/manual/thinkphp6_0/1118028</a></p> 
 <p>但一般而言，我们开发中不会从写<code>迁移代码</code>开始，而是直接使用顺手的数据库工具（Dbeaver、Navcat等）设计数据库，然后在开发中修修补补。</p> 
 <p>这并没有什么不妥，但是如果你做的是一个标准产品，需要经常执行安装和更新，需要给多个客户部署时，就会感到吃力。</p> 
 <p>遇到这种情况，你只能从一个数据库导出，再导入到另一个数据库，反反复复的操作。还有可能不知道哪个是最新的，哪个需要更新，哪个更新到哪个版本了。</p> 
 <p>另一方面，如果数据库丢失了，而你手里又没有及时备份，那么也是很头疼的事。</p> 
 <p>数据库迁移工具就是为了解决以上种种问题的，比如我们需要新建一张<code>test_goods</code>数据表，我们可以使用数据库迁移工具，写出这样的代码：</p> 
 <div> 
  <pre><code><span><span><?php</span>

<span>use</span> <span>think</span>\<span>migration</span>\<span>Migrator</span>;
<span>use</span> <span>think</span>\<span>migration</span>\<span>db</span>\<span>Column</span>;

<span><span>class</span> <span>TestGoods</span> <span>extends</span> <span>Migrator</span>
</span>&#123;
    <span>public</span> <span><span>function</span> <span>change</span><span>()</span>
    </span>&#123;
        <span>$table</span> = <span>$this</span>->table(<span>'test_goods'</span>)
            ->setComment(<span>'商品列表'</span>)
            ->addColumn(<span>'cate_id'</span>, <span>'biginteger'</span>, [<span>'limit'</span> => <span>'20'</span>, <span>'signed'</span> => <span>'0'</span>, <span>'null'</span> => <span>'0'</span>, <span>'default'</span> => <span>'0'</span>, <span>'comment'</span> => <span>'分类ID &#123;relation&#125; (table:mall_cate,relationBindSelect:title)'</span>,])
            ->addColumn(<span>'title'</span>, <span>'char'</span>, [<span>'limit'</span> => <span>'20'</span>, <span>'null'</span> => <span>'0'</span>, <span>'default'</span> => <span>''</span>, <span>'comment'</span> => <span>'商品名称'</span>,])
            .......
            ->addColumn(<span>'detail'</span>, <span>'text'</span>, [<span>'null'</span> => <span>'1'</span>, <span>'comment'</span> => <span>'详情'</span>,])
            ->addIndex(<span>'uid'</span>, [<span>'unique'</span> => <span>true</span>])
            ->addIndex(<span>'detail'</span>, [<span>'type'</span> => <span>'fulltext'</span>])
            ->addIndex(<span>'cate_id'</span>)
            ->create();
    &#125;
&#125;

</span></code></pre> 
  <div>
    
  </div> 
 </div> 
 <p>然后运行命令：</p> 
 <div> 
  <pre><code>php think migrate:<span>run</span>
</code></pre> 
  <div>
    
  </div> 
 </div> 
 <p>此时这张表就出现在我们的数据库了，至于其他的表，并不会覆盖或丢失。</p> 
 <p>这样有很多好处：</p> 
 <ul> 
  <li>数据库跟随版本库存储不会丢失</li> 
  <li>没有反复多余的导出数据库</li> 
  <li>可以安装到“任何数据库”</li> 
  <li>任何标准产品都可以任意运行该命令用于升级数据库</li> 
 </ul> 
 <p>但是我们开发的时候，不会直接写数据迁移工具，而是从设计表开始。如果我们需要数据库迁移工具，就只能照着现在的数据表写迁移工具，这是以前的做法，也只能这样做。但是现在不一样了，通过一行命令可以一键生成数据库迁移的代码。就像生成curd那样。</p> 
 <p>现在按照我们的介绍看看怎么用吧。</p> 
 <h3>使用</h3> 
 <p>我们先用自己喜欢的方式设计出一张表。</p> 
 <div> 
  <pre><code><span>-- admin_demo_ultho.ul_test_goods definition</span>

<span><span>CREATE</span> <span>TABLE</span> <span>`ul_test_goods`</span> (
  <span>`id`</span> <span>int</span>(<span>11</span>) <span>NOT</span> <span>NULL</span> AUTO_INCREMENT,
  <span>`cate_id`</span> <span>bigint</span>(<span>20</span>) unsigned <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'0'</span> COMMENT <span>'分类ID &#123;relation&#125; (table:mall_cate,relationBindSelect:title)'</span>,
  <span>`title`</span> <span>char</span>(<span>20</span>) <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>''</span> COMMENT <span>'商品名称'</span>,
  <span>`logo`</span> <span>char</span>(<span>255</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'商品logo &#123;image&#125;'</span>,
  <span>`images`</span> <span>text</span> <span>NOT</span> <span>NULL</span> COMMENT <span>'商品图片 &#123;images&#125;'</span>,
  <span>`describe`</span> <span>text</span> <span>NOT</span> <span>NULL</span> COMMENT <span>'商品描述 &#123;editor&#125;'</span>,
  <span>`total_stock`</span> <span>int</span>(<span>11</span>) unsigned <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'0'</span> COMMENT <span>'总库存'</span>,
  <span>`sort`</span> <span>int</span>(<span>11</span>) unsigned <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'0'</span> COMMENT <span>'排序'</span>,
  <span>`status`</span> <span>int</span>(<span>1</span>) unsigned <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'0'</span> COMMENT <span>'状态 &#123;radio&#125; (0:正常,1:禁用)'</span>,
  <span>`cert_file`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'合格证 &#123;file&#125;'</span>,
  <span>`verfiy_file`</span> <span>text</span> <span>NOT</span> <span>NULL</span> COMMENT <span>'检测报告 &#123;files&#125;'</span>,
  <span>`remark`</span> <span>char</span>(<span>255</span>) <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>''</span> COMMENT <span>'备注说明'</span>,
  <span>`create_time`</span> <span>int</span>(<span>11</span>) unsigned <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'0'</span>,
  <span>`update_time`</span> <span>int</span>(<span>11</span>) unsigned <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'0'</span>,
  <span>`delete_time`</span> <span>int</span>(<span>11</span>) unsigned <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'0'</span>,
  <span>`publish_time`</span> <span>int</span>(<span>10</span>) unsigned <span>NOT</span> <span>NULL</span> COMMENT <span>'发布日期 &#123;date&#125; (date)'</span>,
  <span>`sale_time`</span> <span>bigint</span>(<span>20</span>) unsigned <span>NOT</span> <span>NULL</span> COMMENT <span>'售卖日期 &#123;date&#125; (datetime)'</span>,
  <span>`intro`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'简介 &#123;textarea&#125;'</span>,
  <span>`time_status`</span> <span>smallint</span>(<span>5</span>) unsigned <span>NOT</span> <span>NULL</span> COMMENT <span>'秒杀状态 &#123;select&#125; (0:未参加,1:已开始,3:已结束)'</span>,
  <span>`is_recommend`</span> tinyint(<span>4</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'是否推荐 &#123;switch&#125; (0:不推荐,1:推荐)'</span>,
  <span>`shop_type`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'商品类型 &#123;checkbox&#125; (taobao:淘宝,jd:京东)'</span>,
  <span>`tag`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'商品标签 &#123;table&#125; (table:mall_tag,type:checkbox,valueField:id,fieldName:title)'</span>,
  <span>`tag_backup`</span> <span>varchar</span>(<span>100</span>) <span>DEFAULT</span> <span>NULL</span> COMMENT <span>'商品标签（单选） &#123;table&#125; (table:mall_tag,type:radio,valueField:id,fieldName:title)'</span>,
  <span>`from_area`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'产地 &#123;city&#125; (name-province:0,code:0)'</span>,
  <span>`store_city`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> <span>DEFAULT</span> <span>'山东省/临沂市'</span> COMMENT <span>'仓库 &#123;city&#125; (level:city)'</span>,
  <span>`tag_input`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'商品标签 （输入） &#123;tag&#125;'</span>,
  <span>`uid`</span> <span>varchar</span>(<span>100</span>) <span>NOT</span> <span>NULL</span> COMMENT <span>'唯一id'</span>,
  <span>`price`</span> <span>decimal</span>(<span>10</span>,<span>2</span>) <span>DEFAULT</span> <span>NULL</span> COMMENT <span>'价格'</span>,
  <span>`detail`</span> longtext COMMENT <span>'详情'</span>,
  <span>PRIMARY</span> <span>KEY</span> (<span>`id`</span>),
  <span>UNIQUE</span> <span>KEY</span> <span>`ul_test_goods_uid_IDX`</span> (<span>`uid`</span>) <span>USING</span> BTREE,
  <span>KEY</span> <span>`cate_id`</span> (<span>`cate_id`</span>) <span>USING</span> BTREE,
  FULLTEXT <span>KEY</span> <span>`ul_test_goods_detail_IDX`</span> (<span>`detail`</span>)
) <span>ENGINE</span>=<span>InnoDB</span> AUTO_INCREMENT=<span>3</span> <span>DEFAULT</span> <span>CHARSET</span>=utf8 COMMENT=<span>'商品列表'</span>;</span>
</code></pre> 
  <div>
    
  </div> 
 </div> 
 <p>面对这样一张数据表，如果我们要对照写出数据库迁移工具的代码，会很费事，而且很容易就写错了。</p> 
 <p>但现在时代变了，只需要一行命令</p> 
 <div> 
  <pre><code>php think curd:migrate -t <span>test</span>_goods
</code></pre> 
  <div>
    
  </div> 
 </div> 
 <p>此时会在数据库迁移工具的工作目录下生成一个文件：</p> 
 <div> 
  <pre><code>database\migrations\<span>20220905222557</span>_test_goods<span>.php</span>
</code></pre> 
  <div>
    
  </div> 
 </div> 
 <blockquote> 
  <p>这跟使用官方的生成方式一致</p> 
 </blockquote> 
 <p>此时会直接生成开头那样的数据库迁移代码。</p> 
 <h2>结尾</h2> 
 <p>可能你没用过数据库迁移工具，那么目前可能无法引起你的兴趣，（建议使用），如果你正在使用，那么这个命令绝对能给你带来极大的便利。甚至可以让那些拥有几十个数据表的项目，也能轻松地使用数据库迁移工具来安装了。</p> 
 <p>ulthon_admin正在积极维护，拥有极高的定制性，支持依赖裁剪，精简代码，欢迎使用。</p> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            