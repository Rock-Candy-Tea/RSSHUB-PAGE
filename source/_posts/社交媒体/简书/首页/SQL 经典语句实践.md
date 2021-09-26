
---
title: 'SQL 经典语句实践'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://picsum.photos/400/300?random=6747'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=6747'
---

<div>   
<h5>每天进步一点点~ (●'◡'●)~</h5>
<h4>01 建表语句</h4>
<pre><code>create table Student(sid varchar(10),sname varchar(10),sage datetime,ssex nvarchar(10));
insert into Student values('01' , '赵雷' , '1990-01-01' , '男');
insert into Student values('02' , '钱电' , '1990-12-21' , '男');
insert into Student values('03' , '孙风' , '1990-05-20' , '男');
insert into Student values('04' , '李云' , '1990-08-06' , '男');
insert into Student values('05' , '周梅' , '1991-12-01' , '女');
insert into Student values('06' , '吴兰' , '1992-03-01' , '女');
insert into Student values('07' , '郑竹' , '1989-07-01' , '女');
insert into Student values('08' , '王菊' , '1990-01-20' , '女');
create table Course(cid varchar(10),cname varchar(10),tid varchar(10));
insert into Course values('01' , '语文' , '02');
insert into Course values('02' , '数学' , '01');
insert into Course values('03' , '英语' , '03');
create table Teacher(tid varchar(10),tname varchar(10));
insert into Teacher values('01' , '张三');
insert into Teacher values('02' , '李四');
insert into Teacher values('03' , '王五');
create table SC(sid varchar(10),cid varchar(10),score decimal(18,1));
insert into SC values('01' , '01' , 80);
insert into SC values('01' , '02' , 90);
insert into SC values('01' , '03' , 99);
insert into SC values('02' , '01' , 70);
insert into SC values('02' , '02' , 60);
insert into SC values('02' , '03' , 80);
insert into SC values('03' , '01' , 80);
insert into SC values('03' , '02' , 80);
insert into SC values('03' , '03' , 80);
insert into SC values('04' , '01' , 50);
insert into SC values('04' , '02' , 30);
insert into SC values('04' , '03' , 20);
insert into SC values('05' , '01' , 76);
insert into SC values('05' , '02' , 87);
insert into SC values('06' , '01' , 31);
insert into SC values('06' , '03' , 34);
insert into SC values('07' , '02' , 89);
insert into SC values('07' , '03' , 98);
</code></pre>
<h4>02 表结构预览</h4>
<blockquote>
<p>--学生表<br>
Student(SId,Sname,Sage,Ssex)<br>
--SId 学生编号,Sname 学生姓名,Sage 出生年月,Ssex 学生性别<br>
--课程表<br>
Course(CId,Cname,TId)<br>
--CId 课程编号,Cname 课程名称,TId 教师编号<br>
--教师表<br>
Teacher(TId,Tname)<br>
--TId 教师编号,Tname 教师姓名<br>
--成绩表<br>
SC(SId,CId,score)<br>
--SId 学生编号,CId 课程编号,score 分数</p>
</blockquote>
<h5>1. 查询“01”课程比“02”课程成绩高的所有学生的学号；</h5>
<pre><code>SELECT
    t1.sid
FROM
    (SELECT * FROM sc WHERE cid = 01) AS t1
LEFT JOIN (SELECT * FROM sc WHERE cid = 02) AS t2 ON t1.sid = t2.sid
WHERE
    t1.score > t2.score
</code></pre>
<h5>2. 查询平均成绩大于60分的同学的学号和平均成绩；</h5>
<pre><code>SELECT
    sid,
    AVG(score)
FROM
    sc
GROUP BY
    sid
HAVING
    AVG(score) > 60
</code></pre>
<h5>3. 查询所有同学的学号、姓名、选课数、总成绩</h5>
<pre><code>SELECT
    s.sid,
    s.sname,
    COUNT(c.cid),
    SUM(c.score)
FROM
    sc AS c
LEFT JOIN student AS s ON c.sid = s.sid
GROUP BY
    c.sid
</code></pre>
<h5>4. 查询姓“李”的老师的个数；</h5>
<pre><code>SELECT
    COUNT(tid)
FROM
    teacher
WHERE
    tname LIKE '李%'
