const a = {
  error: false,
  spotDefaultDataInfo: {
    spotSeq: "093992dd9d7af1b702334b15befb99e920180511095358",
    spotRate: "bf",
    spotAveragePoint: "5.0",
    spotName: "SC제일은행",
    spotCategory: "category7",
    spotLat: 37.558222241761,
    spotLng: 126.92745610114,
    spotZipcode: "04056",
    spotAddress: "서울특별시 마포구 신촌로 10",
    spotBuildingName: "",
    spotPlaceId: "",
    spotOpenDays: {
      openDays: ["mon", "tue", "wed", "thu", "fri"],
      openTime: "09:30",
      closeTime: "04:30",
    },
    spotCloseDays: {
      openTime: "",
      closeDays: "",
      closeTime: "",
    },
    spotRunTimesMemo: "",
    spotTelNumber: "15881599",
    spotUrlLink: "",
    spotRegLang: "",
    spotIsViewEnabled: "Y",
    spotViewCount: 72,
    soptRegUserInfoSeq: "86b49eb710e87f59b5989441d3871e7d20180502073847",
    soptRegUserId: "ssh960512@naver.com",
    spotRegLoginRouteType: "fb",
    spotRegDatetime: "2018-05-11 09:53:58",
  },
  spotMainImageDataInfo: [
    {
      spotAwsS3Seq: "88225d8249daa9375228e76afeba39b920180511095338",
      spotAwsS3ImageFullUrl:
        "https://s3.ap-northeast-1.amazonaws.com/bfzido.com/main/ssh960512%40naver.com/dir_20180511/5af5682024d88aaaaaaaabb.jpg",
      spotAwsS3ThumnailFullUrl:
        "https://s3.ap-northeast-1.amazonaws.com/bfzido.com/main/ssh960512%40naver.com/dir_20180511/thumb/t_200_5af5682024d88aaaaaaaabb.jpg",
      spotAwsS3ImageSortNum: 0,
    },
    {
      spotAwsS3Seq: "7a7d01b46a567d27677ab347814abbb020180511095341",
      spotAwsS3ImageFullUrl:
        "https://s3.ap-northeast-1.amazonaws.com/bfzido.com/main/ssh960512%40naver.com/dir_20180511/5af5682359e78rrrrssssss.jpg",
      spotAwsS3ThumnailFullUrl:
        "https://s3.ap-northeast-1.amazonaws.com/bfzido.com/main/ssh960512%40naver.com/dir_20180511/thumb/t_200_5af5682359e78rrrrssssss.jpg",
      spotAwsS3ImageSortNum: 1,
    },
    {
      spotAwsS3Seq: "7700141c0624c3c75f40b17ea68e6aca20180511095344",
      spotAwsS3ImageFullUrl:
        "https://s3.ap-northeast-1.amazonaws.com/bfzido.com/main/ssh960512%40naver.com/dir_20180511/5af568264669ftttttttttt.jpg",
      spotAwsS3ThumnailFullUrl:
        "https://s3.ap-northeast-1.amazonaws.com/bfzido.com/main/ssh960512%40naver.com/dir_20180511/thumb/t_200_5af568264669ftttttttttt.jpg",
      spotAwsS3ImageSortNum: 2,
    },
  ],
  spotFacilitiesDataInfo: [
    {
      sfsSeq: 1,
      sfsDesc: [],
      sfsName: {
        en: "Suitable for family / children",
        ko: "가족/어린이 이용에 적합",
      },
      isChecked: true,
      sfsIconUrl:
        "https://s3.ap-northeast-2.amazonaws.com/bfzido/images/facilities_icon/",
      sfsSortNum: 0,
      sfsIconName: "icon_people.png",
      sfsIsEnabled: "Y",
      sfsRegDatetime: "2018-01-10 18:30:00",
    },
    {
      sfsSeq: 2,
      sfsDesc: {
        en: "Wheelchair access is easy.",
        ko: "휠체어 접근이 용이합니다.",
      },
      sfsName: {
        en: "Wheelchair accessible",
        ko: "휠체어 접근 가능",
      },
      isChecked: true,
      sfsIconUrl:
        "https://s3.ap-northeast-2.amazonaws.com/bfzido/images/facilities_icon/",
      sfsSortNum: 1,
      sfsIconName: "icon_disabled.png",
      sfsIsEnabled: "Y",
      sfsRegDatetime: "2018-01-10 18:30:00",
    },
  ],
  spotQuestionDataInfo: [
    {
      sqsmQ: {
        en: "Do you have access to a wheelchair?",
        ko: "휠체어로 진입할 수 있는 입구가 있습니까?",
      },
      sqsmSeq: 1,
      sqsmDesc: {
        en: "Please check the information before entering the place.",
        ko: "해당 장소에 대한 진입 전 정보를 확인해 주세요.",
      },
      sqsmName: {
        en: "Q1. Pre-entry information",
        ko: "Q1. 진입 전 정보",
      },
      sqsmQDesc: {
        en: "If the entrance of the place is more than 1 meter wide and there is no staircase at the entrance (or if there is a ramp), answer 'yes'. 1 meter is the width that two people can comfortably stand side by side. Answer 'Yes' if there is no entrance, and 'No' if there is only revolving door.",
        ko: "장소 입구의 너비가 1미터 이상이고 입구에 계단이 없는 경우(또는 경사로가 있는 경우) ‘예’로 답합니다. 1미터는 두 사람이 편안하게 옆으로 나란히 서 있을 수 있는 정도의 너비를 말합니다. 입구가 없는 경우에는 ‘예’로 답하고, 회전문만 있는 경우에는 ‘아니오’로 답합니다.",
      },
      sqsmSortNum: 0,
      sqsmAnswered: "Y",
      sqsmMainName: {
        en: "Pre-entry information",
        ko: "진입 전 정보",
      },
      sqsmIsEnabled: "Y",
      sqsmRegDatetime: "2018-01-10 18:30:00",
      subQuestionInfo: [
        {
          sqssQ: {
            en: "Parking lot installation status",
            ko: "주차장 설치 현황",
          },
          sqsmSeq: 1,
          sqssSeq: 2,
          sqssDesc: {
            en: "Please check the information before entering the place.",
            ko: "해당 장소에 대한 진입 전 정보를 확인해주세요.",
          },
          sqssName: {
            en: "Q1-1. Details before entering",
            ko: "Q1-1. 진입 전 상세 정보",
          },
          sqssQDesc: {
            en: "Please check all that apply.",
            ko: "해당하는것을 모두 체크해주세요.",
          },
          sqssSortNum: 0,
          sqssSubQInfo: [
            {
              sqssSeq: 2,
              sqssqSeq: 8,
              isChecked: false,
              sqssqInfo: {
                en: "Disabled area available",
                ko: "장애인 전용구역이 있음",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 2,
              sqssqSeq: 9,
              isChecked: false,
              sqssqInfo: {
                en: "There is a regular parking area.",
                ko: "일반 주차구역이 있음",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 2,
              sqssqSeq: 10,
              isChecked: true,
              sqssqInfo: {
                en: "None",
                ko: "주차장이 없다.",
              },
              sqssqIsEnabled: "Y",
            },
          ],
          sqssIsEnabled: "Y",
          sqssRegDatetime: "2018-04-18 18:00:00",
        },
        {
          sqssQ: {
            en: "In-building use entrance",
            ko: "건물 내 이용 장소 입구 현황",
          },
          sqsmSeq: 1,
          sqssSeq: 3,
          sqssDesc: {
            en: "Please check the information before entering the place.",
            ko: "해당 장소에 대한 진입 전 정보를 확인해주세요.",
          },
          sqssName: {
            en: "Q1-2. Details before entering",
            ko: "Q1-2. 진입 전 상세 정보",
          },
          sqssQDesc: {
            en: "At the gate threshold, you can see the length of the short side of the card or business card.",
            ko: "출입문 문턱의 경우 카드나 명함의 짧은쪽 면 길이로 확인 할 수 있습니다.",
          },
          sqssSortNum: 1,
          sqssSubQInfo: [
            {
              sqssSeq: 3,
              sqssqSeq: 11,
              isChecked: false,
              sqssqInfo: {
                en: "N / A (The entire building is the same facility)",
                ko: "해당 없음(건물 전체가 같은 시설임)",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 3,
              sqssqSeq: 12,
              isChecked: false,
              sqssqInfo: {
                en: "Movable corridor width more than 120cm",
                ko: "복도 이동가능 폭 120cm 이상",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 3,
              sqssqSeq: 13,
              isChecked: false,
              sqssqInfo: {
                en: "Inside door width more than 90cm",
                ko: "내부 출입문 폭 90cm 이상",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 3,
              sqssqSeq: 14,
              isChecked: true,
              sqssqInfo: {
                en: "No door threshold or less than 5cm",
                ko: "출입문 문턱 없거나 5cm이하",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 3,
              sqssqSeq: 15,
              isChecked: false,
              sqssqInfo: {
                en: "Automatic doors",
                ko: "자동문",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 3,
              sqssqSeq: 16,
              isChecked: false,
              sqssqInfo: {
                en: "Inconvenience",
                ko: "출입 불편함",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 3,
              sqssqSeq: 17,
              isChecked: false,
              sqssqInfo: {
                en: "Unavailable",
                ko: "이용 불가능",
              },
              sqssqIsEnabled: "Y",
            },
          ],
          sqssIsEnabled: "Y",
          sqssRegDatetime: "2018-04-18 18:00:01",
        },
      ],
      sqsmDetailViewInfo: {
        en: "Wheelchair entry entrance",
        ko: "휠체어 진입 입구",
      },
      isDetailInfoEntered: true,
      isSubQuestionEnabled: true,
      isMainQuestionEnabled: false,
    },
    {
      sqsmQ: {
        en: "Can I use the corridor and inner door without the inconvenience of transportation?",
        ko: "복도와 내부 출입문을 교통약자가 불편함 없이 이용 할 수 있습니까?",
      },
      sqsmSeq: 2,
      sqsmDesc: {
        en: "Please confirm the information after entering the place.",
        ko: "해당 장소에 대한 진입 후 정보를 확인해 주세요.",
      },
      sqsmName: {
        en: "Q2. Information after entry",
        ko: "Q2. 진입 후 정보",
      },
      sqsmQDesc: {
        en: "Please consider whether it is inconvenient to use wheelchair etc. and please choose",
        ko: "휠체어 등을 이용하기에 불편함이 없는지 잘 생각해서 선택 해 주세요.",
      },
      sqsmSortNum: 1,
      sqsmAnswered: "Y",
      sqsmMainName: {
        en: "Information after entry",
        ko: "진입 후 정보",
      },
      sqsmIsEnabled: "Y",
      sqsmRegDatetime: "2018-04-18 18:00:00",
      subQuestionInfo: [
        {
          sqssQ: {
            en: "Hallway",
            ko: "복도",
          },
          sqsmSeq: 2,
          sqssSeq: 4,
          sqssDesc: {
            en: "Please check the information after entering the place.",
            ko: "해당 장소에 대한 진입 후 정보를 확인해주세요.",
          },
          sqssName: {
            en: "Q2-1. Details after entry",
            ko: "Q2-1. 진입 후 상세 정보",
          },
          sqssQDesc: {
            en: "Please check all that apply.",
            ko: "해당하는것을 모두 체크해주세요.",
          },
          sqssSortNum: 2,
          sqssSubQInfo: [
            {
              sqssSeq: 4,
              sqssqSeq: 18,
              isChecked: true,
              sqssqInfo: {
                en: "Wheelchair accessible",
                ko: "휠체어 진입 가능함",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 4,
              sqssqSeq: 19,
              isChecked: false,
              sqssqInfo: {
                en: "Slope angle less than 20 degrees",
                ko: "경사로 각도 20도 이하",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 4,
              sqssqSeq: 20,
              isChecked: false,
              sqssqInfo: {
                en: "Unable to enter",
                ko: "진입 불가능",
              },
              sqssqIsEnabled: "Y",
            },
          ],
          sqssIsEnabled: "Y",
          sqssRegDatetime: "2018-04-18 18:00:02",
        },
        {
          sqssQ: {
            en: "Elevator",
            ko: "엘리베이터",
          },
          sqsmSeq: 2,
          sqssSeq: 5,
          sqssDesc: {
            en: "Please check the information after entering the place.",
            ko: "해당 장소에 대한 진입 후 정보를 확인해주세요.",
          },
          sqssName: {
            en: "Q2-2. Details after entry",
            ko: "Q2-2. 진입 후 상세 정보",
          },
          sqssQDesc: {
            en: "Please check all that apply.",
            ko: "해당하는것을 모두 체크해주세요.",
          },
          sqssSortNum: 3,
          sqssSubQInfo: [
            {
              sqssSeq: 5,
              sqssqSeq: 21,
              isChecked: false,
              sqssqInfo: {
                en: "Elevator for the disabled",
                ko: "장애인용 엘리베이터 있음(안전바 설치유무)",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 5,
              sqssqSeq: 22,
              isChecked: false,
              sqssqInfo: {
                en: "Normal elevator available",
                ko: "일반 엘리베이터 이용 가능",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 5,
              sqssqSeq: 23,
              isChecked: true,
              sqssqInfo: {
                en: "None",
                ko: "없음(단층)",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 5,
              sqssqSeq: 24,
              isChecked: false,
              sqssqInfo: {
                en: "Unable to enter",
                ko: "진입 불가능",
              },
              sqssqIsEnabled: "Y",
            },
          ],
          sqssIsEnabled: "Y",
          sqssRegDatetime: "2018-04-18 18:00:03",
        },
      ],
      sqsmDetailViewInfo: {
        en: "Corridors and internal doors",
        ko: "복도와 내부 출입문",
      },
      isDetailInfoEntered: true,
      isSubQuestionEnabled: true,
      isMainQuestionEnabled: false,
    },
    {
      sqsmQ: {
        en: "Do you have facilities available to the weak?",
        ko: "교통약자가 이용할 수 있는 시설이 있습니까?",
      },
      sqsmSeq: 3,
      sqsmDesc: {
        en: "Please check the internal space information for that place.",
        ko: "해당 장소에 대한 내부 공간 정보를 확인해주세요.",
      },
      sqsmName: {
        en: "Q3. Inner space",
        ko: "Q3. 내부 공간",
      },
      sqsmQDesc: {
        en: "Do you have facilities such as elevators and wheelchairs, whether there is a table on the table or a table?",
        ko: "엘리베이터 등 휠체어가 오갈 수 있는 시설이 있는지 테이블이 입식 테이블이 있는지 등 내부에 교통약자가 편하게 이용 할 수 있습니까?",
      },
      sqsmSortNum: 2,
      sqsmAnswered: "Y",
      sqsmMainName: {
        en: "Inner space",
        ko: "내부 공간",
      },
      sqsmIsEnabled: "Y",
      sqsmRegDatetime: "2018-04-18 18:10:00",
      subQuestionInfo: [
        {
          sqssQ: {
            en: "Seating Status",
            ko: "좌석 현황",
          },
          sqsmSeq: 3,
          sqssSeq: 6,
          sqssDesc: {
            en: "Please check the internal space information for that place.",
            ko: "해당 장소에 대한 내부 공간 정보를 확인해주세요.",
          },
          sqssName: {
            en: "Q3-1. Inner space",
            ko: "Q3-1. 내부 공간",
          },
          sqssQDesc: {
            en: "Please check all that apply.",
            ko: "해당하는것을 모두 체크해주세요.",
          },
          sqssSortNum: 4,
          sqssSubQInfo: [
            {
              sqssSeq: 6,
              sqssqSeq: 25,
              isChecked: false,
              sqssqInfo: {
                en: "With a table stand",
                ko: "입식 테이블 의자가 있음",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 6,
              sqssqSeq: 26,
              isChecked: true,
              sqssqInfo: {
                en: "Wheelchair accessible",
                ko: "휠체어가 다닐 수 있음",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 6,
              sqssqSeq: 27,
              isChecked: false,
              sqssqInfo: {
                en: "Group available (5 ~ 10 people)",
                ko: "단체 이용 가능(5~10명)",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 6,
              sqssqSeq: 28,
              isChecked: false,
              sqssqInfo: {
                en: "Unable to enter",
                ko: "진입 불가능",
              },
              sqssqIsEnabled: "Y",
            },
          ],
          sqssIsEnabled: "Y",
          sqssRegDatetime: "2018-04-18 18:00:04",
        },
        {
          sqssQ: {
            en: "Toilet",
            ko: "화장실",
          },
          sqsmSeq: 3,
          sqssSeq: 7,
          sqssDesc: {
            en: "Please check the internal space information for that place.",
            ko: "해당 장소에 대한 내부 공간 정보를 확인해주세요.",
          },
          sqssName: {
            en: "Q3-2. Inner space",
            ko: "Q3-2. 내부 공간",
          },
          sqssQDesc: {
            en: "Please check all that apply.",
            ko: "해당하는것을 모두 체크해주세요.",
          },
          sqssSortNum: 5,
          sqssSubQInfo: [
            {
              sqssSeq: 7,
              sqssqSeq: 29,
              isChecked: true,
              sqssqInfo: {
                en: "Disabled toilet available",
                ko: "장애인용 화장실 있음(안전바 설치유무)",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 7,
              sqssqSeq: 30,
              isChecked: false,
              sqssqInfo: {
                en: "Common toilet",
                ko: "일반화장실(입구에 턱이 없거나 5cm이하)",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 7,
              sqssqSeq: 31,
              isChecked: false,
              sqssqInfo: {
                en: "With front rotator room",
                ko: "대변기 전면 회전공간 있음",
              },
              sqssqIsEnabled: "Y",
            },
            {
              sqssSeq: 7,
              sqssqSeq: 32,
              isChecked: false,
              sqssqInfo: {
                en: "Unable to enter",
                ko: "진입 불가능",
              },
              sqssqIsEnabled: "Y",
            },
          ],
          sqssIsEnabled: "Y",
          sqssRegDatetime: "2018-04-18 18:00:05",
        },
      ],
      sqsmDetailViewInfo: {
        en: "Facilities available inside the transportation abbreviation",
        ko: "교통약자 내부 이용 가능 시설",
      },
      isDetailInfoEntered: true,
      isSubQuestionEnabled: true,
      isMainQuestionEnabled: false,
    },
  ],
  spotDataChangeHistoryInfo: {
    firstAddUserInfo: {
      userInfoSeq: "86b49eb710e87f59b5989441d3871e7d20180502073847",
      userId: "ssh960512@naver.com",
      userMainType: "F",
      userSupportKitType: "",
      userCharacterType: "A",
      signupRouteType: "fb",
      signupSnsId: "1265116163623428",
      signupAcceptLanguage: "ko",
      firstName: "사헌",
      lastName: "송",
      nickName: "송사헌20153418",
      phoneNumber:
        "+P2ssXmAkajuVRwPWVt63saCJMw4J02RRGnj3UUazSCrfWhi0EI77EBNWReJxrBgOo/G8+rz7r5NcKpKKjCVMu8XM86F9yKCJOvTIOjXwIZJ3P3v+tdFXncUG1qkHDzh",
      gender: "M",
      birthday: "1996-05-12",
      profilePhoto: "",
      profileContents: "",
      activeZoneLat: null,
      activeZoneLng: null,
      activeZoneAddress: null,
      etcSettingInfo: "",
      editDate: "2018-05-11 09:23:36",
      regDate: "2018-05-02 07:38:47",
    },
    lastEditUserInfo: {
      userId: "",
      userCharacterType: "",
      firstName: "",
      lastName: "",
      nickName: "",
      profilePhoto: "",
    },
    totalEditCount: 0,
  },
  spotFavoritesDataInfo: {
    isCurrentSpotFavorites: false,
    totalCurrentSpotFavoritesCount: 0,
  },
  spotAuthDataInfo: {
    isDataEditAuth: false,
    isDataDeleteAuth: false,
  },
  spotDonationDataInfo: [],
  message: "spot_detail_view_success",
};
