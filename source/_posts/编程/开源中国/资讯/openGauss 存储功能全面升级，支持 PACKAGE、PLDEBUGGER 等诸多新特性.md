
---
title: 'openGauss 存储功能全面升级，支持 PACKAGE、PLDEBUGGER 等诸多新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=150'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 13:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=150'
---

<div>   
<div class="content">
                                                                    
                                                        <ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">存储过程类似于面向过程语言当中的函数，可以实现面向过程语言当中的声明变量、逻辑判断、条件循环等操作，是一组完成特定功能的SQL语句集合。</p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在 openGauss 2.1 之前的版本中，存储过程支持了定义变量、条件循环、逻辑判断等基本功能，但是没有面向对象语言中类的形式，因此无法对存储过程中的变量以及函数进行封装，也无法在存储过程内使用全局变量。在以前的版本中没有支持类似gdb的功能，用户调试存储过程只能够使用raise info等打印变量的方式。并且在之前的版本当中，存储过程发生异常后，没有自治事务，记录错误日志不便。</p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">而在新的版本当中，通过支持 PACKAGE、存储过程调试/PLDEBUGGER、自治事务等新功能，解决了上述问题。下面将介绍新特性的应用场景以及使用方法。</p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><strong>特性一：PACKAGE</strong></p> 
<p style="margin-left:0; margin-right:0">package是一组相关存储过程、函数、变量、常量、游标等PL/SQL程序的组合，具有面向对象的特点，可以对PL/SQL程序设计元素进行封装。package中的函数具有统一性，创建、删除、修改都统一进行。</p> 
<p style="margin-left:0; margin-right:0">package包含包头（Package Specification）和Package Body两个部分，其中包头所包含的声明可以被外部函数、匿名块等访问，而在包体中包含的声明不能被外部函数、匿名块等访问，只能被包体内函数和存储过程等访问。</p> 
<p style="margin-left:0; margin-right:0">下面可以看一组简单的例子理解一下：</p> 
<pre><code>
CREATE TABLE tab1(col1 int);
CREATE OR REPLACE PACKAGE PCK1 --包头，在包头内声明的变量存储过程等都为公有的，可以被外部访问
IS
public_var1 int:=1; --在包头声明的公有变量public_var1，可以被外部访问
procedure public_proc1(col1 int,col2 int); --只在包头内声明的存储过程，因此为公有的，可以被外部访问。
END PCK1;
/

CREATE OR REPLACE PACKAGE BODY PCK1 --指定了PACKAGE BODY关键字
IS
private_var1 int:=1; --在包体内声明的私有变量private_var1,不能被外部访问
procedure private_proc1(col1 int,col2 int) --只在包体内定义的存储过程为私有存储过程
is
begin
raise notice 'col1 + col2 = %',col1+col2;
insert into tab1 values(col1+col2);
end;
procedure public_proc1(col1 int,col2 int)--只在包体内定义的存储过程为私有存储过程
is
begin
private_proc1(1,2);
end;
--需与包头保持一致
END PCK1;
/
> --package中的函数调用方式与存储过程调用方式一样
> call pck1.public_proc1(1,2);</code></pre> 
<p style="margin-left:0; margin-right:0"><strong>特性二、PLDEBUGGER</strong></p> 
<p style="margin-left:0; margin-right:0">DBE_PLDEBUGGER用于调试存储过程，类似于GDB的功能，可以使用单步调试，设置断点、打印调用堆栈等功能，方便了存储过程的调试，减小了存储过程的开发难度。详细的使用方法以及说明可以参考在本文末提供的 [PLDEBUGGER接口及示例]</p> 
<p style="margin-left:0; margin-right:0"><strong>特性三、自治事务</strong></p> 
<p style="margin-left:0; margin-right:0">自治事务（Autonomous Transaction），在主事务执行过程中新启的独立的事务。自治事务的提交和回滚不会影响主事务已提交的数据，同时自治事务也不受主事务影响。</p> 
<p style="margin-left:0; margin-right:0">自治事务在存储过程、函数和匿名块中定义，用PRAGMA AUTONOMOUS_TRANSACTION关键字来声明。</p> 
<p style="margin-left:0; margin-right:0">自治事务一般用于存储过程发生异常后，处理日志的时候。</p> 
<p style="margin-left:0; margin-right:0">下面可以看一个简单的示例：</p> 
<pre><code>create table t2(a int, b int);
insert into t2 values(1,2);
select * from t2;
 