</code></pre>
<h5>5. 查询没学过“张三”老师课的同学的学号、姓名；</h5>
<pre><code>SELECT
    sid,
    sname
FROM
    student
WHERE
    sid NOT IN (
        SELECT
            sid
        FROM
            teacher
        LEFT JOIN course ON teacher.tid = course.tid
        LEFT JOIN sc ON course.cid = sc.cid
        WHERE
            teacher.tname = '张三'
    )
</code></pre>
<h5>6、查询学过“01”并且也学过编号“02”课程的同学的学号、姓名；</h5>
<pre><code>SELECT
    s.sid,
    s.sname
FROM
    (
        SELECT
            sid
        FROM
            sc
        GROUP BY
            sid
        HAVING
            COUNT(IF(cid = '01', score, NULL) > 0)
        AND COUNT(IF(cid = '02', score, NULL) > 0)
    ) AS t
LEFT JOIN student AS s ON t.sid = s.sid
</code></pre>
<h5>7. 查询学过“张三”老师所教的课的同学的学号、姓名；</h5>
<pre><code>SELECT
    student.sid,
    student.sname
FROM
    (
        SELECT
            course.cid
        FROM
            teacher
        LEFT JOIN course ON teacher.tid = course.tid
        WHERE
            teacher.tname = '张三'
    ) t
LEFT JOIN sc ON t.cid = sc.cid
LEFT JOIN student ON sc.sid = student.sid
</code></pre>
<h5>8. 查询课程编号“01”的成绩比课程编号“02”课程低的所有同学的学号、姓名；</h5>
<pre><code>SELECT
    t1.sid,
    sname
FROM
    (
        SELECT DISTINCT
            t1.sid AS sid
        FROM
            (SELECT * FROM sc WHERE cid = '01') t1
        LEFT JOIN (SELECT * FROM sc WHERE cid = '02') t2 ON t1.sid = t2.sid
        WHERE
            t1.score < t2.score
    ) t1
LEFT JOIN student ON t1.sid = student.sid
</code></pre>
<h5>9. 查询所有课程成绩小于60分的同学的学号、姓名；</h5>
<pre><code>#①一种方式
SELECT
    t1.sid,
    sname
FROM
    (
        SELECT
            sid
        FROM
            sc
        GROUP BY
            sid
        HAVING
            AVG(score) < 60
    ) AS t1
LEFT JOIN student ON t1.sid = student.sid
</code></pre>
<pre><code># ② 第二种方式
SELECT
    t1.sid,
    sname
FROM
    (
        SELECT
            sid
        FROM
            sc
        GROUP BY
            sid
        HAVING
            max(score < 60)
    ) t1
LEFT JOIN student ON t1.sid = student.sid
</code></pre>
<h5>10. 查询没有学全所有课的同学的学号、姓名；</h5>
<pre><code>SELECT
    s.sid,
    s.sname
FROM
    (
        SELECT
            sid
        FROM
            sc
        GROUP BY
            sid
        HAVING
            COUNT(cid) < (SELECT COUNT(*) FROM course)
    ) t1
LEFT JOIN student s ON t1.sid = s.sid
</code></pre>
<h5>11. 查询至少有一门课与学号为“01”的同学所学相同的同学的学号和姓名；</h5>
<pre><code>SELECT DISTINCT
    sc.sid
FROM
    (SELECT cid FROM sc WHERE sid = 01) t1
LEFT JOIN sc ON t1.cid = sc.cid
</code></pre>
<h6>12. 查询和"01"号的同学学习的课程完全相同的其他同学的学号和姓名</h6>
<pre><code>SELECT
    sc.sid,
    COUNT(sc.cid)
FROM
    sc
LEFT JOIN (
    SELECT
        cid
    FROM
        sc
    WHERE
        sid = '01'
) t1 ON sc.cid = t1.cid
GROUP BY
    sc.sid
HAVING
    COUNT(sc.cid) = 3
AND sc.sid != '01';
</code></pre>
<h5>14. 查询没学过"张三"老师讲授的任一门课程的学生姓名</h5>
<pre><code>SELECT
    sid,
    sname
FROM
    student
