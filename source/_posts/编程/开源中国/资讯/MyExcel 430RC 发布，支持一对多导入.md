
---
title: 'MyExcel 4.3.0.RC 发布，支持一对多导入'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/8674986/185737738-8952c7cb-cb6e-44d0-9b3e-2a159b2dbb85.png'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 07:30:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/8674986/185737738-8952c7cb-cb6e-44d0-9b3e-2a159b2dbb85.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel，是一个集导入、导出、加密 Excel 等多项功能的 Java 工具包。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MyExcel 采用声明式语法来构建、读取 Excel，屏蔽 POI 的具体操作细节（对 POI 无感知），以开发常用的技术替代，使得构建（从简单到高度复杂 Excel）以及读取 Excel 变得极为便利，且构建、读取性能极为优异，占用内存极低。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如导入：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>List<ArtCrowd> result = SaxExcelReader.of(ArtCrowd<span><span><span><span>.</span></span></span><span style="color:#d73a49"><span><span style="color:#d73a49"><span><span style="color:#d73a49"><span><span style="color:#d73a49">class</span></span></span></span></span></span></span><span><span><span>)</span></span></span></span>
        .sheet(<span><span><span><span><span><span><span>0</span></span></span></span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 0代表第一个sheet，如果为0，可省略该操作，也可sheet("名称")读取</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .rowFilter(row -> row.getRowNum() > <span><span><span><span><span><span><span>0</span></span></span></span></span></span></span>) <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 如无需过滤，可省略该操作，0代表第一行</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .detectedMerge() <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 识别合并单元格并填充数据，默认不识别</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>
        .read(path);</code></pre> 
<p><strong style="color:#333333">本次更新如下</strong><span style="background-color:#ffffff; color:#333333">：</span></p> 
<ul> 
 <li>修复DefaultExcelBuilder调用hideColumns无效问题；</li> 
 <li><span style="color:#e74c3c">SaxExcelReader支持一对多导入</span>；</li> 
 <li>调整DefaultStreamExcelBuilder等待队列长度，提升导出性能；</li> 
 <li>升级imageio-jpeg版本为3.8.2；</li> 
</ul> 
<p style="text-align:start"><strong>一对多导入示例</strong></p> 
<p style="text-align:start">示例1</p> 
<p><img alt="image" src="https://user-images.githubusercontent.com/8674986/185737738-8952c7cb-cb6e-44d0-9b3e-2a159b2dbb85.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-java">URL htmlToExcelEampleURL = this.getClass().getResource("/muilt_read.xlsx");
Path path = Paths.get(htmlToExcelEampleURL.toURI());

List<Grade> multiParents = SaxExcelReader.of(Grade.class)
        .rowFilter(row -> row.getRowNum() > 0)
        .detectedMerge() // 必须要调用识别合并单元格方法，否则无效
        .read(Files.newInputStream(path));

public class Grade &#123;
    @ExcelColumn(index=0)
    private String gradeName;

    @MultiColumn(classType=String.class)
    @ExcelColumn(index=1)
    private List<String> studentNames;

    @MultiColumn(classType=Integer.class)
    @ExcelColumn(index=2)
    private List<Integer> studentAges;
&#125;</code></pre> 
<p>示例2</p> 
<p><img alt="image" src="https://user-images.githubusercontent.com/8674986/185737738-8952c7cb-cb6e-44d0-9b3e-2a159b2dbb85.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-java">URL htmlToExcelEampleURL = this.getClass().getResource("/muilt_read.xlsx");
Path path = Paths.get(htmlToExcelEampleURL.toURI());

List<Grade> multiParents = SaxExcelReader.of(Grade.class)
        .rowFilter(row -> row.getRowNum() > 0)
        .detectedMerge() // 必须要调用识别合并单元格方法，否则无效
        .read(Files.newInputStream(path));

public class Grade &#123;
    @ExcelColumn(index=0)
    private String gradeName;

    @MultiColumn(classType=Student.class)
    private List<Student> students;
&#125;

public class Student &#123;
   @ExcelColumn(index=1)
   private String name;

   @ExcelColumn(index=2)
   private Integer age;
&#125;</code></pre> 
<p>示例3</p> 
<p><img alt="image" src="https://user-images.githubusercontent.com/8674986/185738600-d97fd041-0393-4f69-a1ae-daae94d7f7f2.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<pre><code class="language-java">URL htmlToExcelEampleURL = this.getClass().getResource("/muilt_read.xlsx");
Path path = Paths.get(htmlToExcelEampleURL.toURI());

List<School> multiParents = SaxExcelReader.of(School.class)
        .rowFilter(row -> row.getRowNum() > 0)
        .detectedMerge() // 必须要调用识别合并单元格方法，否则无效
        .read(Files.newInputStream(path));

public class School &#123;
    @ExcelColumn(index=0)
    private String name;

    @MultiColumn(classType=Grade.class)
    private List<Grade> grades;
&#125;

public class Grade &#123;
    @ExcelColumn(index=1)
    private String gradeName;

    @MultiColumn(classType=Student.class)
    private List<Student> students;
&#125;

public class Student &#123;
   @ExcelColumn(index=2)
   private String name;

   @ExcelColumn(index=3)
   private Integer age;
&#125;</code></pre> 
<p><span style="background-color:#ffffff; color:#333333">具体，请移步文档</span><span style="background-color:#ffffff; color:#333333">：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliaochong%2Fmyexcel%2Fwiki" target="_blank">https://github.com/liaochong/myexcel/wiki</a></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bf0dcbd14b9df24356a206ff40878aaec30.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            