--创建包含自治事务的存储过程
CREATE OR REPLACE PROCEDURE autonomous_proc1(a int, b int)  AS 
DECLARE 
    num3 int := a;
    num4 int := b;
    PRAGMA AUTONOMOUS_TRANSACTION; --声明此存储过程为一个自治事务的存储过程
BEGIN
    insert into t2 values(num3, num4); 
    dbe_output.print_line('just use call.');
END;
/
 --创建调用自治事务存储过程的普通存储过程
CREATE OR REPLACE PROCEDURE proc1(a int, b int)  AS 
DECLARE 
c int:=0;
BEGIN
    dbe_output.print_line('just no use call.');
    insert into t2 values(5, 6);--异常后回滚
    c:=c/0;
    exception when others then
    autonomous_proc1(a,b);
END;
/
--调用普通存储过程
select proc1(11,22);
select * from t2 order by a;
输出结果：
a  | b  
----+----
1 |  2
11 | 22
(2 rows)</code></pre> 
<p style="margin-left:0; margin-right:0"><strong>pldebugger 接口及示例</strong></p> 
<table cellspacing="0" style="border-collapse:collapse; box-sizing:border-box !important; display:table; margin:0px 0px 10px; max-width:100%; outline:0px; overflow-wrap:break-word !important; padding:0px; width:677px"> 
 <tbody> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center"><strong>接口名称</strong></p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center"><strong>描述</strong></p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.turn_on</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">server端调用，标记存储过程可以调试，调用后执行该存储过程时会hang住等待调试信息。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.turn_off </p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">server端调用，标记存储过程关闭调试。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.local_</p> <p style="margin-left:0px; margin-right:0px; text-align:center">debug_server_info</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">server端调用，打印本session内所有已turn_on的存储过程。 </p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.attach</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，关联到正在调试存储过程。  </p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.info_locals </p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，打印正在调试的存储过程中的变量当前值。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.next</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，单步执行。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.continue </p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，继续执行，直到断点或存储过程结束。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.abort</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，停止调试，server端报错长跳转。  </p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.print_var </p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，打印正在调试的存储过程中指定的变量当前值。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.info_code</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug和server端都可以调用，打印指定存储过程的源语句和各行对应的行号。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.step</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，单步进入执行。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.add_</p> <p style="margin-left:0px; margin-right:0px; text-align:center">breakpoint</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，新增断点。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.delete_</p> <p style="margin-left:0px; margin-right:0px; text-align:center">breakpoint</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，删除断点。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.info_</p> <p style="margin-left:0px; margin-right:0px; text-align:center">breakpoint </p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，查看当前的所有断点。 </p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.backtrace</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，查看当前的调用栈。 </p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.enable_</p> <p style="margin-left:0px; margin-right:0px; text-align:center">breakpoint</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，激活被禁用的断点。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.disable_</p> <p style="margin-left:0px; margin-right:0px; text-align:center">breakpoint </p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，禁用已激活的断点</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.finish</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，继续调试，直到断点或返回上一层调用栈。</p> </td> 
  </tr> 
  <tr> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">DBE_PLDEBUGGER.set_var</p> </td> 
   <td colspan="1" rowspan="1" style="border-color:#959baa; border-style:solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">debug端调用，为变量进行赋值操作。</p> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:0; margin-right:0"><strong>示例</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">准备调试</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">通过PG_PROC，查找到待调试存储过程的oid，并执行DBE_PLDEBUGGER.turn_on(oid)。本客户端就会作为server端使用</p> 
