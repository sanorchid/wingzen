
$(function() {
	$(".nav-sidebar li a").on("click", function() {
		if ($(this).next().hasClass("sub-menu")) {
			if (!$(this).next().children().hasClass("toActivate")) {
				$(this).parent().addClass("toActivate");
			}
			if ($(this).next().hasClass("hide")) {
				$(this).next().removeClass("hide");
			}
			else {
				$(this).next().addClass("hide");
			}
		}
		else {
			if ($(this).parent().parent().hasClass("sub-menu")) {
				$(".nav-sidebar .toActivate").removeClass("toActivate");
				$(".nav-sidebar .active").removeClass("active");
				$(this).parent().addClass("toActivate");
				$(this).parent().parent().prev().addClass("active");
			}
			else {
				$(".nav-sidebar .toActivate").removeClass("toActivate");
				$(".nav-sidebar .active").removeClass("active");
				$(".nav-sidebar .sub-menu").addClass("hide");
				$(this).parent().addClass("active");
        	}
        	sid=$(this).parent().attr('id');
			$.ajax({
				url: "aget_dbsc",
				data: {
				'sid': sid
				},
				success: function(json) {
					$(".table-responsive").children().remove();
					var thm = 0; thn = 0;
					var $table = $("<table/>");
					$table.addClass("table table-condensed");
					jlen = json.result.length;
					$table.append($("<caption/>").text("共 "+jlen+" 条记录"));
					if (sid == 'address-list') {
						for (var i=0; i<jlen; i++) {
							if (!thn) {
								$thName = $("<th/>").text("姓名");
								$thSex = $("<th/>").text("性别");
								$thWid = $("<th/>").text("员工号");
								$thIs_teamleader = $("<th/>").text("组长");
								$thInst = $("<th/>").text("校区");
								$thDepartment = $("<th/>").text("部门");
								$thRank= $("<th/>").text("级别");
								$thGrade = $("<th/>").text("年级");
								$thSubject = $("<th/>").text("科目");
								$thBirthday = $("<th/>").text("生日");
								$thTelephone = $("<th/>").text("电话");
								$th = $("<tr/>").append($thName, $thSex, $thWid, $thIs_teamleader, $thInst, $thDepartment, $thRank, $thGrade, $thSubject, $thBirthday, $thTelephone);
								thn = 1;
							}
							$tdName = $("<td/>").text(json.result[i].name);
							$tdSex = $("<td/>").text(json.result[i].sex);
 							$tdWid = $("<td/>").text(json.result[i].wid);
							$tdIs_teamleader = $("<td/>").text(json.result[i].is_teamleader);
							$tdInst = $("<td/>").text(json.result[i].inst);
							$tdDepartment = $("<td/>").text(json.result[i].department);
							$tdRank = $("<td/>").text(json.result[i].rank);
							$tdGrade = $("<td/>").text(json.result[i].grade);
							$tdSubject = $("<td/>").text(json.result[i].subject);
							$tdBirthday = $("<td/>").text(json.result[i].birthday);
							$tdTelephone = $("<td/>").text(json.result[i].telephone);
							$tr = $("<tr/>").append($tdName,$tdSex, $tdWid, $tdIs_teamleader, $tdInst, $tdDepartment, $tdRank, $tdGrade, $tdSubject, $tdBirthday, $tdTelephone);

							if (json.result[i].pd) {
								if (!thm) {
									$thUser = $("<th/>").text("用户名");
									$thSid = $("<th/>").text("身份证号");
									$thDatentry = $("<th/>").text("合同起始日");
									$thDatexpire = $("<th/>").text("合同到期日");
									$thGraduate = $("<th/>").text("毕业学校");
									$thMajor = $("<th/>").text("专业");
									$th.append($thUser, $thSid, $thDatentry, $thDatexpire, $thGraduate, $thMajor);
									$table.append($th);
									thm = 1;
								}
								$tdUser = $("<td/>").text(json.result[i].user);
								$tdSid = $("<td/>").text(json.result[i].sid);
								$tdDatentry = $("<td/>").text(json.result[i].datentry);
								$tdDatexpire = $("<td/>").text(json.result[i].datexpire);
								$tdGraduate = $("<td/>").text(json.result[i].graduate);
								$tdMajor = $("<td/>").text(json.result[i].major);
								$tr.append($tdUser, $tdSid, $tdDatentry, $tdDatexpire, $tdGraduate, $tdMajor);
								$table.append($tr);
							}
							else {
								$table.append($th);
								$table.append($tr);
							}
						}
						$table.appendTo(".table-responsive");

					}
					else if (sid == 'present-stulist' || sid == 'trial-stulist') {
						for (var i=0; i<jlen; i++) {
							if (!thn) {
								$thName = $("<th/>").text("姓名");
								$thSex = $("<th/>").text("性别");
								$thSchool = $("<th/>").text("学校");
								$thGrade = $("<th/>").text("年级");
								$thKlass = $("<th/>").text("班级");
								$thTelephone = $("<th/>").text("联系电话");
								$thAddress= $("<th/>").text("家庭地址");
								$thInitchs = $("<th/>").text("入学语文成绩");
								$thInitmath = $("<th/>").text("入学数学成绩");
								$thIniteng = $("<th/>").text("入学英语成绩");
								$thInitsci = $("<th/>").text("入学科学成绩");
								$thInitrnk = $("<th/>").text("入学年级排名");
								$thInst = $("<th/>").text("校区");
								$thCsort = $("<th/>").text("课程类别");
								$thCourse = $("<th/>").text("课程");
								$thDatentry = $("<th/>").text("入学日期");
								$thIs_picked = $("<th/>").text("是否接送");
								$thIs_dining = $("<th/>").text("是否就餐");
								$thCharacter = $("<th/>").text("性格特点");
								$thMemo = $("<th/>").text("备注");
								$thReceiver = $("<th/>").text("接收人");

								$th = $("<tr/>").append($thName, $thSex, $thSchool, $thGrade, $thKlass, $thTelephone, $thAddress, $thInitchs, $thInitmath, $thIniteng, $thInitsci, $thInitrnk, $thInst, $thCsort, $thCourse, $thDatentry, $thIs_picked, $thIs_dining, $thCharacter, $thMemo, $thReceiver);
								$table.append($th);
								thn = 1;
							}
							if ((sid == 'present-stulist' && json.result[i].status == 'present')||(sid == 'trial-stulist' && json.result[i].status == 'trial')) {
								$tdName = $("<td/>").text(json.result[i].name);
								$tdSex = $("<td/>").text(json.result[i].sex);
								$tdSchool = $("<td/>").text(json.result[i].school);
								$tdGrade = $("<td/>").text(json.result[i].grade);
								$tdKlass = $("<td/>").text(json.result[i].klass);
								$tdTelephone = $("<td/>").text(json.result[i].telephone);
								$tdAddress = $("<td/>").text(json.result[i].address);
								$tdInitchs = $("<td/>").text(json.result[i].initchs);
								$tdInitmath = $("<td/>").text(json.result[i].initmath);
								$tdIniteng = $("<td/>").text(json.result[i].initeng);
								$tdInitsci = $("<td/>").text(json.result[i].initsci);
								$tdInitrnk = $("<td/>").text(json.result[i].initrnk);
								$tdInst = $("<td/>").text(json.result[i].inst);
								$tdCsort = $("<td/>").text(json.result[i].csort);
								$tdCourse = $("<td/>").text(json.result[i].course);
								$tdDatentry = $("<td/>").text(json.result[i].datentry);
								$tdIs_picked = $("<td/>").text(json.result[i].is_picked);
								$tdIs_dining = $("<td/>").text(json.result[i].is_dining);
								$tdCharacter = $("<td/>").text(json.result[i].character);
								$tdMemo = $("<td/>").text(json.result[i].memo);
								$tdReceiver = $("<td/>").text(json.result[i].receiver);
								$tr= $("<tr/>").append($tdName, $tdSex, $tdSchool, $tdGrade, $tdKlass, $tdTelephone, $tdAddress, $tdInitchs, $tdInitmath, $tdIniteng, $tdInitsci, $tdInitrnk, $tdInst, $tdCsort, $tdCourse, $tdDatentry, $tdIs_picked, $tdIs_dining, $tdCharacter, $tdMemo, $tdReceiver);
								$table.append($tr);

							}
						}
					}
					else if (sid == 'score-stat') {
						for (var i=0; i<jlen; i++) {
							if (!thn) {
								$thStudent = $("<th/>").text("学生");
								$thGrade = $("<th/>").text("年级");
								$thExam = $("<th/>").text("考试");
								$thDate = $("<th/>").text("日期");
								$thEnglish = $("<th/>").text("英语");
								$thChinese = $("<th/>").text("语文");
								$thMaths = $("<th/>").text("数学");
								$thScience= $("<th/>").text("科学");
								$thPhysics = $("<th/>").text("物理");
								$thChemistry = $("<th/>").text("化学");
								$thBiology = $("<th/>").text("生物");
								$thRank = $("<th/>").text("排名");
								$thMemo = $("<th/>").text("备注");

								$tr=$("<tr/>").append($thStudent, $thGrade, $thExam, $thDate, $thEnglish, $thChinese, $thMaths, $thScience, $thPhysics, $thChemistry, $thBiology, $thRank, $thMemo);
								$table.append($tr);
								thn = 1;
							}
							$tdStudent = $("<td/>").text(json.result[i].student);
							$tdGrade = $("<td/>").text(json.result[i].grade);
							$tdExam = $("<td/>").text(json.result[i].exam);
							$tdDate = $("<td/>").text(json.result[i].date);
							$tdEnglish = $("<td/>").text(json.result[i].english);
							$tdChinese = $("<td/>").text(json.result[i].chinese);
							$tdMaths = $("<td/>").text(json.result[i].maths);
							$tdScience = $("<td/>").text(json.result[i].science);
							$tdPhysics = $("<td/>").text(json.result[i].physics);
							$tdChemistry = $("<td/>").text(json.result[i].chemistry);
							$tdBiology = $("<td/>").text(json.result[i].biology);
							$tdRank = $("<td/>").text(json.result[i].rank);
							$tdMemo = $("<td/>").text(json.result[i].memo);

							$tr = $("<tr/>").append($tdStudent, $tdGrade, $tdExam, $tdDate, $tdEnglish, $tdChinese, $tdMaths, $tdScience, $tdPhysics, $tdChemistry, $tdBiology, $tdRank, $tdMemo)
							$table.append($tr);

						}

					}
					else if (sid == 'learn-record') {
						for (var i=0; i<jlen; i++) {
							if (!thn) {
								$thStudent = $("<th/>").text("学生");
								$thGrade = $("<th/>").text("年级");
								$thDatefrom = $("<th/>").text("起始日期");
								$thDateto = $("<th/>").text("结束日期");
								$thStustat = $("<th/>").text("学生状态");
								$thStugoal = $("<th/>").text("学习目标");
								$thIs_focus = $("<th/>").text("是否重点关注");
								$thMemo= $("<th/>").text("备注");

								$tr = $("<tr/>").append($thStudent, $thGrade, $thDatefrom, $thDateto, $thStustat, $thStugoal, $thIs_focus, $thMemo)
								$table.append($tr);
								thn = 1;
							}
							$tdStudent = $("<td/>").text(json.result[i].student);
							$tdGrade = $("<td/>").text(json.result[i].grade);
							$tdDatefrom = $("<td/>").text(json.result[i].datefrom);
							$tdDateto = $("<td/>").text(json.result[i].dateto);
							$tdStustat = $("<td/>").text(json.result[i].stustat);
							$tdStugoal = $("<td/>").text(json.result[i].stugoal);
							$tdIs_focus = $("<td/>").text(json.result[i].is_focus);
							$tdMemo = $("<td/>").text(json.result[i].memo);

							$tr = $("<tr/>").append($tdStudent, $tdGrade, $tdDatefrom, $tdDateto, $tdStustat, $tdStugoal, $tdIs_focus, $tdMemo)
							$table.append($tr);
						}
					}
					else if (sid == 'zen-kls') {
						for (var i=0; i<jlen; i++) {
							if (!thn) {
								$thInst = $("<th/>").text("校区");
								$thName= $("<th/>").text("班级");
								$thRoom = $("<th/>").text("教室");
								$tr = $("<tr/>").append($thInst, $thName, $thRoom);
								$table.append($tr);
								thn = 1;
							}
							$tdInst = $("<td/>").text(json.result[i].inst);
							$tdName = $("<td/>").text(json.result[i].name);
							$tdRoom = $("<td/>").text(json.result[i].room);
							$tr = $("<tr>").append($tdInst, $tdName, $tdRoom);
							$table.append($tr);
						}
					}
					else if (sid == 'course-tuition') {
						for (var i=0; i<jlen; i++) {
							if (!thn) {
								$thName = $("<th/>").text("名称");
								$thTuition= $("<th/>").text("学费");
								$thCtimes = $("<th/>").text("课次");
								$tr = $("<tr/>").append($thName, $thTuition, $thCtimes);
								$table.append($tr);
								thn = 1;
							}
							$tdName = $("<td/>").text(json.result[i].name);
							$tdTuition = $("<td/>").text(json.result[i].tuition);
							$tdCtimes = $("<td/>").text(json.result[i].ctimes);
							$tr = $("<tr/>").append($tdName, $tdTuition, $tdCtimes);
							$table.append($tr);
						}
					}
					else if (sid == 'stu-tuition') {
						for (var i=0; i<jlen; i++) {
							if (!thn) {
								$thStudent = $("<th/>").text("学生");
								$thGrade= $("<th/>").text("年级");
								$thCourse = $("<th/>").text("课程");
								$thDatefrom = $("<th/>").text("起始日期");
								$thDateto = $("<th/>").text("结束日期");
								$thTuition = $("<th/>").text("学费");
								$thMemo = $("<th/>").text("备注");
								$tr = $("<tr/>").append($thStudent, $thGrade, $thCourse, $thDatefrom, $thDateto, $thTuition, $thMemo)
								$table.append($tr);
								thn = 1;
							}
							$tdStudent = $("<td/>").text(json.result[i].student);
							$tdGrade = $("<td/>").text(json.result[i].grade);
							$tdCourse = $("<td/>").text(json.result[i].course);
							$tdDatefrom = $("<td/>").text(json.result[i].datefrom);
							$tdDateto = $("<td/>").text(json.result[i].dateto);
							$tdTuition = $("<td/>").text(json.result[i].tuition);
							$tdMemo = $("<td/>").text(json.result[i].memo);
							$tr = $("<tr/>").append($tdStudent, $tdGrade, $tdCourse, $tdDatefrom, $tdDateto, $tdTuition, $tdMemo)
							$table.append($tr);
						}
					}
					if (!jlen) {
						$h3 = $("<h3/>").text("您所在年级目前无该列表信息。")
						$h3.appendTo(".table-responsive");
					}
					else {
						$table.appendTo(".table-responsive");
					}

				},
			});
		}

	});

	$("a.zen-red").on("click", function(){
		$("div.reminder-content").slideToggle();
	});

	$(".table-responsive").on("mouseover", "td", function(e) {
		$promptBox = $("<div/>", {id:"prompt-box"}).text($(this).text());
		if ($promptBox.text()) {
			$(".table-responsive").after($promptBox);
			$("#prompt-box").css({"top":"80px", "left":($(window).width)/2 + "px"});
		}
	});
	$(".table-responsive").on("mouseout", "td", function() {
		if ($("#prompt-box")) {
			$("#prompt-box").remove();
		}
	});
});



$(document).ajaxStart(onStart).ajaxComplete(onComplete);

function onStart(event) {
	$img = $("<img/>");
	$img.attr("src", "/static/assets/img/ajax-loader.gif");
	$span = $("<span/>").append($img);
	if ($("ul.nav-sidebar li").hasClass("active")) {
		$span.appendTo($("ul.nav-sidebar li.active a"));
	}
	else {
		$span.appendTo($("ul.nav-sidebar li a.active"));
	}
}

function onComplete(event, xhr, settings) {
	if ($("ul.nav-sidebar li").hasClass("active")) {
		$("ul.nav-sidebar li.active a").children("span").last().remove();
	}
	else {
		$("ul.nav-sidebar li a.active").children("span").last().remove();
	}
}
