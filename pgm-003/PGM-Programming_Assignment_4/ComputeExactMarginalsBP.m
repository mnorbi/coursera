%COMPUTEEXACTMARGINALSBP Runs exact inference and returns the marginals
%over all the variables (if isMax == 0) or the max-marginals (if isMax == 1). 
%
%   M = COMPUTEEXACTMARGINALSBP(F, E, isMax) takes a list of factors F,
%   evidence E, and a flag isMax, runs exact inference and returns the
%   final marginals for the variables in the network. If isMax is 1, then
%   it runs exact MAP inference, otherwise exact inference (sum-prod).
%   It returns an array of size equal to the number of variables in the 
%   network where M(i) represents the ith variable and M(i).val represents 
%   the marginals of the ith variable. 
%
% Copyright (C) Daphne Koller, Stanford University, 2012


function M = ComputeExactMarginalsBP(F, E, isMax)

% initialization
% you should set it to the correct value in your code
M = [];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% YOUR CODE HERE
%
% Implement Exact and MAP Inference.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
V = unique([F(:).var]);
N = length(V);
M = repmat(struct('var', [], 'card', [], 'val',[]), N, 1);

P = CreateCliqueTree(F, E);
P = CliqueTreeCalibrate(P, isMax);

for i = 1:N,
	for j = 1:length(P.cliqueList),
		if intersect(P.cliqueList(j).var, i),
			if isMax,
				M(i) = FactorMaxMarginalization(P.cliqueList(j), setdiff(P.cliqueList(j).var, i));
			else
				M(i) = FactorMarginalization(P.cliqueList(j), setdiff(P.cliqueList(j).var, i));
				M(i).val = M(i).val ./ sum(M(i).val);
			end;
			break;
		end;
	end;
end;
end