WHERE
    sid NOT IN (
        SELECT
            sid
        FROM
            sc
        LEFT JOIN course AS c ON sc.cid = c.cid
        LEFT JOIN teacher AS t ON c.tid = t.tid
        WHERE
            tname = '张三'
    )
</code></pre>
<h5>15. 查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩</h5>
<pre><code>SELECT
    sid,
    avg(score),
    COUNT(IF(score < 60, cid, NULL)) AS num
FROM
    sc
GROUP BY
    sid
HAVING
    COUNT(IF(score < 60, cid, NULL)) >= 2
</code></pre>
<h5>16. 检索"01"课程分数小于60，按分数降序排列的学生信息</h5>
<pre><code>SELECT
    *
FROM
    sc
WHERE
    cid = '01'
GROUP BY
    sid
HAVING
    score < 60
ORDER BY
    score DESC
</code></pre>
<h5>17. 按平均成绩从高到低显示所有学生的平均成绩</h5>
<pre><code>SELECT
    sid,
    avg(score) AS av
FROM
    sc
GROUP BY
    sid
ORDER BY
    av DESC
</code></pre>
<h5>18. 查询各科成绩最高分、最低分和平均分：以如下形式显示：课程ID，课程name，最高分，最低分，平均分，及格率</h5>
<pre><code>SELECT
    sc.cid,
    c.cname,
    MAX(sc.score),
    MIN(sc.score),
    AVG(sc.score),
    count(IF(score >= 60, sid, NULL)) / count(sid) AS pass_rate
FROM
    sc
LEFT JOIN course AS c ON sc.cid = c.cid
GROUP BY
    sc.cid
</code></pre>
<h5>19. 按各科平均成绩从低到高和及格率的百分数从高到低顺序</h5>
<pre><code>select 
   cid
,avg(score) as avg_score
    ,count(if(score>=60,sid,null))/count(sid) as pass_rate
from sc
group by cid
order by avg_score,pass_rate desc
</code></pre>
<h6>20. 查询学生的总成绩并进行排名</h6>
<pre><code>SELECT
    sid,
    SUM(score) AS zh
FROM
    sc
GROUP BY
    sid
ORDER BY
    zh DESC
</code></pre>
<h5>21. 查询不同老师所教不同课程平均分从高到低显示</h5>
<pre><code>SELECT
    c.tid,
    avg(score) AS cj
FROM
    sc
LEFT JOIN course AS c ON sc.cid = c.cid
GROUP BY
    sc.cid
ORDER BY
    cj DESC
</code></pre>
<h5>22. 查询所有课程的成绩第2名到第3名的学生信息及该课程成绩</h5>
<pre><code>SELECT
    sid,
    rank_num,
    score,
    cid
FROM
    (
        SELECT
            rank () over (
                PARTITION BY cid
                ORDER BY
                    score DESC
            ) AS rank_num,
            sid,
            score,
            cid
        FROM
            sc
    ) t
WHERE
    rank_num IN (2, 3)
</code></pre>
<h5>23. 统计各科成绩各分数段人数：课程编号,课程名称,[100-85],[85-70],[70-60],[0-60]及所占百分比</h5>
<pre><code>select
    sc.cid
    ,cname
    ,count(if(score between 85 and 100,sid,null))/count(sid)
    ,count(if(score between 70 and 85,sid,null))/count(sid)
    ,count(if(score between 60 and 70,sid,null))/count(sid)
    ,count(if(score between 0 and 60,sid,null))/count(sid)
from sc
left join course
    on sc.cid=course.cid
group by sc.cid,cname
</code></pre>
<h5>24. 查询学生平均成绩及其名次</h5>
<pre><code>SELECT
    sid,
    avg_cj,
    rank () over (ORDER BY avg_cj DESC) AS rank_num
FROM
    (
        SELECT
            sid,
            avg(score) AS avg_cj
        from sc
        GROUP BY
            sid
    ) t
</code></pre>
<h5>25. 查询各科成绩前三名的记录</h5>
<pre><code>SELECT sid,cid,cj_num,score
FROM
    (
        SELECT
            sid,
            cid,
            rank () over (
                PARTITION BY cid
                ORDER BY
                    score DESC
            ) AS cj_num,
            score
        FROM
            sc
    ) t
WHERE
    cj_num <= 3
</code></pre>
  
</div>
            