<pre><code>CREATE OR REPLACE PROCEDURE test_debug ( IN  x INT) 
AS  
BEGIN
    INSERT INTO t1 (a) VALUES (x);
    DELETE FROM t1 WHERE a = x;
END;
/
输出结果:
CREATE PROCEDURE
SELECT OID FROM PG_PROC WHERE PRONAME='test_debug';
输出结果：
  oid
-------
 16389
(1 row)
 
SELECT * FROM DBE_PLDEBUGGER.turn_on(16389);
输出结果：
 nodename | port
----------+------
 datanode |    0
(1 row)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">开始调试</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">server端执行存储过程，会在存储过程内第一条SQL语句前hang住，等待debug端发送的调试消息。仅支持直接执行存储过程的调试，不支持通过trigger调用执行的存储过程调试。</p> 
<pre><code>call test_debug(1);</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">再起一个客户端，作为debug端，通过turn_on返回的数据，调用DBE_PLDEBUGGER.attach关联到该存储过程上进行调试。</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.attach('datanode',0);
输出结果：
 funcoid |  funcname  | lineno |              query
---------+------------+--------+----------------------------------
   16389 | test_debug |      3 |   INSERT INTO t1 (a) VALUES (x);
(1 row)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在执行 attach 的客户端调试，执行下一条 statement。</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.next();
输出结果：
 funcoid |  funcname  | lineno |        query
---------+------------+--------+----------------------
   16389 | test_debug |      0 | [EXECUTION FINISHED]
(1 row)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">在执行 attach 的客户端调试，可以执行以下变量操作</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.info_locals(); --打印全部变量
输出结果：
 varname | vartype | value | package_name | isconst
---------+---------+-------+--------------+---------
 x       | int4    | 1     |              | f
(1 row)

SELECT * FROM DBE_PLDEBUGGER.set_var('x', 2); --变量赋值
输出结果：
 set_var
---------
 t
(1 row)

SELECT * FROM DBE_PLDEBUGGER.print_var('x'); --打印单个变量
输出结果：
 varname | vartype | value | package_name | isconst
---------+---------+-------+--------------+---------
 x       | int4    | 2     |              | f
(1 row)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">直接执行完成当前正在调试的存储过程。</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.continue();
输出结果：
 funcoid |  funcname  | lineno |        query
---------+------------+--------+----------------------
   16389 | test_debug |      0 | [EXECUTION FINISHED]
(1 row)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">直接退出当前正在调试的存储过程，不执行尚未执行的语句。</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.abort();
输出结果：
 abort
-------
 t
(1 row)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">client端查看代码信息并识别可以设置断点行号。</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.info_code(16389);
输出结果：
 lineno |                           query                           | canbreak
--------+-----------------------------------------------------------+----------
        | CREATE OR REPLACE PROCEDURE public.test_debug( IN  x INT) | f
      1 | AS  DECLARE                                               | f
      2 | BEGIN                                                     | f
      3 |     INSERT INTO t1 (a) VALUES (x);                        | t
      4 |     DELETE FROM t1 WHERE a = x;                           | t
      5 | END;                                                      | f
      6 | /                                                         | f
(7 rows)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">设置断点</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.info_breakpoints();
输出结果：
 breakpointno | funcoid | lineno |              query              | enable
--------------+---------+--------+---------------------------------+--------
            0 |   16389 |      4 |     DELETE FROM t1 WHERE a = x; | t</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">查看断点信息</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.info_breakpoints();
输出结果：
 breakpointno | funcoid | lineno |              query              | enable
--------------+---------+--------+---------------------------------+--------
            0 |   16389 |      4 |     DELETE FROM t1 WHERE a = x; | t
(1 row)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">执行至断点</p> </li> 
</ul> 
<pre><code>SELECT * FROM DBE_PLDEBUGGER.continue();
输出结果：
 funcoid |  funcname  | lineno |              query
---------+------------+--------+---------------------------------
   16389 | test_debug |      4 |     DELETE FROM t1 WHERE a = x;</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            