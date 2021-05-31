
---
title: 'mybatis-plus-generator 3.5.0 发布，CRUD 代码也不用写了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9883'
author: 开源中国
comments: false
date: Mon, 31 May 2021 09:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9883'
---

<div>   
<div class="content">
                                                                    
                                                        <h3>mybatis-plus-generator 3.5.0 发布，该版本为重构版本，可能存在部分历史API不兼容情况，本次主要升级内容为简化配置链式操作。</h3> 
<h2><a href="https://gitee.com/baomidou/generator">源码仓库</a></h2> 
<p>H2 生成代码示例：</p> 
<blockquote> 
 <p>new SimpleAutoGenerator() &#123;<br>     @Override<br>     public IConfigBuilder<DataSourceConfig> dataSourceConfigBuilder() &#123;<br>         return new DataSourceConfig.Builder("jdbc:h2:mem:test;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE;CASE_INSENSITIVE_IDENTIFIERS=TRUE",<br>         "sa", "");<br>     &#125;<br> &#125;.execute();</p> 
</blockquote> 
<h1>升级日志</h1> 
<ul> 
 <li>优化代码重构核心构建方式</li> 
 <li>修复swagger注释包含双引号生成代码错误</li> 
 <li>swagger2 修改为 swagger 避免以为支持 swagger2 版本</li> 
 <li>修复生成驼峰命名属性字段转换错误</li> 
 <li>修复mysql自动生成代码类型错误(bit,year类型)</li> 
 <li>修复h2数据库主键自增判断错误</li> 
 <li>修复无乐观锁或逻辑删除字段导入多余的包</li> 
 <li>修复Oscar（神通数据库）生成错误</li> 
 <li>修复高斯数据库生成错误</li> 
 <li>修复SQLServer日期生成错误</li> 
 <li>增加虚谷数据库代码生成支持</li> 
 <li>增加ClickHouse代码生成支持</li> 
 <li>支持Beetl模板3.2.x版代码生成</li> 
 <li>去除PG中不包含的clob、blob类型，二进制类型调整为byte类型</li> 
 <li>支持PostgreSql大写表名</li> 
 <li>支持基于模型属性字段填充</li> 
 <li>支持通过数据源构建DataSourceConfig</li> 
 <li>velocity提示1.x版本依赖过时，输出日志警告信息</li> 
 <li>表的主键为自增主键时会导致全局主键的ID类型设置生效，输出日志警告信息</li> 
 <li>移除lombok依赖</li> 
 <li>优化 Jdbc 连接关闭逻辑</li> 
 <li>PackageConfig,DataSourceConfig,GlobalConfig,StrategyConfig,TemplateConfig更改为构建者模式.</li> 
 <li>Entity 新增 ignoreColumns 支持忽略指定字段不生成</li> 
 <li>文本输入 scanner 读取 next 修改为 nextLine</li> 
</ul>
                                        </div>
                                      
</div>
            