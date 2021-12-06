#include <vector>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "DataFormats/MuonReco/interface/MuonRecHitCluster.h"

class HLTMuonRecHitClusterFilter : public edm::global::EDFilter<> {
public:
  explicit HLTMuonRecHitClusterFilter(const edm::ParameterSet&);
  ~HLTMuonRecHitClusterFilter() override = default;
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  bool filter(edm::StreamID, edm::Event&, edm::EventSetup const&) const override;
  const edm::EDGetTokenT<reco::MuonRecHitClusterCollection> cluster_token_;
  const int min_N_;
  const int min_Size_;
  const int min_SizeMinusMB1_;
  const std::vector<double> min_SizeRegionCutEtas_;
  const std::vector<double> max_SizeRegionCutEtas_;
  const std::vector<int> min_SizeRegionCutNstations_;
  const std::vector<int> max_SizeRegionCutNstations_;
  const std::vector<int> min_SizeRegionCutClusterSize_;
  const int max_nMB1_;
  const int max_nMB2_;
  const int max_nME11_;
  const int max_nME12_;
  const int max_nME41_;
  const int max_nME42_;
  const int min_Nstation_;
  const double min_AvgStation_;
  const double min_Time_;
  const double max_Time_;
  const double min_Eta_;
  const double max_Eta_;
  const double max_TimeSpread_;
};
//
// constructors and destructor
//
HLTMuonRecHitClusterFilter::HLTMuonRecHitClusterFilter(const edm::ParameterSet& iConfig)
    : cluster_token_(consumes<reco::MuonRecHitClusterCollection>(iConfig.getParameter<edm::InputTag>("ClusterTag"))),
      min_N_(iConfig.getParameter<int>("MinN")),
      min_Size_(iConfig.getParameter<int>("MinSize")),
      min_SizeMinusMB1_(iConfig.getParameter<int>("MinSizeMinusMB1")),
      min_SizeRegionCutEtas_(iConfig.getParameter<std::vector<double> >("MinSizeRegionCutEtas")),
      max_SizeRegionCutEtas_(iConfig.getParameter<std::vector<double> >("MaxSizeRegionCutEtas")),
      min_SizeRegionCutNstations_(iConfig.getParameter<std::vector<int> >("MinSizeRegionCutNstations")),
      max_SizeRegionCutNstations_(iConfig.getParameter<std::vector<int> >("MaxSizeRegionCutNstations")),
      min_SizeRegionCutClusterSize_(iConfig.getParameter<std::vector<int> >("MinSizeRegionCutClusterSize")),
      max_nMB1_(iConfig.getParameter<int>("Max_nMB1")),
      max_nMB2_(iConfig.getParameter<int>("Max_nMB2")),
      max_nME11_(iConfig.getParameter<int>("Max_nME11")),
      max_nME12_(iConfig.getParameter<int>("Max_nME12")),
      max_nME41_(iConfig.getParameter<int>("Max_nME41")),
      max_nME42_(iConfig.getParameter<int>("Max_nME42")),
      min_Nstation_(iConfig.getParameter<int>("MinNstation")),
      min_AvgStation_(iConfig.getParameter<double>("MinAvgStation")),
      min_Time_(iConfig.getParameter<double>("MinTime")),
      max_Time_(iConfig.getParameter<double>("MaxTime")),
      min_Eta_(iConfig.getParameter<double>("MinEta")),
      max_Eta_(iConfig.getParameter<double>("MaxEta")),
      max_TimeSpread_(iConfig.getParameter<double>("MaxTimeSpread")) {}

void HLTMuonRecHitClusterFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.add<edm::InputTag>("ClusterTag", edm::InputTag("hltCSCrechitClusters"));
  desc.add<int>("MinN", 1);
  desc.add<int>("MinSize", 50);
  desc.add<int>("MinSizeMinusMB1", 9999);
  std::vector<double> minSizeRegionCutEtas{-1., -1., 1.9, 1.9};
  std::vector<double> maxSizeRegionCutEtas{1.9, 1.9, -1., -1.};
  std::vector<int> minSizeRegionCutNstations{-1, 1, -1, 1};
  std::vector<int> maxSizeRegionCutNstations{1, -1, 1, -1};
  std::vector<int> minSizeRegionCutClusterSize{9999, 9999, 9999, 9999};
  desc.add<std::vector<double> >("MinSizeRegionCutEtas", minSizeRegionCutEtas);
  desc.add<std::vector<double> >("MaxSizeRegionCutEtas", maxSizeRegionCutEtas);
  desc.add<std::vector<int> >("MinSizeRegionCutNstations", minSizeRegionCutNstations);
  desc.add<std::vector<int> >("MaxSizeRegionCutNstations", maxSizeRegionCutNstations);
  desc.add<std::vector<int> >("MinSizeRegionCutClusterSize", minSizeRegionCutClusterSize);
  desc.add<int>("Max_nMB1", 999);
  desc.add<int>("Max_nMB2", 999);
  desc.add<int>("Max_nME11", 999);
  desc.add<int>("Max_nME12", 999);
  desc.add<int>("Max_nME41", 999);
  desc.add<int>("Max_nME42", 999);
  desc.add<int>("MinNstation", 0);
  desc.add<double>("MinAvgStation", 0.0);
  desc.add<double>("MinTime", -999);
  desc.add<double>("MaxTime", 999);
  desc.add<double>("MinEta", -1.0);
  desc.add<double>("MaxEta", -1.0);
  desc.add<double>("MaxTimeSpread", 999);
  descriptions.addWithDefaultLabel(desc);
}

//
// member functions
//

// ------------ method called on each new Event  ------------
bool HLTMuonRecHitClusterFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
  int nClusterPassed = 0;

  auto const& rechitClusters = iEvent.get(cluster_token_);

  for (auto const& cluster : rechitClusters) {
    bool passSizeCut = false;
    if (cluster.size() >= min_Size_)
      passSizeCut = true;
    if (cluster.size() - cluster.nMB1() >= min_SizeMinusMB1_)
      passSizeCut = true;
    for (size_t i = 0; i < min_SizeRegionCutEtas_.size(); ++i) {
      if ((min_SizeRegionCutEtas_ < 0.0 || std::abs(cluster.eta()) > min_SizeRegionCutEtas_[i]) &&
          (max_SizeRegionCutEtas_ < 0.0 || std::abs(cluster.eta()) <= max_SizeRegionCutEtas_[i]) &&
          (min_SizeRegionCutNstations_ < 0 || cluster.nStation() > min_SizeRegionCutNstations_[i]) &&
          (max_SizeRegionCutNstations_ < 0 || cluster.nStation() <= max_SizeRegionCutNstations_[i]) &&
          cluster.size() >= min_SizeRegionCutClusterSize_[i])
        passSizeCut = true;
    }
    if ((passSizeCut) && (cluster.nMB1() <= max_nMB1_) && (cluster.nMB2() <= max_nMB2_) &&
        (cluster.nME11() <= max_nME11_) && (cluster.nME12() <= max_nME12_) && (cluster.nME41() <= max_nME41_) &&
        (cluster.nME42() <= max_nME42_) && (cluster.nStation() >= min_Nstation_) &&
        (cluster.avgStation() >= min_AvgStation_) && ((min_Eta_ < 0.0) || (std::abs(cluster.eta()) >= min_Eta_)) &&
        ((max_Eta_ < 0.0) || (std::abs(cluster.eta()) <= max_Eta_)) && (cluster.time() > min_Time_) &&
        (cluster.time() <= max_Time_) && (cluster.timeSpread() <= max_TimeSpread_)) {
      nClusterPassed++;
    }
  }

  return (nClusterPassed >= min_N_);
}

DEFINE_FWK_MODULE(HLTMuonRecHitClusterFilter);
